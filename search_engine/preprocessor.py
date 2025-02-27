import argparse
import os

import requests

from ir_exercise import logger
from ir_exercise.constants import DATA_FOLDER, DATA_PATH


class Preprocessor:
    def __init__(self, download):
        self.DOWNLOAD_LINK = "https://owncloud.tuwien.ac.at/index.php/s/klYjT0Xq2HourVo/download"
        self.download = download
        self.data = []

    def create_data(self):
        if self.download:
            self._download()
        else:
            logger.info("Download is set to false, no data will be downloaded from source url.")

    def _download(self):
        if not os.path.exists(DATA_FOLDER):
            os.makedirs(DATA_FOLDER)
        if os.path.exists(DATA_PATH):
            logger.warning(f"Path {DATA_PATH} already exists and it will be overwritten.")
        logger.info("Downloading data...")
        response = requests.get(self.DOWNLOAD_LINK)
        open(DATA_PATH, "wb").write(response.content)
        logger.info(f"Data is successfully downloaded to: {DATA_PATH}")


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--download",
        action="store_true",
        help="True if data should be downloaded from source url.",
    )
    return parser.parse_args()


def main():
    args = get_args()
    preprocessor = Preprocessor(args.download)
    preprocessor.create_data()


if __name__ == "__main__":
    main()
