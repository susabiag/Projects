#!/bin/bash
#Calculator

if [ $# != 3 ]; then
  echo You did not run the program correctly
  echo Example:coursegrade.sh Giddens 70 85
   exit 1
fi

if [ $2 -gt $3 ]; then
  echo $2 is the best grade
	if [ $2 -le 59 ]; then
		echo You got a F on the class
	fi
	if [[ $2 -le 69 && $2 -ge 60 ]]; then
		echo You got a D on the class
	fi
	if [[ $2 -le 79 && $2 -ge 70 ]]; then
		echo You got a C on the class
	fi
	if [[ $2 -le 89 && $2 -ge 80 ]]; then
		echo You got a B on the class
	fi
	if [[ $2 -le 100 && $2 -ge 90 ]]; then
		echo You got an A on the class
	fi
	exit

fi

if [ $3 -gt $2 ]; then
  echo $3 is the best grade
	if [ $3 -le 59 ]; then
		echo You got a F on the class
	fi
	if [[ $3 -le 69 && $3 -ge 60 ]]; then
		echo You got a D on the class
	fi
	if [[ $3 -le 79 && $3 -ge 70 ]]; then
		echo You got a C on the class
	fi
	if [[ $3 -le 89 && $3 -ge 80 ]]; then
		echo You got a B on the class
	fi
	if [[ $3 -le 100 && $3 -ge 90 ]]; then
		echo You got an A on the class
	fi
	exit 
fi
