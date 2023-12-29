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


def sort_beliefs():
    with open("scraps/beliefs.json") as f:
        d = json.load(f)
    new_d = {}
    for k, v in d.items():
        tmp = [x[1] for x in v]
        new_d[k] = tmp
    sorted_d = dict(sorted(new_d.items()))
    with open("scraps/beliefs_sorted.json", "w") as f:
        json.dump(sorted_d, f)


def sort_facets():
    with open("scraps/facets.json") as f:
        d = json.load(f)
    new_d = {}
    for k, v in d.items():
        tmp = [x[1] for x in v]
        new_d[k] = tmp
    sorted_d = dict(sorted(new_d.items()))
    with open("scraps/facets_sorted.json", "w") as f:
        json.dump(sorted_d, f)


def sort_goals():
    with open("scraps/goals.json") as f:
        l = json.load(f)
    new_l: list[str] = []
    for v in l:
        new_l.append(v[0])
    new_l.sort()
    with open("scraps/goals_sorted.json", "w") as f:
        json.dump(new_l, f)


def sort_atbs():
    with open("scraps/master_list/attributes_master_list.json") as f:
        d = json.load(f)

    new_d = dict(sorted(d.items()))
    with open("a.json", "w") as f:
        json.dump(new_d, f)


if __name__ == "__main__":
    # get_beliefs()
    # get_goals()
    # get_facets()
    # sort_beliefs()
    # sort_facets()
    # sort_goals()
    sort_atbs()
