# VoiceNova 🎙️ - Your AI Voice Assistant 

VoiceNova is an AI-based voice assistant built with Python and a beautiful Tkinter GUI. It can listen to your voice, respond via text-to-speech, and perform tasks like opening apps, playing songs, telling the time/date, cracking jokes, and more — just like Alexa!

---

## 🧠 Features

- 🎤 Voice Command Recognition (using microphone)
- 🔊 Text-to-Speech with natural female voice
- 🌐 Opens websites like YouTube, Google, Spotify
- 🎶 Plays songs on YouTube via voice
- ⏰ Tells current time and date
- 😂 Tells programming jokes and fun facts
- 🧠 Learns and handles unknown commands gracefully
- 🪟 GUI interface built using Tkinter
- 🧵 Background threading (non-blocking voice listening)
- 🛑 Exit via command or GUI button

---

## 📦 Dependencies

Make sure you have these installed:

```bash
pip install pyttsx3
pip install SpeechRecognition
pip install pywhatkit
pip install pyaudio

📁 Project Structure
VoiceNova/
│
├── VoiceNova.py         # Main GUI + Assistant logic
├── README.md            # You're reading it!


🛠️ How to Run
python VoiceNova.py
Make sure your microphone is working and Python 3.8+ is installed.


🤖 Voice Commands Supported
| Command Type | Examples                                      |
| ------------ | --------------------------------------------- |
| Open App     | "Open YouTube", "Open Google", "Open Spotify" |
| Play Song    | "Play song", "Play something"                 |
| Time/Date    | "What time", "Tell me date"                   |
| Fun          | "Tell me a joke", "Give me a fact"            |
| Info         | "Who are you?"                                |
| Search       | "Search something"                            |
| Exit         | "Exit", "Quit", "Goodbye"                     |
"

