#!/home/jake/anaconda3/envs/310/bin/python3
'''
File: radio.py
Created Date: 21 Sep 2022
Author: Jake Skelton
Date Modified: Fri Sep 30 2022
Copyright (c): 2022 Jake Skelton
'''

import os
import sys
import vlc

stations_dict = {
    'q':'',  # Stop playing
    'NTS 1':'http://stream-relay-geo.ntslive.net/stream',
    'NTS 2':'http://stream-relay-geo.ntslive.net/stream2',
    'Rinse FM':'http://206.189.117.157:8000/stream',
    'Balamii':'http://balamii.out.airtime.pro:8000/balamii_a',
    'Worldwide FM':'http://worldwidefm.out.airtime.pro:8000/worldwidefm_a',
    'BBC radio 6 music':'http://open.live.bbc.co.uk/mediaselector/5/select/version/2.0/mediaset/http-icy-mp3-a/vpid/bbc_6music/format/pls.pls',
    'KUVO Denver':'http://kuvo-ice.streamguys.org/kuvo-aac-128',
    'FIP jazz':'http://icecast.radiofrance.fr/fipjazz-hifi.aac',
    'Jungletrain':'http://jungletrain.net/128kbps.pls',
}
stations = list(stations_dict.keys())
urls = list(stations_dict.values())

instance = vlc.Instance()
player = instance.media_player_new()

print("Please choose a radio station from the following:")
i = 1
for s in stations[1:]:
    print("%d: %s"%(i, s))
    i += 1

while True:
    try:
        prompt = input()
        try:
            if prompt.isdigit():
                url = urls[int(prompt)]
            else:
                url = stations_dict[prompt]
            if url:  # If station not empty string
                media = instance.media_new(url)
            else:
                continue
        except Exception as e:
            print("Input not parseable: ", e)
            continue

        print("Connecting to %s"%url)
        player.set_media(media)
        player.play()

    except KeyboardInterrupt:
        break
