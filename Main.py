import pyttsx3


engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice


while True:
    find = int(input("type number:"))
    if find < 3:
         print(f"{find}voice name is:",voices[find].name)
    else:
        print('none')