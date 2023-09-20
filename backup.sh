#!/bin/bash
if  [  !   -d   /home/susabiag/backup  ];   then
     mkdir  /home/susabiag/backup
fi
MONTH=`date +%b`
DAY=`date +%d`
tar  -zcf   /home/susabiag/backup/bin$MONTH$DAY.tgz     /home/susabiag/bin
echo  Backup complete
