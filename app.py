import streamlit as st
from runner import converted_text
# Set up your Streamlit interface
st.title('Pronunciation Correction Tool')
corrected_text = converted_text
error_percentage = 0.6851944976699905
st.write('Speech-To-Text:', corrected_text)
st.write('Audio Similarity:', error_percentage)
st.write('Correct Audio')
st.audio(audio_file)
