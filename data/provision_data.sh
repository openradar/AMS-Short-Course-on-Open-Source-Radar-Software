#!/bin/bash
wget \
    https://ndownloader.figshare.com/articles/1537461/versions/6 \
    -O pyart_course_data.zip
unzip -o pyart_course_data.zip
mv 3402575_KAMX_20140417_1056 KAMX_20140417_1056
rm -f pyart_course_data.zip

