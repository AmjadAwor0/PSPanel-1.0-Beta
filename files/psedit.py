import os

print("<<<TYPE CT+C TO SAVE>>>")
file = ""
Text = []
num = 0
while True:
    num += 1
    inp = input(str(num) + " ")
    if inp == "CT+C":
        break
    else:
        if inp:
            Text.append(inp)
FiText = '\n'.join(Text)
FileName = input("File name: ")
FileLocation1 = input("File Location(without '/'): ")
FileLocation = FileLocation1+"/"
os.system('echo ' + FiText + ' > '+FileLocation+FileName)
print("\n")
print("File saved, Press any key to exit")
os.system("pause>nul")