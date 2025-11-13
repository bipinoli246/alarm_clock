import time
import datetime
import pygame

# Simple Alarm Clock
def set_alarm(alarm_time):
    print(f"⏰ Alarm set for {alarm_time}")
    sound = r"C:\Users\HP\Desktop\python mini-project\mini projects\alarm_clock\sound.mp3"  # your alarm sound file

    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print(now, end="\r")  # show live time

        if now == alarm_time:
            print("\nWake up! ⏰")
            pygame.mixer.init()
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play()

            # Keep playing sound until stopped manually (Ctrl + C)
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            break

        time.sleep(1)

# Run program
if __name__ == "__main__":
    alarm_time = input("Set alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
