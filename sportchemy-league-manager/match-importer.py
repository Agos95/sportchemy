# %%
import os
import sys
import csv
import yaml
from argparse import ArgumentParser

from match import Match

# %%


def parse_args():
    parser = ArgumentParser(prog="Sportchemy Match Importer",
                            description="Import matches from CSV file.")
    parser.add_argument(
        "--csv", type=str, default="sportchemy-league-manager/test.csv", help="CSV file path.")
    parser.add_argument(
        "-d", "--dst", default="sportchemy-league-manager/match/", help="Folder to save imported matches ['content/match/'].")

    args = parser.parse_args()
    return vars(args)

# %%


def main(args):
    matches = []
    with open(args["csv"], "r") as f:
        header = next(f).rstrip().split(",")
        data = csv.DictReader(f, fieldnames=header, delimiter=",", quotechar='"',
                              skipinitialspace=True)
        for row in data:
            matches.append(Match.from_csv(row))

    os.makedirs(args["dst"], exist_ok=True)

    for match in matches:
        match.write_file(folder=args["dst"])


# %%


if __name__ == "__main__":
    args = parse_args()
    sys.exit(main(args))
