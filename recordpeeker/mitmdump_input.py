import json
from ast import literal_eval
import socket
import heapq
from collections import OrderedDict

from libmproxy.protocol.http import decoded

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
    for round_data in all_rounds_data:
        print "  Round {0}:".format(round_data.get("round", "???"))
        for enemy in round_data["enemy"]:
            had_drop = False
            name = get_display_name(enemy)
            for drop in get_drops(enemy):
                if "item_id" in drop:
                    kind = "orb id#" if drop["type"] == 51 else "equipment id#"
                    item = ITEMS.get(drop["item_id"], kind + drop["item_id"])
                    print "    {0} drops {rarity}* {1}".format(name, item, **drop)
                else:
                    print "    {0} drops {amount} gold".format(name, **drop)
                had_drop = True
            if not had_drop:
                print "    {0} drops nothing!".format(name)
    print ""

def handle_party_list(data):
    wanted = "name series_id acc atk def eva matk mdef mnd series_acc series_atk series_def series_eva series_matk series_mdef series_mnd"
    topn = OrderedDict()
    topn["atk"] = 5
    topn["matk"] = 2
    topn["mnd"] = 2
    topn["def"] = 5
    find_series = [101001, 102001, 104001, 105001, 106001, 107001, 110001]
    heap = []
    for item in data["equipments"]:
        heapq.heappush(heap, Equipment(slicedict(item, wanted)))
    for series in find_series:
        print "Best equipment for FF{0}:".format((series - 100001) / 1000)
        for stat, count in topn.iteritems():
            for equip in best_equipment(series, heap, stat, count):
                name = equip["name"].replace(u"\uff0b", "+")
                print "  {0}: {1} -- {2}".format(stat, equip[stat], name)
    print ""

def start(context, argv):
    global conf
    conf = literal_eval(argv[1])
    ip = socket.gethostbyname(socket.gethostname())
    ip = "" if ip == '127.0.0.1' else ip + ", "
    print "Configure your phone's proxy to point to this computer, then visit mitm.it"
    print "on your phone to install the interception certificate.\n"
    print "Record Peeker is listening on {0}port {port}.\n".format(ip, **conf)
    print "Try entering the Party screen, or starting a battle."



def response(context, flow):
    if flow.request.pretty_host(hostheader=True).endswith('ffrk.denagames.com'):
        with decoded(flow.response):
            if 'get_battle_init_data' in flow.request.path:
                data = json.loads(flow.response.content)
                handle_get_battle_init_data(data)
            elif 'party/list' in flow.request.path:
                data = json.loads(flow.response.content)
                handle_party_list(data)
