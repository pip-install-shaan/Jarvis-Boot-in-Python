import speech_recognition as sr
import webbrowser
import pyttsx3 
import os
import subprocess
import pyautogui
import music_library




recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    command=command.strip()
    print('Your command; ', command)

    if 'open google' in command.lower():
        webbrowser.open("https.//www.google.com")
    elif c.lower().startswith('play'):
         song=c.lower().split(" ")[1]
         link=music_library.music[song]
         webbrowser.open(link)
    elif "close this tab" in command:
        pyautogui.hotkey("ctrl", "w")
    elif "open recycle bin" in command:
        subprocess.Popen("explorer.exe shell:RecycleBinFolder", shell=True)
    elif "open cmd" in command or "open command prompt" in command:
        subprocess.Popen("cmd.exe", shell=True)
    elif 'open my pc' in command or 'open this pc' in command:
         subprocess.Popen("explorer.exe shell:Downloads", shell=True)
    elif 'open youtube' in command.lower():
            webbrowser.open("https.//www.youtube.com")
    elif 'open tiktok' in command.lower():
            webbrowser.open("https.//www.tiktok.com")
    elif 'open umt student portal' in command.lower():
            webbrowser.open("https://online.umt.edu.pk/Account/Login?ReturnUrl=%2FCourseRequest")
    else:
         print('Sorry Boss, I don\'t know this command yet.')



   
if __name__=="__main__":
    speak('Initializing Jarivs...') 
    while True:
        r=sr.Recognizer()
        print('recognizing...')

        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                print("Listening...")
                audio=r.listen(source, timeout=5, phrase_time_limit=3)
            word=r.recognize_google(audio)
            print('You said: ', word)

            if(word.lower()=='jarvis'):
                speak("Yes Boss")
                with sr.Microphone() as source:
                    print("Jarvis active....")
                    audio=r.listen(source, timeout=5, phrase_time_limit=5)
                    command=r.recognize_google(audio)


                    processCommand(command)
        
        except sr.UnknownValueError:
            print("Sorry bro, I couldn't understand your voice. Try again.")

        except sr.WaitTimeoutError:
            print("No voice detected. Please speak again.")

        except sr.RequestError as e:
            print(f"Google speech recognition service error: {e}")

