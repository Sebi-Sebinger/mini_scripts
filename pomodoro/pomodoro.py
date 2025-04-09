#!/usr/bin/env python3
import time
import subprocess
import signal
import os

def start_countdown(minutes, round_number):
    seconds = minutes * 60
    notification = f"Runde {round_number}"
    subprocess.run(["notify-send", notification])
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"Verbleibende Zeit: {timer}", end='\r')
        time.sleep(1)
        seconds -= 1

    print("\nZeit abgelaufen!")

def start_pause(minutes, round_number):
    seconds = minutes * 60
    notification = f"Pause von Runde {round_number}"
    subprocess.run(["notify-send", notification])
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"Pausenzeit: {timer}", end='\r')
        time.sleep(1)
        seconds -= 1

    print("\nPausenzeit abgelaufen!")

def terminate_processes(process_names):
    for process_name in process_names:
        try:
            subprocess.run(["pkill", "-f", process_name])
        except Exception as e:
            print(f"Fehler beim Beenden von {process_name}: {e}")

def terminate_processes_by_pid(process_names):
    for process_name in process_names:
        try:
            process_info = subprocess.run(["pgrep", "-o", process_name], capture_output=True, text=True)
            if process_info.returncode == 0:
                pid = int(process_info.stdout.strip())
                os.kill(pid, signal.SIGTERM)
        except Exception as e:
            print(f"Fehler beim Beenden von {process_name}: {e}")

def start_processes(process_names):
    for process_name in process_names:
        try:
            if (process_name != "firefox" or process_name != "chromium"):
                process_name = process_name + "-desktop"
            #process_name = "nohup "+ process_name + " &"
            subprocess.Popen([process_name])
            #subprocess.run([process_name])
        except Exception as e:
            print(f"Fehler beim Starten von {process_name}: {e}")

if __name__ == "__main__":
    try:
        num_rounds = int(input("Gib die Anzahl der Lernrunden ein: "))

        for round_number in range(1, num_rounds + 1):
            os.system('clear')
            focus_countdown_minutes = 25 #Change minutes of one round
            pause_countdown_minutes = 5 #Change minutes of the break
            processes_to_terminate = ["signal", "telegram"] #Change services, you want to stop
            terminate_processes_by_pid(processes_to_terminate)
            terminate_processes(processes_to_terminate)
            os.system('clear')
            start_countdown(focus_countdown_minutes, round_number)
            start_processes(processes_to_terminate)
            os.system('clear')
            start_pause(pause_countdown_minutes, round_number)
        notification = "Lernziel erreicht!"
        subprocess.run(["notify-send", notification])

    except KeyboardInterrupt:
        print("\nProgramm abgebrochen.")

