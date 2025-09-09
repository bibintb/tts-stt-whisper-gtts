# TTS-STT with Whisper & gTTS

A web-based application for speech-to-text and text-to-speech conversion using OpenAI Whisper and Google Text-to-Speech, optimized for Malayalam language processing.

## Features

- **Speech-to-Text (STT)**: Convert audio to text using OpenAI Whisper
- **Text-to-Speech (TTS)**: Convert text to audio using Google gTTS
- **Web Interface**: Easy-to-use Gradio interface
- **Offline STT**: Whisper runs locally for privacy
- **Malayalam Optimization**: Specifically tuned for Malayalam recognition

## Models Used

- **OpenAI Whisper (Base)**: Speech recognition model (~140MB)
- **Google Text-to-Speech (gTTS)**: Neural TTS with Malayalam support

## Files

- `app.py` - Basic speech processing app
- `malayalam_app.py` - Enhanced version with improved Malayalam detection
- `requirements.txt` - Python dependencies
- `run.bat` / `run.sh` - Setup scripts

## Quick Start

### Enhanced App (Recommended)
```bash
source venv/bin/activate
python malayalam_app.py
```

### Basic App
```bash
source venv/bin/activate
python app.py
```

Open your browser and go to: `http://127.0.0.1:7860`

## Installation

### Prerequisites
- Python 3.8+
- FFmpeg (for audio processing)

### Setup
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install FFmpeg (Ubuntu/Debian)
sudo apt install ffmpeg
```

## Usage

### Speech-to-Text Tab
1. Upload or record audio file
2. Click "Transcribe" 
3. Get text output

### Text-to-Speech Tab
1. Enter text
2. Click "Generate Speech"
3. Download generated audio

## Technical Details

### Performance
- **Model Size**: ~140MB (Whisper base)
- **Processing**: Local CPU/GPU processing
- **Quality**: Good for most dialects

### Language Support
- **Input**: Audio files (mp3, wav, m4a, etc.)
- **Output**: Text and audio
- **Optimization**: Initial prompt prevents language misdetection

## Improvements in malayalam_app.py

- **Better Recognition**: Uses language-specific initial prompt
- **Forced Language**: Explicitly sets language code
- **Enhanced UI**: Language-specific labels and descriptions

## Dependencies

```
openai-whisper  # Speech recognition
gradio         # Web interface
gTTS           # Text-to-speech
```

## Troubleshooting

### Common Issues

**Language misdetection:**
- Use `malayalam_app.py` instead of `app.py`
- Ensure clear pronunciation in audio

**FFmpeg not found:**
```bash
sudo apt install ffmpeg  # Linux
brew install ffmpeg      # macOS
```

**Virtual environment issues:**
```bash
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

## Limitations

- **Internet Required**: gTTS needs internet for speech synthesis
- **Single Voice**: Only one voice available per language
- **Processing Time**: Larger audio files take longer to process
- **Audio Quality**: Input audio quality affects transcription accuracy

## License

Open source - uses OpenAI Whisper (MIT) and Google TTS services.