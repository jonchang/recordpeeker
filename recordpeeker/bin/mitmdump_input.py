import socket

import requests

from recordpeeker.dispatcher import Dispatcher

def enter_dungeon(data, flow):
    global args
    # XXX: This maybe works for all survival events...
    dungeon_request = flow.request.content
    headers = flow.request.headers
    enter_url = flow.request.url
    leave_url = enter_url.replace("enter_dungeon", "leave_dungeon")

    name = data.get("enemy", dict(name="???", memory_factor="0")).get("name")

    while args.find not in name:
        print "Opponent is {0}, retrying...".format(name)
        resp = requests.post(leave_url, headers=headers, data=dungeon_request)
        if resp.status_code != requests.codes.ok: resp.raise_for_status()
        resp = requests.post(enter_url, headers=headers, data=dungeon_request)
        if resp.status_code != requests.codes.ok: resp.raise_for_status()
        data = resp.json()
        name = data.get("enemy", dict(name="???", memory_factor="0")).get("name")

    print "Found {0}! Entering the dungeon now...".format(name)
    flow.response.content = resp.content

def start(context, argv):
    global args

    from recordpeeker.bin.command_line import parse_args
    args = parse_args(argv)
    ips = set([ii[4][0] for ii in socket.getaddrinfo(socket.gethostname(), None) if ii[4][0] != "127.0.0.1"])
    print "Configure your phone's proxy to point to this computer, then visit mitm.it"
    print "on your phone to install the interception certificate.\n"
    print "Record Peeker is listening on port {0}, on these addresses:".format(args.port)
    print "\n".join(["  * {0}".format(ip) for ip in ips])
    print ""
    print "forever24 is waiting for you to enter the magicite factory..."

    global dp
    dp = Dispatcher('ffrk.denagames.com')
    dp.register('/dff/event/coliseum/6/enter_dungeon', enter_dungeon, flow=True)
    [dp.ignore(path, regex) for path, regex in ignored_requests]

ignored_requests = [
    ('/dff/', True),
    ('/dff/splash', False),
    ('/dff/?timestamp', False),
    ('/dff/battle/?timestamp', False),
]

def response(context, flow):
    global args
    global dp
    dp.handle(flow, args)
