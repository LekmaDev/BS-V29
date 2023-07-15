#!/bin/bash
while true
do
    sudo fuser -k 9339/tcp
    python3 core.py
done
