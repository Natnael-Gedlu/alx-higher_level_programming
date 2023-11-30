#!/bin/bash
# script takes URL and displays all accepted methods.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
