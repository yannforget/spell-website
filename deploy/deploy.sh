#!/usr/bin/env sh

# If last deployment occured during the last five minutes, abort
elapsed=$(deploy/elapsed_time.py "deploy/last_deploy.txt")
mintime=180
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
echo $password | sshfs mgilbert@resu5.ulb.ac.be:/home/web1301/public_html spell.ulb.be -o password_stdin,allow_other
echo "Syncing files..."
rsync -rz --delete public/ spell.ulb.be/
fusermount -u spell.ulb.be
echo "Done."
