import whisper
import sys

# Load the model
print("Loading Whisper model...")
model = whisper.load_model("medium")

# Get audio file from command line argument
if len(sys.argv) < 2:
    print("Usage: python transcribe.py <audio_file.m4a>")
    sys.exit(1)

audio_file = sys.argv[1]

# Transcribe
print(f"Transcribing {audio_file}...")
result = model.transcribe(audio_file)

# Print and save
print("\n--- Transcription ---")
print(result["text"])

# Save to file
output_file = audio_file.rsplit('.', 1)[0] + "_transcript.txt"
with open(output_file, "w") as f:
    f.write(result["text"])

print(f"\nSaved to: {output_file}")