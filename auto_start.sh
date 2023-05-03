#!/bin/bash

sleep 10

sudo pigpiod
/usr/bin/python3.9 /home/artur/Desktop/auto-tracking_camera/main.py
