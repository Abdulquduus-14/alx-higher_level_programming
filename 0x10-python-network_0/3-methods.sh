#!/bin/bash
# a Bash script that takes in a URL and displays all methods
# the server will accept.
curl -sI "$1" -X OPTIONS | grep "ALLOW" | cut -d " " -f 2
