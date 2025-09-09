import gradio as gr
import whisper
from gtts import gTTS
import tempfile

# Load Whisper model
model = whisper.load_model("base")

def speech_to_text(audio):
    if audio is None:
        return "No audio provided"
    
    # Force Malayalam with initial prompt to improve accuracy
    result = model.transcribe(
        audio, 
        language="ml",
        initial_prompt="ഇത് മലയാളം ഭാഷയിലാണ്"  # "This is in Malayalam language"
    )
    return result["text"]

def text_to_speech(text):
    if not text:
        return None
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tts = gTTS(text=text, lang="ml")
        tts.save(tmp_file.name)
        return tmp_file.name

# Create interface
with gr.Blocks(title="Malayalam Speech Processor") as demo:
    gr.Markdown("# Malayalam Speech Processing")
    gr.Markdown("*Optimized for Malayalam language recognition*")
    
    with gr.Tab("Speech to Text"):
        audio_input = gr.Audio(type="filepath", label="Upload Malayalam Audio")
        text_output = gr.Textbox(label="Malayalam Text Output", lines=5)
        stt_btn = gr.Button("Transcribe Malayalam", variant="primary")
        stt_btn.click(speech_to_text, inputs=audio_input, outputs=text_output)
    
    with gr.Tab("Text to Speech"):
        text_input = gr.Textbox(label="Enter Malayalam Text", lines=3)
        audio_output = gr.Audio(label="Generated Malayalam Speech")
        tts_btn = gr.Button("Generate Speech", variant="primary")
        tts_btn.click(text_to_speech, inputs=text_input, outputs=audio_output)

if __name__ == "__main__":
    demo.launch()
