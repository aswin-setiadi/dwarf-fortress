import json


def get_beliefs():
    with open("scraps/beliefs.json") as f:
        d = json.load(f)

    for k in d.keys():
        print(k)


def get_goals():
    with open("scraps/goals.json") as f:
        d = json.load(f)

    for l in d:
        print(l[0])


def get_facets():
    with open("scraps/facets.json") as f:
        d = json.load(f)

    for k in d.keys():
        print(k)


if __name__ == "__main__":
    # get_beliefs()
    # get_goals()
    get_facets()
