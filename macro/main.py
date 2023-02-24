import pyautogui
import time

print("Paste commands - Double tap Enter to save.")

commandInputs = []

while True:
    line = input("")
    if line == "":
        break
    commandInputs.append(line)

print("Pasting commands in 5 seconds - open Minecraft chat.")

time.sleep(5)

for command in commandInputs:
    pyautogui.write(command)
    pyautogui.press("enter")
    pyautogui.write("t")
    time.sleep(0.5)