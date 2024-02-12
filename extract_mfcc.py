import librosa
import numpy as np

def extract_mfcc_from_local_file(audio_file_path, num_mfcc=13, n_fft=2048, hop_length=512):
    """
    Extract MFCC features from a local audio file.

    Parameters:
    - audio_file_path: Path to the local audio file (e.g., 'path/to/your/audio/file.wav').
    - num_mfcc: Number of MFCC coefficients to extract.
    - n_fft: Number of samples per Fourier Transform.
    - hop_length: Number of samples between successive frames.

    Returns:
    - mfcc_features: 2D array of MFCC coefficients.
    """
    try:
        # Load audio file
        y, sr = librosa.load(audio_file_path, sr=None)

        # Extract MFCC features
        mfcc_features = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=num_mfcc, n_fft=n_fft, hop_length=hop_length)

        return mfcc_features

    except Exception as e:
        print(f"Error processing audio file: {e}")
        return None

# Example usage
local_audio_file_path = 'path_to_your_local_audio_file.wav'
mfcc_features = extract_mfcc_from_local_file(local_audio_file_path)

if mfcc_features is not None:
    print(f"Shape of MFCC features: {mfcc_features.shape}")
    print("MFCC features:")
    print(mfcc_features)
