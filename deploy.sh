#!/bin/bash

# Connect to ULB VPN
echo $ULB_PASSWD | sudo openconnect --protocol=gp --background --user=$ULB_NETID --passwd-on-stdin vpn.ulb.ac.be 
sleep 5

mkdir -p ~/.ssh
touch ~/.ssh/known_hosts
ssh-keyscan -H $FTP_HOSTNAME >> ~/.ssh/known_hosts

if ping -c 1 $FTP_HOSTNAME &> /dev/null
then
  echo "Connection to $FTP_HOSTNAME successfull"
else
  echo "Connection to $FTP_HOSTNAME failed"
fi

# Mirror local changes to a remote SFTP directory
echo "Uploading changes..."
LOCALDIR="$(cd public && pwd)"
lftp -c "set sftp:auto-confirm yes; open sftp://$FTP_HOSTNAME
user $FTP_USERNAME '$FTP_PASSWORD'
mirror --only-newer --ignore-time --reverse --delete --verbose $LOCALDIR $FTP_REMOTEDIR
"

# Close VPN
sudo killall openconnect
