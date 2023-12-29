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
    # scrape_goals()
    # scrape_facets()


def scrape_atbs():
    metas = [
        ("GOOD4", "1000"),
        ("GOOD3", "750"),
        ("GOOD2", "500"),
        ("GOOD1", "250"),
        ("NEUTRAL", "0"),
        ("BAD1", "-250"),
        ("BAD2", "-500"),
        ("BAD3", "-750"),
        ("BAD4", "-1000"),
    ]
    URL = "https://dwarffortresswiki.org/index.php/Attribute"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("table", {"class": "wikitable"})
    d = {}
    index = 0
    for res in results[:19]:
        trs = res.find_all("tr")
        l: list[str] = []
        count = 0
        for tr in trs[1:]:
            td = tr.find_all("td")[1]
            tpl = metas[count % 9]
            l.append(f"{tpl[1]}.{tpl[0]}| {td.text.strip()}")
            count += 1
        d[index] = l
        index += 1
    with open("scraps/attributes_master_list.json", "w") as f:
        json.dump(d, f)


def coba():
    dd: defaultdict[str, set[tuple[int, str]]] = defaultdict(set)
    print(dd)
    dd["LAW"].add((1, "test"))
    print(dd)
    dd["LAW"].add((2, "test2"))
    print(dd)


if __name__ == "__main__":
    # main()
    scrape_atbs()
