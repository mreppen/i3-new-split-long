#!/usr/bin/env python3

import getopt
import sys
import os
from i3ipc import Connection, Event

last_focus_con = None

def find_parent(i3, window_id):
    """
        Find the parent of a given window id
    """

    def finder(con, parent):
        if con.id == window_id:
            return parent
        for node in con.nodes:
            res = finder(node, con)
            if res:
                return res
        return None

    return finder(i3.get_tree(), None)

def split_move_new(i3, e):
    parent = find_parent(i3, e.container.id)
    if parent is None or (parent.workspace() is parent and len(parent.nodes) == 1):
        return

    playout = parent.layout

    if last_focus_con.rect.height > last_focus_con.rect.width:
        command = f"[con_id={last_focus_con.id}] split v; "
    else:
        command = f"[con_id={last_focus_con.id}] split h; "

    if playout == "splitv":
        command += f"[con_id={e.container.id}] move up"
    elif playout == "splith":
        command += f"[con_id={e.container.id}] move left"

    i3.command(command)

def record_focus(i3, e):
    global last_focus_con
    last_focus_con = i3.get_tree().find_by_id(e.container.id)

def print_help():
    print("Usage: " + sys.argv[0] + " [-p path/to/pid.file]")
    print("")
    print("Options:")
    print("    -p path/to/pid.file   Saves the PID for this program in the filename specified")
    print("")

def main():
    """
    Main function - listen for window focus
        changes and call set_layout when focus
        changes
    """
    opt_list, _ = getopt.getopt(sys.argv[1:], 'hp:')
    pid_file = None
    for opt in opt_list:
        if opt[0] == "-h":
            print_help()
            sys.exit()
        if opt[0] == "-p":
            pid_file = opt[1]

    if pid_file:
        with open(pid_file, 'w') as f:
            f.write(str(os.getpid()))

    i3 = Connection()
    global last_focus_con
    last_focus_con = i3.get_tree().find_focused()
    i3.on(Event.WINDOW_NEW, split_move_new)
    i3.on(Event.WINDOW_FOCUS, record_focus)
    i3.main()


if __name__ == "__main__":
    main()
