#!/usr/bin/env python3

# A basic command loop

import pickle
import re
import os

SYSDATA_PATH = "sysdata.dat"

def make_empty_sysdata():
    return { "matches": [] }

def read_sysdata(path):
    if os.path.isfile(path):
        return pickle.load(open(path, "rb"))
    return make_empty_sysdata()

def save_sysdata(sysdata, path):
    pickle.dump(sysdata, open(path, "wb"))

def do_register_result(sysdata, tname, tround, playerA, scoreA, playerB, scoreB):
    """Register a game."""
    match = { "tournament": tname, "round": tround, "playerA": playerA, "playerB": playerB, "scoreA": scoreA, "scoreB": scoreB }
    sysdata["matches"].append(match)
    save_sysdata(sysdata, SYSDATA_PATH) 

def do_list_all_matches(sysdata):
    print("{:<10} {:<5} {:<10} {:<10} {:<6} {:<6}".format("Tournament", "Round", "PlayerA", "PlayerB", "ScoreA", "ScoreB"))
    for m in sysdata["matches"]:
        print("{:<10} {:<5} {:<10} {:<10} {:<6} {:<6}".format(m["tournament"], m["round"], m["playerA"], m["playerB"], m["scoreA"], m["scoreB"]))

def command_loop(sysdata):
    while True:
        cmd = input("$ ")
        cmd = cmd.strip()
        m = re.match(r"result\s+(\S+)\s+(\d+)\s+(\S+)\s+(\d+)\s+(\S+)\s+(\d+)$", cmd)
        if m:
            tname = m.group(1)
            tround = int(m.group(2))
            playerA = m.group(3)
            scoreA = int(m.group(4))
            playerB = m.group(5)
            scoreB = int(m.group(6))
            do_register_result(sysdata, tname, tround, playerA, scoreA, playerB, scoreB)
            continue
        if cmd == "list-matches":
            do_list_all_matches(sysdata)
            continue
        if cmd == "quit":
            break
        print("unknown command: " + cmd)

sysdata = read_sysdata(SYSDATA_PATH)
command_loop(sysdata)

