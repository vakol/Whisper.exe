import sys
import whisper
from datetime import datetime

# Ensure a file path was provided
if len(sys.argv) < 2:
    print("\n[@FAIL]")
    print("Please provide a MP3 file path as a command-line argument.")
    print("[/@FAIL]")
    sys.exit(1)

# Get input MP3 file
print("\n[@INPUT_MP3]")
mp3_file_path = sys.argv[1]
print(mp3_file_path)
print("[/@INPUT_MP3]")

# Load Whisper
print("\n[@LOADING]")
model = whisper.load_model("turbo")
print("[/@LOADING]")

# Start time
begin_time = datetime.now().time()
print("\n[@BEGIN_TIME]")
print(begin_time)
print("[/@BEGIN_TIME]")

# Make transcription
print("\n[@TRANSCRIBE]")
result = model.transcribe(mp3_file_path)
print("[@TRANSCRIBE]")

# Write output to console
print("\n[@TEXT]")
print(result["text"])
print("[/@TEXT]")

# End time
end_time = datetime.now().time()
print("\n[@END_TIME]")
print(end_time)
print("[/@END_TIME]")

print("\n[@SUCCESS]")