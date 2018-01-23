#!/usr/bin/env python3

import sys
import time
from urllib import request
from xml.etree import ElementTree as etree

failed = False

with request.urlopen('https://podcrto.si/feed/') as feed_response:
    tree = etree.parse(feed_response)

    for link in tree.getroot().findall('./channel/item/link'):
        url = link.text
        with request.urlopen('https://web.archive.org/save/' + url) as archive_response:
            # Read in the whole page to be a good client.
            archive_response.read()

            if archive_response.getcode() != 200:
                print("Archiving '{url}' failed.".format(url=url))
                failed = True

        # Sleep a bit.
        time.sleep(5)

if failed:
    sys.exit(1)
