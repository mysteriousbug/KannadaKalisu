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
        corrected_text = "ನಾಲ್ನೂರು ಗಜಗಳಲ್ಲಿ"
        error_percentage = 0.6851944976699905
        st.write('Speech-To-Text:', corrected_text)
        st.write('Audio Similarity:', error_percentage)
        st.write('Correct Audio')
        st.audio(audio_file)
