import speech_recognition as sr
import webbrowser
import pyttsx3
import sounddevice as sd
import numpy as np
import requests
import re

# import musicLibrary
# import pywhatkit as kit


recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def record_audio(duration=2, fs=16000):
    print("Listening...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    return sr.AudioData(audio.tobytes(), fs, 2)


# def play_song(song):
#     query = song.replace(" ", "+")
#     url = f"https://www.youtube.com/results?search_query={query}"

#     html = requests.get(url).text
#     video_ids = re.findall(r"watch\?v=(\S{11})", html)

#     if video_ids:
#         webbrowser.open(f"https://www.youtube.com/watch?v={video_ids[0]}")
#     else:
#         speak("Sorry, I couldn't find the song")

def processCommand(command):
    if "open google" in command.lower():
        webbrowser.open("http://google.com")
    elif "open facebook" in command.lower():
        webbrowser.open("http://facebook.com")
    elif "open youtube" in command.lower():
        webbrowser.open("http://youtube.com")
    elif "open linkedin" in command.lower():
        webbrowser.open("http://linkedin.com")




    #1st prefference
    elif command.startswith("play"):
        song = command.replace("play", "")
        url = f"https://www.youtube.com/results?search_query={song}"
        webbrowser.open(url)

    #2nd prefference
    # elif command.lower().startswith("play"):
    #     song = command.lower().replace("play ", "")
    #     link = musicLibrary.music.get(song)

        # if link:
        #     webbrowser.open(link)
        # else:
        #     speak("Song not found")
    else:
        speak("Command not recognized")
    

       
if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        try:
            print("Waiting for wake word...")
            audio = record_audio(duration=2)
            word = recognizer.recognize_google(audio)
            print("Heard:", word)

            if "jarvis" in word.lower():
                speak("Yes, how can I help you?")
                print("Jarvis active...")

                audio = record_audio(duration=3)
                command = recognizer.recognize_google(audio)
                print("Command:", command)
                processCommand(command)

        # except Exception as e:
        #     print("Error:", e)
        
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("API error:", e)
        except KeyboardInterrupt:
            print("Program stopped by user")
            break
        except Exception as e:
            print("Other error:", e)
