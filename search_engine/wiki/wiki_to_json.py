import json
import os.path
import pickle
from argparse import ArgumentParser

from ir_exercise import logger


def get_existing_titles(output):
    titles = []
    if os.path.exists(output):
        with open(output) as f:
            lines = f.readlines()
        for line in lines:
            doc = json.loads(line)
            titles.append(doc["title"])
    return titles


def create_json(input, titles):
    with open(input, "rb") as f:
        pages = pickle.load(f)
    logger.info(f"Start creating {len(pages)} number of jsons from {input}.")
    for i, page in enumerate(pages):
        if i > 0 and i % 500 == 0:
            logger.info(f"Generated {i} number of documents.")
        if page.title in titles:
            continue
        plot, cast = "", ""
        for section in page.sections:
            if section.title == "Plot":
                plot = section.text
            elif section.title == "Cast":
                cast = section.text
        yield {
            "title": page.title,
            "summary": page.summary,
            "text": page.text,
            "plot": plot,
            "cast": cast,
            "links": [link for link in page.links],
            "backlinks": [link for link in page.backlinks],
            "_id": page.title,
        }


def save_jsonl(input, output):
    titles = get_existing_titles(output)
    with open(output, "a") as f:
        for doc in create_json(input, titles):
            json.dump(doc, f)
            f.write("\n")


def main():
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", help="Input pickle.")
    parser.add_argument("-o", "--output", help="Output jsonl file.")
    args = parser.parse_args()
    save_jsonl(args.input, args.output)


if __name__ == "__main__":
    main()
