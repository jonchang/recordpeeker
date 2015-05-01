import json
import csv
from ast import literal_eval
from pkg_resources import Requirement, resource_stream
import socket

from libmproxy.protocol.http import decoded

def load_item_dict():
    res = dict()
    rfile = resource_stream("recordpeeker", "data/items.csv")
    reader = csv.reader(rfile)
    for row in reader:
        res[row[0]] = row[1]
    return res

def get_display_name(enemy):
    for child in enemy["children"]:
        for param in child["params"]:
            return param.get("disp_name", "Unknown Enemy")

def get_drops(enemy):
    for child in enemy["children"]:
        for drop in child["drop_item_list"]:
            yield drop


def handle_get_battle_init_data(data):
    items = load_item_dict()
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
                    item = items.get(drop["item_id"], kind + drop["item_id"])
                    print "    {0} drops {rarity}* {1}".format(name, item, **drop)
                else:
                    print "    {0} drops {amount} gold".format(name, **drop)
                had_drop = True
            if not had_drop:
                print "    {0} drops nothing!".format(name)

def start(context, argv):
    global conf
    conf = literal_eval(argv[1])
    ip = socket.gethostbyname(socket.gethostname())
    ip = "" if ip == '127.0.0.1' else ip + ", "
    print "Configure your phone's proxy to point to this computer, then visit mitm.it"
    print "on your phone to install the interception certificate.\n"
    print "Record Peeker is listening on {0}port {port}...".format(ip, **conf)


def response(context, flow):
    if flow.request.pretty_host(hostheader=True).endswith('ffrk.denagames.com'):
        with decoded(flow.response):
            if 'get_battle_init_data' in flow.request.path:
                data = json.loads(flow.response.content)
                handle_get_battle_init_data(data)
