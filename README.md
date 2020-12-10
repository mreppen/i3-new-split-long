i3-new-split-long
=====================

IPC script to automatically make the next split along the direction in which there is most space.

The code is based on [i3-alternating-layout](https://github.com/olemartinorg/i3-alternating-layout), but avoids splitting on focus change, as that causes other frustrations in my workflow.  See the section on known problems for the (small) trade-offs.

Note: I am running Sway. Others have tested it on i3.

Installation
------------
The script requires Python 3 and the library `i3ipc` to be installed.

### Ubuntu

```
sudo apt-get install python3-pip git
pip3 install i3ipc
git clone https://github.com/mreppen/3-new-split-long
```
And add `i3_long_split.py` to your `~/.i3/config` autostart:
```
exec --no-startup-id /path/to/i3_long_split.py
```

### Arch Linux
Install `python-i3ipc`, clone the repo, then add
```
exec --no-startup-id /path/to/i3_long_split.py
```
to your `~/.i3/config`.


Screenshot
----------

This screenshot is from [i3-alternating-layout](https://github.com/olemartinorg/i3-alternating-layout), but in this instance, this script does the same thing.

![Screenshot](https://github.com/mreppen/i3-new-split-long/raw/main/screenshot.png "Screenshot (1920x1080)")

Known problems
--------------

1. Because splitting happens after window creation, this can cause a quick flicker from changing layout right after creation.
2. The IPC does not seem to allow subscriptions to window resizes. Window creation immediately after a resize could result in the wrong layout. If focus has changed in-between, this is not a problem.
