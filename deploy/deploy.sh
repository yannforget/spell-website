#!/usr/bin/env sh

# If last deployment occured during the last five minutes, abort
elapsed=$(deploy/elapsed_time.py "deploy/last_deploy.txt")
mintime=180
if [ ! "$elapsed" > "$mintime" ]
then
   exit 0
fi

# Log new deploy
date '+%m/%d/%Y %H:%M:%S' > deploy/last_deploy.txt

# Pull from github
git pull
sleep 1

# Update publications
rm -r content/publication
mkdir -p content/publication
deploy/fetch_zotero.py content/publication

# Compile website
hugo

# Mount remote FTP, synchronize data and unmount
echo $SPELL_PASSWORD | sshfs mgilbert@resu5.ulb.ac.be:/home/web1301/public_html spell.ulb.be -o password_stdin,allow_other
rsync -rz --delete public/ spell.ulb.be/
fusermount -u spell.ulb.be
