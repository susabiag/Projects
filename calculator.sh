#!/bin/bash
#Calculator




if [ $# != 3 ]; then
  echo You did not run the program correctly
  echo Example: calculator.sh 4 + 5
   exit 1
fi

# Now do the math

if [ $2 = "+" ]; then
   ANSWER=`expr $1 + $3`
   echo The sum of $1 and $3 is $ANSWER
fi
if [ $2 = "-" ]; then
   ANSWER=`expr $1 - $3`
   echo The minus of $1 and $3 is $ANSWER
fi
if [ $2 = "x" ]; then
   ANSWER=`expr $1 \*  $3`
   echo The product of $1 and $3 is $ANSWER
fi

if [ $2 = "/" ]; then
   if [ $3 = "0" ]; then
     echo You cannot divide by 0
     exit 
   fi

   ANSWER=`expr $1 /  $3`
   echo The division of $1 and $3 is $ANSWER
fi

exit 0
