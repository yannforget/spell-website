#!/bin/bash

# Connect to ULB VPN
: ${ULB_NETID}
: ${ULB_PASSWD}
echo ${ULB_PASSWD} | openconnect --protocol=gp --user=$ULB_NETID --passwd-on-stdin vpn.ulb.ac.be

# Mirror local changes to a remote SFTP directory
: ${FTP_HOSTNAME:?}
: ${FTP_REMOTEDIR:?}
: ${FTP_USERNAME:?}
: ${FTP_PASSWORD:?}
LOCALDIR="$(cd public && pwd)"
lftp -c "set sftp:auto-confirm yes; open sftp://$FTP_HOSTNAME
user $FTP_USERNAME '$FTP_PASSWORD'
mirror --only-newer --ignore-time --reverse --delete --verbose $LOCALDIR $FTP_REMOTEDIR
"
