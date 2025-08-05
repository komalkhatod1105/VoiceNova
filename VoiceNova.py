import tkinter as tk
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random
import threading
import time
import urllib.parse
import pywhatkit

# Global flag to stop assistant safely
should_exit = False

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  

# Safely log to GUI using tkinter's main thread
def log(message):
    output_box.after(0, lambda: (
        output_box.insert(tk.END, f"\n{message}"),
        output_box.see(tk.END)
    ))

def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        log(f"[Speech Error] {e}")

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning! I hope you have a productive day.")
    elif 12 <= hour < 18:
        speak("Good afternoon! Ready to help you.")
    else:
        speak("Good evening! What can I do for you?")
    speak("Hi, I’m your assistant. Just say what you need.")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        log("Adjusting for background noise...")
        r.adjust_for_ambient_noise(source, duration=1)
        log("Listening...")
        try:
            audio = r.listen(source, timeout=8, phrase_time_limit=6)
            log("Processing your voice...")
            query = r.recognize_google(audio, language='en-in').lower()
            log(f"You said: {query}")
            return query
        except:
            log("I didn’t catch that. Please try again.")
            speak("I didn’t catch that. Please try again.")
            return ""

def open_app(app_name, path=None, web_url=None):
    speak(f"Sure, opening {app_name}.")
    if web_url:
        webbrowser.open(web_url)
    elif path and os.path.exists(path):
        os.startfile(path)
    else:
        speak(f"Sorry, I couldn't find {app_name}.")

def play_youtube_song():
    speak("Tell me the song you want to hear.")
    song_query = take_command()
    if song_query:
        speak(f"Playing {song_query} on YouTube.")
        try:
            pywhatkit.playonyt(song_query)
        except:
            speak("Sorry, I couldn't play the song.")

def exit_assistant():
    global should_exit
    should_exit = True
    speak("Goodbye! Have a great day ahead.")
    log("Assistant stopped.")
    root.after(2000, root.destroy)  # exit after 2 seconds

COMMANDS = {
    'youtube': {
        'phrases': ['open youtube', 'youtube'],
        'action': lambda: open_app("YouTube", web_url="https://youtube.com")
    },
    'spotify': {
        'phrases': ['open spotify', 'spotify'],
        'action': lambda: open_app("Spotify", web_url="https://open.spotify.com")
    },
    'google': {
        'phrases': ['open google', 'google'],
        'action': lambda: open_app("Google", web_url="https://www.google.com")
    },
    'time': {
        'phrases': ['what time', 'current time', 'tell me time'],
        'action': lambda: speak(f"The time is {datetime.datetime.now().strftime('%I:%M %p')}")
    },
    'date': {
        'phrases': ['what date', "today's date", 'tell me date'],
        'action': lambda: speak(f"Today is {datetime.datetime.now().strftime('%A, %B %d, %Y')}")
    },
    'song': {
        'phrases': ['play song', 'play music', 'play something'],
        'action': lambda: play_youtube_song()
    },
    'exit': {
        'phrases': ['exit', 'quit', 'goodbye'],
        'action': lambda: exit_assistant()
    }
}

def run_voice_assistant():
    wish_me()
    while not should_exit:
        query = take_command().strip()
        if not query or should_exit:
            continue

        found = False
        for cmd, data in COMMANDS.items():
            if any(phrase in query for phrase in data['phrases']):
                data['action']()
                found = True
                break

        if not found:
            if 'who are you' in query:
                speak("I’m your smart assistant built with Python.")
            elif 'joke' in query:
                joke = random.choice([
                    "Why did the computer show up at work late? It had a hard drive.",
                    "I would tell you a UDP joke, but you might not get it.",
                    "Why did the developer go broke? Because he used up all his cache."
                ])
                speak(joke)
            elif 'search' in query:
                speak("What should I search for?")
                term = take_command()
                if term:
                    speak(f"Here's what I found for {term}.")
                    webbrowser.open(f"https://www.google.com/search?q={urllib.parse.quote(term)}")
            elif 'fact' in query:
                fact = random.choice([
                    "Did you know? Honey never spoils.",
                    "Octopuses have three hearts.",
                    "Bananas are berries, but strawberries are not.",
                    "The Eiffel Tower can be 15 cm taller during the summer.",
                    "A bolt of lightning contains enough energy to toast 100,000 slices of bread."
                ])
                speak(fact)
            else:
                speak("I’m still learning. Could you try saying that differently?")
        time.sleep(1)

def start_assistant():
    threading.Thread(target=run_voice_assistant, daemon=True).start()

# GUI
root = tk.Tk()
root.title("VoiceNova - AI Voice Assistant")
root.geometry("640x540")
root.configure(bg="#f2f9ff")
root.resizable(False, False)

header = tk.Label(root, text=" AI Voice Assistant ", font=("Segoe UI", 20, "bold"), bg="#d6efff", fg="#003366")
header.pack(fill=tk.X, pady=10)

start_btn = tk.Button(root, text="Start Listening", font=("Helvetica", 12, "bold"), bg="#28a745", fg="white", padx=20, pady=5, command=start_assistant)
start_btn.pack(pady=10)

output_box = tk.Text(root, wrap=tk.WORD, font=("Consolas", 10), bg="#ffffff", height=18, borderwidth=2, relief="groove")
output_box.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

exit_btn = tk.Button(root, text="Exit", font=("Helvetica", 11, "bold"), bg="#dc3545", fg="white", command=exit_assistant)
exit_btn.pack(pady=10)

root.mainloop()
