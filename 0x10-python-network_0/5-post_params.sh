#!/bin/bash
# script sends POST request and displays response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
