from argparse import ArgumentParser


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
    parser.add_argument(
        "--timeout",
        type=int,
        default=30,
        help="Request timeout in seconds (default: 30).",
    )

    args = parser.parse_args()

    print(args)


if __name__ == "__main__":
    main()
