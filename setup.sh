#!/bin/bash

pip install -r requirements.txt
chmod 766 morse.py

is_alias=$(alias | grep morse)

if [[ -z "$is_alias" ]]
then
	path=$(find /** -name morse.py 2> /dev/null)
	echo "alias morse='$path'" >> ~/.bash_aliases
fi

