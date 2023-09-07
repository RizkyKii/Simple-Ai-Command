import pyttsx3
import speech_recognition as sr
import datetime
import os
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import cv2
import sys
import time
from gtts import gTTS

engine = pyttsx3.init()
# print(voices[1].id)

def speak(audio):
    print(audio)
    engine.runAndWait()
    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        audio = r.listen(source, timeout=5, phrase_time_limit=8)
        
    try:
        print('Recongnizing...')
        query = r.recognize_google(audio, language='id-ID')
        print(f'user said: {query}')
        if 'alexa' in query:
            query = query.replace('alexa', '')
            print(query)
        
    except Exception as e:
        speak('Mohon katakan sekali lagi')
        return 'none'
    return query
     
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime('%I:%M:%p')
    
    if hour>=0 and hour<=12:
        speak(f'Selamat Pagi Tuan, sekarang pukul {tt}')
    elif hour>=12 and hour<=17:
        speak(f'Selamat Siang Tuan, sekarang pukul {tt}')
    else:
        speak(f'Selamat Malam Tuan, sekarang pukul {tt}')
    speak('Saya Alexa, akan membantu anda')


if __name__ == "__main__":
    wish()
    while True:
    # if 1:
        
        query = takecommand().lower()
        
        if 'buka notepad' in query:
            speak('Ok tuan, membuka notepad')
            npath = 'C:\\WINDOWS\\system32\\notepad.exe'
            os.startfile(npath)
        
        elif 'tutup notepad' in query:
            speak('okay tuan, menutup notepad')
            os.system('taskill /f /im notepad.exe')
        
        elif 'shut down the computer' in query:
            speak('okay tuan, shutting down computer. Semoga hari anda menyenangkan')
            os.system('shutdown /s /t 5')
        
        elif 'restart the computer' in query:
            speak('okay tuan, restarting computer')
            os.system('shutdown /r /t 5')
        
        elif 'sleep the computer' in query:
            speak('okay tuan, sleeping computerr')
            os.system('rundll32.exe powrproft.dll,SetSuspendState 0,1,0')
            
        elif 'buka command prompt' in query:
            speak('Ok tuan, membuka command prompt')
            os.system('start cmd')
        
        elif 'buka camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitkey(50)
                if k==27:
                    break;
                cap.release()
                cv2.destroyAllWindows()
            
        elif 'wikipedia' in query:
            speak('mencari di wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, 1)
            speak('menurut wikipedia')
            speak(results)
            # print(results)
        
        elif 'buka youtube' in query:
            speak('Ok tuan, membuka youtube')
            webbrowser.open('www.youtube.com')
            
        elif 'buka facebook' in query:
            speak('Ok tuan, membuka facebook')
            webbrowser.open('www.facebook.com')
            
        elif 'buka github' in query:
            speak('Ok tuan, membuka github')
            webbrowser.open('www.github.com')
            
        elif 'buka google' in query:
            speak('tuan, sebutkan nama yang akan dicari')
            cm = takecommand().lower()
            speak('Ok tuan')
            webbrowser.open(f'{cm}')
            
        elif 'kirim pesan ke whatsapp' in query:
            speak('Ok tuan, mengirim pesan ke whatsapp')
            kit.sendwhatmsg_instantly('+6282277288585', 'Hello, this jarvis')
            speak('Pesan telah dikirim')
        
        elif 'putar lagu di youtube' in query:
            speak('tuan, sebutkan namanya')
            song = takecommand().lower()
            speak('Ok tuan, memainkan lagu ' + song)
            kit.playonyt(song)
        
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f'IP address anda adalah {ip}')
        
        elif 'istirahat' in query:
            speak('Senang membantu anda')
            sys.exit()



            