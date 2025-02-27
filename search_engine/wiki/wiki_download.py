import os.path
import pickle

import wikipediaapi

from ir_exercise import logger
from ir_exercise.constants import DATA_FOLDER


def download_docs(category, wiki, pages):
    cat = wiki.page(category)
    logger.info(f"{len(cat.categorymembers)} number of movies found in category {category}")
    for member in cat.categorymembers:
        page = wiki.page(member)
        pages.append(page)


def download_category(category, wiki, output):
    pages = []
    download_docs(category, wiki, pages)
    logger.info(f"Downloaded {len(pages)} pages.")
    with open(os.path.join(DATA_FOLDER, output), "wb") as f:
        pickle.dump(pages, f)


def main():
    wiki_wiki = wikipediaapi.Wikipedia("en")
    download_category("Category:2000s English-language films", wiki_wiki, "movies_2000s.pickle")
    download_category("Category:2010s English-language films", wiki_wiki, "movies_2010s.pickle")
    download_category("Category:2020s English-language films", wiki_wiki, "movies_2020s.pickle")


if __name__ == "__main__":
    main()
