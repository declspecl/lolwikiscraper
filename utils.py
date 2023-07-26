import json
from champion import Champion

def export_to_csv(champions: list[Champion], filename: str, write_slot: bool, write_name: bool, write_cd: bool) -> bool:
    with open(".\\{}.csv".format(filename if not filename.endswith(".csv") else filename[:filename.rfind(".")]), "w+") as file:
        for champion in champions:
            pass

def export_to_json(champions: list[Champion], filename: str) -> bool:
    with open(".\\{}.json".format(filename if not filename.endswith(".csv") else filename[:filename.rfind(".")]), "w+") as file:
        file.write(json.dumps(champions))