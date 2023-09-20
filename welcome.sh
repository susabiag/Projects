#!/bin/bash
#Good Morning

HOUR=`date +%H`
if  [  $HOUR -ge 12  ]; then
    echo "Good Afternoon!"
fi

if  [  $HOUR -le 11  ]; then
    echo "Good Morning!"
fi
DAYOFWEEK=`date +%A`
case $DAYOFWEEK in
   "Friday")
            echo "Thank goodness it is Friday!"
    ;;
    "Monday")
            echo "I hate Mondays"
    ;;
   "Tuesday" | "Thursday")
            echo "No class today!"
    ;;
   "Wednesday")
	   echo "You have class today with Dr.gidddens!"
    ;;
   *)
            echo "Must be the weekend!"
    ;;
esac

TODAY=`date +%j` 
LASTDAY=`date +%j -d '05/10/22'`
DAYSLEFT=`expr $LASTDAY - $TODAY`
echo "You still have $DAYSLEFT days until the final exam"
