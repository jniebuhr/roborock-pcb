#!/usr/bin/env bash
rm assets/pinout.png
python3 -m pinout.manager --export scripts/pinout_diagram.py assets/pinout.png