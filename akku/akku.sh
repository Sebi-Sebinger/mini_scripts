#!/bin/bash

# Akku-Gerät ermitteln
BATTERY=$(upower -e | grep 'BAT')
if [ -z "$BATTERY" ]; then
    echo "Kein Akku gefunden!"
    exit 1
fi

echo "Überwachung des Ladeverhaltens gestartet..."

while true; do
    # Akkustand und Ladezustand abrufen
    CAPACITY=$(upower -i "$BATTERY" | grep "percentage" | awk '{print $2}' | tr -d '%')
    STATUS=$(upower -i "$BATTERY" | grep "state" | awk '{print $2}')
    
    if [ "$CAPACITY" -ge 78 ] && [ "$STATUS" == "charging" ]; then
        notify-send "Bitte Ladegerät ausstecken" "Akkustand: $CAPACITY%. Zum Schutz der Batterie bitte trennen."
    fi
    
    if [ "$CAPACITY" -le 50 ] && [ "$STATUS" == "discharging" ]; then
        notify-send "Bitte Ladegerät einstecken" "Akkustand: $CAPACITY%. Zum Schutz der Batterie bitte anschließen."
    fi
    
    sleep 30  # Alle 30 sek prüfen

done
