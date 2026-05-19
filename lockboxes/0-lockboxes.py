#!/usr/bin/env python3
"""0-lockboxes.py"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened."""
    if not boxes:
        return False

    opened = set()
    to_open = [0]

    while to_open:
        box = to_open.pop()
        if box not in opened and 0 <= box < len(boxes):
            opened.add(box)
            to_open.extend(boxes[box])

    return len(opened) == len(boxes)
