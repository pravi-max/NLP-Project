
# 🎶 Audio to Lyrics Generator

A simple Streamlit app that transcribes uploaded audio files and generates song lyrics using BERT-style language models like BART or T5. Designed to analyze the spoken content and convert it into lyrics based on selected mood or style.

## Features
- Upload audio in MP3, WAV, or M4A format
- Transcribe speech using Whisper
- Choose lyric mood/style: romantic, sad, funny, motivational, etc.
- Generate lyrics in real-time using BART-based model
- Download the generated lyrics

## Run the App
```bash
pip install -r requirements.txt
streamlit run app.py
