import json
import shlex
import os
import socket
import heapq
from collections import OrderedDict, defaultdict

from libmproxy.protocol.http import decoded
from tabulate import tabulate

from recordpeeker import Equipment, ITEMS, slicedict, best_equipment

def get_display_name(enemy):
    for child in enemy["children"]:
        for param in child["params"]:
            return param.get("disp_name", "Unknown Enemy")

def get_drops(enemy):
    for child in enemy["children"]:
        for drop in child["drop_item_list"]:
            yield drop


def handle_get_battle_init_data(data):
    print "Entering battle #{battle_id}..".format(**data["battle"])
    all_rounds_data = data['battle']['rounds']
    tbl = [["rnd", "enemy", "drop"]]
    for round_data in all_rounds_data:
        round = round_data.get("round", "???")
        for enemy in round_data["enemy"]:
            had_drop = False
            enemyname = get_display_name(enemy)
            for drop in get_drops(enemy):
                if "item_id" in drop:
                    kind = "orb id#" if drop["type"] == 51 else "equipment id#"
                    item = ITEMS.get(drop["item_id"], kind + drop["item_id"])
                    itemname = "{0}* {1}".format(drop.get("rarity", "1"), item)
                else:
                    itemname = "{0} gold".format(drop.get("amount", 0))
                had_drop = True
                tbl.append([round, enemyname, itemname])
            if not had_drop:
                tbl.append([round, enemyname, "nothing"])
    print tabulate(tbl, headers="firstrow")
    print ""

def handle_party_list(data):
    wanted = "name series_id acc atk def eva matk mdef mnd series_acc series_atk series_def series_eva series_matk series_mdef series_mnd"
    topn = OrderedDict()
    topn["atk"] = 5
    topn["matk"] = 2
    topn["mnd"] = 2
    topn["def"] = 5
    find_series = [101001, 102001, 104001, 105001, 106001, 107001, 110001]
    equips = defaultdict(list)
    for item in data["equipments"]:
        kind = item.get("equipment_type", 1)
        heapq.heappush(equips[kind], Equipment(slicedict(item, wanted)))

    for series in find_series:
        print "Best equipment for FF{0}:".format((series - 100001) / 1000)

        # Need to use lists for column ordering
        tbl = ["stat n weapon stat n armor stat n accessory".split()]
        tbldata = [[],[],[],[]]
        for itemtype in range(1, 4): ## 1, 2, 3
            for stat, count in topn.iteritems():
                for equip in best_equipment(series, equips[itemtype], stat, count):
                    name = equip["name"].replace(u"\uff0b", "+")
                    tbldata[itemtype].append([stat, equip[stat], name])

        # Transpose data
        for idx in range(0, len(tbldata[1])):
            tbl.append(tbldata[1][idx] + tbldata[2][idx] + tbldata[3][idx])
        print tabulate(tbl, headers="firstrow")
        print ""

def start(context, argv):
    global args
    
    from command_line import parse_args
    split_args = shlex.split(argv[1], False, os.name == "Posix")
    args = parse_args(split_args)
    ip = socket.gethostbyname(socket.gethostname())
    ip = "" if ip == '127.0.0.1' else ip + ", "
    print "Configure your phone's proxy to point to this computer, then visit mitm.it"
    print "on your phone to install the interception certificate.\n"
    print "Record Peeker is listening on {0}port {1}.\n".format(ip, args.port)
    print "Try entering the Party screen, or starting a battle."

handlers = [
    ('/dff/get_battle_init_data' , handle_get_battle_init_data),
    ('/dff/party/list' , handle_party_list)
]

ignored_requests = [
    '/dff/',
    '/dff/splash'
]

def response(context, flow):
    global args
    if flow.request.pretty_host(hostheader=True).endswith('ffrk.denagames.com'):
        if args.verbosity >= 1:
            print flow.request.path
        with decoded(flow.response):
            handler = next((x for x in handlers if x[0] in flow.request.path), None)
            data = json.loads(flow.response.content)
            if handler == None:
                # When verbosity is >= 2, print the content of unknown requests
                if (args.verbosity >= 2) and (flow.request.path not in ignored_requests):
                    print json.dumps(data, sort_keys=True, indent=2, separators=(',', ': '))
            else:
                # When verbosity is >= 3, also print the content of known requests
                if args.verbosity >= 3:
                    print json.dumps(data, sort_keys=True, indent=2, separators=(',', ': '))
                handler[1](data)
