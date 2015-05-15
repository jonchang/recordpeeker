import csv
from pkg_resources import resource_stream
import heapq
import json

import command_line

def json_decode(string):
    """Windows likely does not have utf8 as the system encoding and Python is
    too stubborn to provide a sensible default."""
    return json.loads(string.decode('utf-8-sig'))


class Equipment(dict):
    def __init__(self, sourcedict):
        dict.__init__(self, **sourcedict)

    def rs(self, series):
        if self["series_id"] == int(series):
            return {"name": self["name"], "acc": self["series_acc"], "atk": self["series_atk"],
                    "def": self["series_def"], "eva": self["series_eva"], "matk": self["series_matk"],
                    "mdef":self["series_mdef"], "mnd":self["series_mnd"]}
        else:
            return slicedict(self, "name acc atk def eva matk mdef mnd".split())

def slicedict(d, s):
    return {k:v for k,v in d.iteritems() if k in s}

def best_equipment(series, heap, stat, n=3):
    n_seen = 0
    seen_eq = []
    last_seen = None
    for item in sorted(heap, key=lambda x: x.rs(series)[stat], reverse=True):
        if n_seen == n:
            break
        if item.rs(series) == last_seen or item.rs(series) in seen_eq:
            continue
        seen_eq.append(item.rs(series))
        n_seen += 1
        yield item.rs(series)
    else:
        for ii in range(n - n_seen):
            yield {"name": "n/a", "acc": 0, "atk": 0, "def": 0, "eva": 0, "matk": 0, "mdef": 0, "mnd": 0}

def load_dict(path):
    res = dict()
    rfile = resource_stream("recordpeeker", path)
    reader = csv.reader(rfile)
    for row in reader:
        res[row[0]] = row[1]
    return res

ITEMS = load_dict("data/items.csv")
BATTLES = load_dict("data/battles.csv")
DUNGEONS = load_dict("data/dungeons.csv")
