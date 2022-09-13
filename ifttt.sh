#!/bin/bash

touch /home/dimitar/Desktop/web_scrapper/ifttt/web_scrapper_$(date +"%y-%m-%d-%T").txt \
&& rclone copy /home/dimitar/Desktop/web_scrapper/ifttt gdrive:web_scrapper/ifttt
exit
