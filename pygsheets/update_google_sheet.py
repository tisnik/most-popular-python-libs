#!/usr/bin/env python3

"""Import CSV into Google sheet.

In order to use this script, file with client secret to Google API must be present (symlinked etc.)

Please look into official documentation how to create service account and retrieve client secret:
https://cloud.google.com/iam/docs/service-accounts-create

usage: import_csv_into_google_sheet.py [-h]
                                       [--input CSV file to be imported]
                                       [-s SPREADSHEET]

CSV Uploader

options:
  -h, --help            show this help message and exit
  --input FILENAME      CSV file to be imported
  -s SPREADSHEET, --spreadsheet SPREADSHEET
                        Spreadsheed title as displayed on Google doc
"""

import argparse
import csv
import logging
import sys

import pygsheets

logger = logging.getLogger("CSV importer")


def args_parser(args: list[str]) -> argparse.Namespace:
    """Command line arguments parser."""
    parser = argparse.ArgumentParser(description="CSV uploader")
    parser.add_argument(
        "--input",
        type=str,
        default="input.csv",
        help="CSV file to be imported",
    )
    parser.add_argument(
        "-s",
        "--spreadsheet",
        type=str,
        default="Test",
        help="Spreadsheed title as displayed on Google doc",
    )
    return parser.parse_args(args)


def upload_csv_file(worksheet, filename):
    """Upload selected file into selected worksheet."""
    logger.info(f"Uploading file {filename}")

    # Read CSV and update
    with open(filename, "r") as file:
        csv_reader = csv.reader(file)
        worksheet.update_values("A1", list(csv_reader))

    logger.info("Upload finished")


def perform_upload(
    spreadsheet_title, file
):
    """Perform uploading."""
    # first authorize access to sheet
    logger.info("Authorizing to Google docs.")
    gc = pygsheets.authorize(service_file="clanek_secret.json")

    # open Google sheet
    logger.info(f"Opening spreadsheet with title {spreadsheet_title}")
    sheet = gc.open(spreadsheet_title)
    logger.info(f"ID={sheet.id}")
    logger.info(f"Title={sheet.title}")
    logger.info(f"URL={sheet.url}")

    upload_csv_file(sheet[0], file)

    logger.info("Done")


def main() -> None:
    """Upload selected CSV file into existing Google sheet."""
    logging.basicConfig(level=logging.INFO)
    args = args_parser(sys.argv[1:])
    perform_upload(
        args.spreadsheet,
        args.input,
    )


if __name__ == "__main__":
    main()
