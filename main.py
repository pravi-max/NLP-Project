import streamlit as st
from utils.audio_analysis import analyze_audio
from utils.lyric_generator import generate_lyrics
from utils.file_utils import save_uploaded_file

# Page settings
st.set_page_config(page_title="Lyricify 🎶", page_icon="🎵", layout="wide")

st.title("🎵 Lyricify: Turn Your Audio Into Lyrics!")

uploaded_file = st.file_uploader("📁 Upload an audio or video file", type=["mp3", "wav", "mp4", "m4a"])

if uploaded_file is not None:
    file_path = save_uploaded_file(uploaded_file)
    mood, tempo = analyze_audio(file_path)
    lyrics = generate_lyrics(mood, tempo)

    # Create two columns
    col1, col2 = st.columns(2)

    # Left Column - Audio Analysis
    with col1:
        st.header("🎼 Audio Analysis")
        st.success(f"**Mood Detected:** {mood} 🎶")
        st.info(f"**Tempo:** {tempo} BPM 🥁")

    # Right Column - Generated Lyrics
    with col2:
        st.header("🤖 Generated Lyrics")
        
        # Display lyrics as chat bubbles
        for line in lyrics.split("\n"):
            if line.strip() != "":
                with st.chat_message("assistant"):
                    st.markdown(f"🎤 {line}")

# Footer or background could be added later for even more polish
else:
    st.info("👆 Please upload a file to get started!")

