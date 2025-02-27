import json
import re
from argparse import ArgumentParser
from typing import Callable, Generator

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

from ir_exercise import logger
from ir_exercise.constants import INDEX_NAME, DATA_PATH


class Indexer:
    def __init__(self):
        self.es_client = Elasticsearch(
            ["http://localhost:9200"],
        )
        self.es_client.ping()

    def _create_mappings(self):
        # Todo:
        #  Improve mapping by defining separate analyzers for separate fields
        #  See an example mapping provided for the title field, with a keyword analyzer
        #  More details:
        #  - https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping.html
        return {
            "properties": {
                "cast": {
                    "type": "keyword",  # No need for tokenization, so keyword is used
                },
                "title": {
                    "type": "text",
                    "analyzer": "title_analyzer",  # Use the custom analyzer for title
                },
                "summary": {
                    "type": "text",
                    "analyzer": "custom_analyzer",  # Use the custom analyzer for summary
                },
                "plot": {
                    "type": "text",
                    "analyzer": "custom_analyzer"  # Optionally, use the same analyzer for plot
                },
                "text": {
                    "type": "text",
                    "analyzer": "custom_analyzer"  # Apply analyzer for the 'text' field
                }
            }
        }

    def _create_settings(self):
        # Todo:
        #  Define your own tokenizers, filters and analyzers here
        #  More details:
        #   - https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-tokenizers.html
        #   - https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-tokenfilters.html
        #   - https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-analyzers.html
        return {
            "analysis": {
                "filter": {
                    "my_stop": {
                        "type": "stop",
                        "stopwords": [
                            "a", "and", "at", "but", "by", "for", "if", "in", "is", "it", "of", "on", "or", "the",
                            "to"
                        ]
                    },
                    "filter_synonym": {
                        "type": "synonym",
                        "synonyms": [
                            "case, mystery, game, murder",
                            "2, two"
                        ]
                    }
                },
                "analyzer": {
                    "title_analyzer": {  # Simple analyzer for titles
                        "type": "custom",
                        "tokenizer": "standard",
                        "filter": ["lowercase", "filter_synonym"]
                    },
                    "custom_analyzer": {  # Complex analyzer for summaries
                        "type": "custom",
                        "tokenizer": "standard",
                        "filter": [
                            "lowercase",
                            "my_stop",
                            "filter_synonym"
                        ]
                    }
                }
            }
        }

    def create_index(self, index_name: str, recreate: bool = False) -> None:
        if self.es_client.indices.exists(index=index_name):
            if recreate:
                logger.info("Index will be deleted and recreated.")
                self.es_client.indices.delete(index=index_name)
            else:
                logger.info("Index already exists nothing to be done.")
                return
        mappings = self._create_mappings()
        settings = self._create_settings()
        logger.info(
            f"Creating index {index_name} with the following settings:\n{json.dumps(settings, indent=2)}\n"
            f"and with following mapping:{json.dumps(mappings, indent=2)}"
        )
        self.es_client.indices.create(index=index_name, mappings=mappings, settings=settings)

    def populate_index(
            self, index_name: str, data_path: str, generate: Callable[[str, str], Generator]
    ) -> None:
        logger.info(f"Populating index {index_name}...")
        bulk(self.es_client, generate(index_name, data_path), refresh=True)
        result = self.es_client.search(index=index_name, query={"match_all": {}}, scroll="1m")
        nr_docs = result["hits"]["total"]["value"]
        logger.info(f"Index populated with {nr_docs} documents.")

def strip(title):
    return re.sub(r'\(.*?\)', '', title).strip()

def generate_data(index_name: str, data_path: str):
    logger.info(f"Loading data from {data_path}.")
    with open(data_path) as f:
        lines = f.readlines()
    logger.info(f"Start indexing {len(lines)} number of docs from {data_path}.")
    for i, line in enumerate(lines):
        doc = json.loads(line)
        if i > 0 and i % 1000 == 0:
            logger.info(f"Generated {i} number of documents.")
        # Todo:
        #  Include more fields if necessary, e.g.:
        #   - fields that already exist in the data
        #   - complete new fields that you come up with, e.g. a separate field with partial data
        yield {
            "title": doc["title"],
            "summary": doc["summary"],
            "stripped_title": strip(doc["title"]),
            "_index": index_name,
            "_id": doc["title"],
            "cast": doc.get("cast", "N/A"),  # Make sure the 'cast' field is indexed
            "plot": doc.get("plot", "N/A"),  # Include 'plot' field if needed
            "text": doc.get("text", "N/A")  # Include 'text' field if needed
        }


def get_args():
    parser = ArgumentParser()
    parser.add_argument(
        "-r",
        "--recreate",
        action="store_true",
        help="If set, already existing index will be deleted and recreated. "
             "If not set, the index will be kept and documents with the same id will be overwritten.",
    )
    parser.add_argument(
        "-i",
        "--index",
        default=INDEX_NAME,
        help=f"Name of the index. If left empty it defaults to '{INDEX_NAME}.",
    )
    parser.add_argument(
        "-d",
        "--data-path",
        default=DATA_PATH,
        help=f"Path to the data. If left empty it defaults to '{DATA_PATH}.",
    )
    return parser.parse_args()


def main():
    args = get_args()
    indexer = Indexer()
    indexer.create_index(args.index, recreate=args.recreate)
    indexer.populate_index(args.index, args.data_path, generate_data)


if __name__ == "__main__":
    main()
