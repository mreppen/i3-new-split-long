i3-new-split-long
=====================

IPC script to automatically make the next split along the direction in which there is most space.

The code is based on [i3-alternating-layout](https://github.com/olemartinorg/i3-alternating-layout), but avoids splitting on focus change, as that causes other frustrations in my workflow.

Installation
------------
The script requires Python 3 and the library `i3ipc` to be installed.

### Ubuntu

```
sudo apt-get install python3-pip git
pip3 install i3ipc
git clone https://github.com/mreppen/3-new-split-long
```
And add `alternating_layouts.py` to your `~/.i3/config` autostart:
```
exec --no-startup-id /path/to/alternating_layouts.py
```

### Arch Linux
Install `python-i3ipc`, clone the repo, then add
```
exec --no-startup-id /path/to/alternating_layouts.py
```
to your `~/.i3/config`.


Screenshot
----------

This screenshot is from [i3-alternating-layout](https://github.com/olemartinorg/i3-alternating-layout), but in this instance, this script does the same thing.

![Screenshot](https://github.com/mreppen/i3-new-split-long/raw/main/screenshot.png "Screenshot (1920x1080)")
