#!/usr/bin/bash
# script prints size in bytes, 
curl -s "$1" | wc -c
