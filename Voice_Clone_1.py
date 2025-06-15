# ── Cell 1: install Coqui TTS ──
!pip install TTS


# ── Cell 2: import & choose device ──
import torch
from TTS.api import TTS

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")


# ── Cell 3: load a multi-speaker “YourTTS” model (zero-shot capable) ──
# This model lets you clone any voice from a few seconds of audio. :contentReference[oaicite:0]{index=0}
tts = TTS(
    model_name="tts_models/multilingual/multi-dataset/your_tts",
    progress_bar=False
).to(device)




# Option B: Mount your Google Drive (if you’ve saved sample_8sec.wav there)
from google.colab import drive
drive.mount('/content/drive')                # follow on-screen auth
audio_path1 = "/content/drive/MyDrive/audiosample1.wav"
audio_path2 = "/content/drive/MyDrive/sample2.wav"
audio_path3 = "/content/drive/MyDrive/sample3.wav"
audio_path4 = "/content/drive/MyDrive/sample4.wav"
audio_path5 = "/content/drive/MyDrive/sample5.wav"


print("Using audio file at:", audio_path1,'\n',audio_path2,'\n',audio_path3,'\n',audio_path4,'\n',audio_path5,'\n',)


# ── Cell 5: synthesize new speech in that voice ──
text = "Hello, this is a cloned voice test!"
output_path = "cloned_output.wav"

tts.tts_to_file(
    text=text,
    speaker_wav=[audio_path1,audio_path2,audio_path3,audio_path4,audio_path5],   # <-- use the variable you defined in Cell 4
    language="en",
    file_path=output_path
)

print("✅ Generated:", output_path)

# (Optional) play it back inline
from IPython.display import Audio, display
display(Audio(output_path))


# ── Cell 5: synthesize any user-defined text ──

# Prompt you for new text (or just hard-code your string here)
new_text = input("What should I say? ")

output_path = "cloned_custom.wav"

tts.tts_to_file(
    text=new_text,
    speaker_wav=[audio_path1,audio_path2,audio_path3,audio_path4,audio_path5]ss,
    language="en",
    file_path=output_path
)

print("✅ Generated:", output_path)

# Play it back inline
from IPython.display import Audio, display
display(Audio(output_path))


