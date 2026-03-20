from argparse import ArgumentParser
from sys import exit


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        help="make it verbose",
        action="store_true",
        default=None,
    )
    parser.add_argument(
        "-n",
        "--no-colors",
        dest="nocolors",
        help="disable color output",
        action="store_true",
        default=None,
    )
    parser.add_argument(
        "-d",
        "--directory",
        dest="directory",
        help="directory with JSON files to check",
        action="store",
        default=".",
    )

    args = parser.parse_args()

    print(args)
    exit(1)


if __name__ == "__main__":
    main()
