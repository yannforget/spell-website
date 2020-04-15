#!/bin/bash

# Connect to ULB VPN
echo $ULB_PASSWD | sudo openconnect --protocol=gp --user=$ULB_NETID --passwd-on-stdin vpn.ulb.ac.be &
sleep 3

# Mirror local changes to a remote SFTP directory
LOCALDIR="$(cd public && pwd)"
lftp -c "set sftp:auto-confirm yes; open sftp://$FTP_HOSTNAME
user $FTP_USERNAME '$FTP_PASSWORD'
mirror --only-newer --ignore-time --reverse --delete --verbose $LOCALDIR $FTP_REMOTEDIR
"

# Close VPN
sudo killall openconnect
