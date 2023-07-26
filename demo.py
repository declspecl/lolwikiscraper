import scrape
from champion import Champion

def main():
    riven: Champion = scrape.get_champion("riven", verbose=False)

    print(riven)

    all_champs: list[Champion] = scrape.get_all_champions(verbose=True)

    print(len(all_champs))

    all_champs_dictionary: dict[str, Champion] = scrape.get_all_champions_as_dictionary(verbose=True)

    print(all_champs_dictionary["Riven"])

if __name__ == "__main__":
    main()
