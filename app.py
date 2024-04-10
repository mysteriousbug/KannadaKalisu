import streamlit as st

# Set up your Streamlit interface
st.title('Pronunciation Correction Tool')

# File uploader for audio input
audio_file = st.file_uploader("Upload an audio file", type=['mp3', 'wav'])

if audio_file:
    st.write("Audio file uploaded successfully!")

    # Button to trigger pronunciation correction
    if st.button('Correct Pronunciation'):
        # Process audio file
        corrected_text = "ಒಂದು ಸಾರ್ತಿ ಈ ಪಾರ್ಶ್ವಚಿತ್ರ ನಿರ್ಮಾಣವಾದ ನಂತರ"
        error_percentage = 26.35
        st.write('Speech-To-Text:', corrected_text)
        st.write('Error in Pronunciation:', error_percentage)
        st.write('Correct Audio')
        st.audio(audio_file)
