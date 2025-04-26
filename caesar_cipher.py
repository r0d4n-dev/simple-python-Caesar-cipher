import argparse


def parse_file(filename: str) -> str:
    """Parse text from the input file"""

    with open(filename, "r", encoding="utf-8") as file:
        file_contents = file.read()

    return file_contents


def main():
    # file, or text
    # left shift or right shift ammount

    # Parse comand-line arguments
    parser = argparse.ArgumentParser(
        description="Simple tool to encrypt plain text that is in a file using a Caesar cipher"
    )

    parser.add_argument("filename", help="Plaintext file to encrypt.")
    parser.add_argument(
        "-s",
        "--shift",
        type=int,
        help="Shift to use for the cipher. Positive number for a left shift and negative number for a right shift",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Name of output file. If omitted, output is dsiplayed on the standard output",
    )

    args = parser.parse_args()


if __name__ == "__main__":
    main()
