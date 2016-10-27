#!/usr/bin/env bash

# If last deployment occured during the last five minutes, abort
elapsed=$(deploy/elapsed_time.py "deploy/last_deploy.txt")
mintime=600
echo "Time since last deployment: "$elapsed"s"
if [ ! "$elapsed" > "$mintime" ]
then
    echo "Time since last deployment: "$elapsed"s"
    echo "Not enough elapsed time. Aborting..."
    exit 0
fi

# Log new deploy
date '+%m/%d/%Y %H:%M:%S' > deploy/last_deploy.txt

# Pull from github
echo "Pulling from github..."
git pull
sleep 1

# Update publications
echo "Updating publications from zotero..."
rm -r content/publication
mkdir -p content/publication
deploy/fetch_zotero.py content/publication

# Compile website
echo "Compiling website with hugo..."
hugo

# Mount remote FTP, synchronize data and unmount
echo "Mounting spell.ulb.be FTP..."
source deploy/password.sh
mkdir -p spellftp
echo $password | sshfs mgilbert@resu5.ulb.ac.be:/home/web1301/public_html spellftp -o password_stdin
echo "Syncing files..."
rm -rf spellftp/*
cp -r public/* spellftp/
fusermount -u spell.ulb.be
echo "Done."
