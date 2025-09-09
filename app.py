import gradio as gr
import whisper
from gtts import gTTS
import tempfile
import os

# Load Whisper model
model = whisper.load_model("base")

def speech_to_text(audio):
    if audio is None:
        return "No audio provided"
    result = model.transcribe(audio, language="ml")
    return result["text"]

def text_to_speech(text):
    if not text:
        return None
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tts = gTTS(text=text, lang="ml")
        tts.save(tmp_file.name)
        return tmp_file.name

# Create Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Malayalam Speech Processing App")
    
    with gr.Tab("Speech to Text"):
        audio_input = gr.Audio(type="filepath")
        text_output = gr.Textbox(label="Transcribed Text")
        stt_btn = gr.Button("Transcribe")
        stt_btn.click(speech_to_text, inputs=audio_input, outputs=text_output)
    
    with gr.Tab("Text to Speech"):
        text_input = gr.Textbox(label="Enter Text")
        audio_output = gr.Audio(label="Generated Speech")
        tts_btn = gr.Button("Generate Speech")
        tts_btn.click(text_to_speech, inputs=text_input, outputs=audio_output)

if __name__ == "__main__":
    demo.launch()