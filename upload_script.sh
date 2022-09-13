#!/bin/bash

rclone copy /home/dimitar/Desktop/web_scrapper/2022_dev.xlsx gdrive:web_scrapper --log-file=/home/dimitar/Desktop/web_scrapper/logs/log_dev.txt --log-level INFO

exit
