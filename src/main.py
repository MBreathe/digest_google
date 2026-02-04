from gmail import get_gmail
import argparse


def main(**args):
    get_gmail(args["short"], args["unread"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--short", action="store_true", help="Short output")
    parser.add_argument(
        "-u", "--unread", action="store_true", help="Show only unread messages"
    )
    parsed = parser.parse_args()

    main(**vars(parsed))
