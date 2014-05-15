#!/bin/bash

WHITELISTDIR=/space/distfiles-whitelist
SCRIPTSDIR=/space/prefix-whitelists/scripts
HOMEDIR=/space/prefix-whitelists/home

export PATH=/space/prefix-whitelists/portage/usr/bin:$PATH
export PYTHONPATH=/space/prefix-whitelists/portage/usr/lib/portage/pym:$PYTHONPATH

cd "${HOMEDIR}"

bash "${SCRIPTSDIR}"/update-prefix-tree.sh
bash "${SCRIPTSDIR}"/update-prefix-snapshots.sh

[[ -e $WHITELISTDIR/prefix-tree ]] && mv $WHITELISTDIR/prefix-tree $WHITELISTDIR/prefix-tree.old
cp prefix-tree-whitelist $WHITELISTDIR/prefix-tree
rm -f $WHITELISTDIR/prefix-tree.old

[[ -e $WHITELISTDIR/prefix-bootstrap-snapshot ]] && mv $WHITELISTDIR/prefix-bootstrap-snapshot $WHITELISTDIR/prefix-bootstrap-snapshot.old
cp prefix-bootstrap-snapshot-whitelist $WHITELISTDIR/prefix-bootstrap-snapshot
rm -f $WHITELISTDIR/prefix-bootstrap-snapshot.old
