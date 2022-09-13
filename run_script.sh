#!/bin/bash

python /home/dimitar/Desktop/web_scrapper/web_scrapper_4.py >> /home/dimitar/Desktop/web_scrapper/logs/log_dev.txt && rclone copy /home/dimitar/Desktop/web_scrapper/logs/log_dev.txt gdrive:web_scrapper -P


exit