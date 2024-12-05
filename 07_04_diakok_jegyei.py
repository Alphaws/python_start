def diakok_jegyei():
    naplo = [
        {"diak": "Gipsz Jakab", "jegyek": [4, 5, 3, 2, 5, 5]},
        {"diak": "Kis Géza", "jegyek": [3, 1, 3, 1, 3, 1]},
        {"diak": "Nagy Béla", "jegyek": [5, 5, 5, 5, 5, 5]},
        {"diak": "Szabó Ernő", "jegyek": [2, 2, 2, 2, 2, 2]}
    ]

    for diak in naplo:
        atlag = sum(diak["jegyek"]) / len(diak["jegyek"])
        print(f"{diak['diak']} átlaga: {atlag:.2f}, legjobb jegye: {max(diak['jegyek'])}")


if __name__ == "__main__":
    diakok_jegyei()
    