#!/bin/bash
# print allowed methods
curl -s --head "$1" | grep "Allow" | cut -d ' ' -f2-
