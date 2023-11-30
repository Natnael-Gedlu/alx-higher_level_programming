#!/bin/bash
# script displays size of response in bytes
curl -s "$1" | wc -c
