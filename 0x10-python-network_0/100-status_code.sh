#!/bin/bash
# Print the status code from a request
curl --silent --write-out "%{http_code}" "$1" --output /dev/null
