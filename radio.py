#!/home/jake/anaconda3/envs/310/bin/python3
'''
File: radio.py
Created Date: 21 Sep 2022
Author: Jake Skelton
Date Modified: Wed Sep 21 2022
Copyright (c): 2022 Jake Skelton
'''

import os
import sys
import vlc

nts1 = 'http://stream-relay-geo.ntslive.net/stream'

instance = vlc.Instance()
player = instance.media_player_new()

while True:
    prompt = input()


media = instance.media_new(nts1)
player.set_media(media)
player.play()
