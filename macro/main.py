print("Paste commands - Double tap Enter to save.")

commandInputs = []

while True:
    line = input("")
    if line == "":
        break
    commandInputs.append(line)
print(commandInputs)

for command in commandInputs:
    print(command)