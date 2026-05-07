import whisper
import sys
import io
import re
from contextlib import redirect_stdout, redirect_stderr
from tqdm import tqdm

# Load the model
print("Loading Whisper model...")
model = whisper.load_model("medium")

# Get audio file from command line argument
if len(sys.argv) < 2:
    print("Usage: python transcribe.py <audio_file.m4a>")
    sys.exit(1)

audio_file = sys.argv[1]

# Load audio and get duration
print(f"Loading audio: {audio_file}")
audio = whisper.load_audio(audio_file)
audio_duration = len(audio) / whisper.audio.SAMPLE_RATE

print(f"Audio duration: {audio_duration:.1f} seconds")
print("Transcribing...")

# Custom stream that captures output and updates progress bar
class ProgressCapture(io.StringIO):
    def __init__(self, progress_bar, total_duration):
        super().__init__()
        self.progress_bar = progress_bar
        self.total_duration = total_duration
        # Pattern to match timestamp like [00:00.000 --> 00:05.280]
        self.timestamp_pattern = re.compile(r'\[[\d:.]+\s*-->\s*([\d:.]+)\]')

    def write(self, text):
        super().write(text)
        # Look for timestamp pattern in the output
        match = self.timestamp_pattern.search(text)
        if match:
            # Parse end timestamp (format: MM:SS.mmm or HH:MM:SS.mmm)
            time_str = match.group(1)
            parts = time_str.split(':')
            if len(parts) == 2:
                minutes, seconds = parts
                current_time = float(minutes) * 60 + float(seconds)
            elif len(parts) == 3:
                hours, minutes, seconds = parts
                current_time = float(hours) * 3600 + float(minutes) * 60 + float(seconds)
            else:
                return

            # Update progress bar
            progress = min(100, (current_time / self.total_duration) * 100)
            self.progress_bar.n = progress
            self.progress_bar.refresh()

# Create progress bar and run transcription
with tqdm(total=100, desc="Progress", bar_format="{desc}: {percentage:3.0f}%|{bar}| {n:.1f}%") as pbar:
    capture = ProgressCapture(pbar, audio_duration)

    # Redirect stderr (where whisper prints verbose output) and capture it
    with redirect_stderr(capture):
        result = model.transcribe(audio, language="en", verbose=True)

    # Ensure we hit 100%
    pbar.n = 100
    pbar.refresh()

# Print and save
print("\n--- Transcription ---")
print(result["text"])

# Save to file
output_file = audio_file.rsplit('.', 1)[0] + "_transcript.txt"
with open(output_file, "w") as f:
    f.write(result["text"])

print(f"\nSaved to: {output_file}")
