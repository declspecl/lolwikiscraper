import json
import scrape
import utils
from champion import Champion

def main():
    # all_champs = scrape.get_all_champions(verbose=True)
    all_champs = utils.import_from_json("champs.json")

    utils.export_to_json(all_champs, "champs.json")
    utils.export_with_format(all_champs, "champs.txt", "{N}:\n[\t(S): (N) @ (C)\n]\n")
    utils.export_with_format(all_champs, "champs.md", "# {n}\n## cds\n[- (s): (c)\n]\n")

if __name__ == "__main__":
    main()
