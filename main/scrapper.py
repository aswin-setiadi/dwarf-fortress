from collections import defaultdict
import json

from bs4 import BeautifulSoup
import requests


def main():
    URL = "https://dwarffortresswiki.org/index.php/Personality_trait"
    page = requests.get(URL)
    # print(page.text)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("table", {"class": "wikitable"})
    belief_val_ranges, beliefs, goals, facets_val_ranges, facets = results

    def scrape_beliefs():
        # table-> tbody-> tr
        trs = beliefs.find_all("tr")

        res: dict[str, list[list[str]]] = {}
        key = ""
        # skip table header
        for tr in trs[1:]:
            row: list[str] = []
            for tc in tr:
                if tc.name == "th":
                    a_text = tc.find("a").text.strip()
                    res[a_text] = []
                    key = a_text
                elif tc.name == "td":
                    e_text = tc.text.strip()
                    row.append(e_text)
            res[key].append(row)

        with open("beliefs.json", "w") as f:
            json.dump(res, f)

    def scrape_goals():
        # table-> tbody-> tr
        trs = goals.find_all("tr")

        res: list[list[str]] = []
        # skip table header
        for tr in trs[1:]:
            row: list[str] = []
            for tc in tr:
                if tc.name == "th":
                    a_text = tc.find("a").text.strip()
                    row.append(a_text)
                elif tc.name == "td":
                    e_text = tc.text.strip()
                    row.append(e_text)
            res.append(row)

        with open("goals.json", "w") as f:
            json.dump(res, f)

    def scrape_facets():
        # table-> tbody-> tr
        trs = facets.find_all("tr")

        res: dict[str, list[list[str]]] = {}
        key = ""
        # skip table header
        for tr in trs[1:]:
            row: list[str] = []
            for tc in tr:
                if tc.name == "th":
                    a_text = tc.find("a").text.strip()
                    res[a_text] = []
                    key = a_text
                elif tc.name == "td":
                    e_text = tc.text.strip()
                    row.append(e_text)
            res[key].append(row)

        with open("facets.json", "w") as f:
            json.dump(res, f)

    # scrape_beliefs()
    scrape_goals()
    scrape_facets()


def coba():
    dd: defaultdict[str, set[tuple[int, str]]] = defaultdict(set)
    print(dd)
    dd["LAW"].add((1, "test"))
    print(dd)
    dd["LAW"].add((2, "test2"))
    print(dd)


if __name__ == "__main__":
    main()
