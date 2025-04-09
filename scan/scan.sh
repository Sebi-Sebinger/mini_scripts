#!/bin/bash

# Subnetz automatisch ermitteln
SUBNET=$(ip -o -f inet addr show | awk '/scope global/ {print $4}' | cut -d. -f1-3)

if [ -z "$SUBNET" ]; then
  echo "Could not detect subnet. Please specify manually."
  exit 1
fi

echo "Detected subnet: $SUBNET"

for i in {1..254}; do
  (ping -c 1 $SUBNET.$i | grep "bytes from" &) 
done
