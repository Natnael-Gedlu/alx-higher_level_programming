#!/bin/bash
# script sends  GET request and display the response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
