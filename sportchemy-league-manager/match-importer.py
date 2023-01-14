# %%
import os
import sys
import csv
import yaml
from argparse import ArgumentParser

from archetype import DEFAULT

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


def create_match(row):
    match = DEFAULT
    match["home"]["name"] = row["home"]
    match["away"]["name"] = row["away"]
    match["date"] = f"{row['date']} {row['time']}"
    match["court"] = row['court']

    match["title"] = f"{row['home']} vs {row['away']}"
    match["publishDate"] = match["date"]

    return match
# %%


def main(args):
    matches = []
    with open(args["csv"], "r") as f:
        header = next(f).rstrip().split(",")
        data = csv.DictReader(f, fieldnames=header, delimiter=",", quotechar='"',
                              skipinitialspace=True)
        for row in data:
            matches.append(row)

    os.makedirs(args["dst"], exist_ok=True)

    for match in matches:
        match = create_match(match)
        fname = f"{match['date']}_{match['home']['name']}-{match['away']['name']}.md"
        with open(os.path.join(args["dst"], fname), "w") as f:
            content = "---\n" + yaml.dump(match) + "\n---"
            f.write(content)


# %%


if __name__ == "__main__":
    args = parse_args()
    sys.exit(main(args))
