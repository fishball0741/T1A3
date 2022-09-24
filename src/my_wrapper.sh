#!/bin/bash
a=$(python3 --version)

if  [[ "$a" > 3 ]]
then
    echo python "$a" is installed running the application...
    python3 main.py "$@"
else
    echo 'Error: 
    This program runs on Python, but it looks like Python is not installed.
    To install Python, check out https://installpython3.com/' >&2
  exit 1
fi


