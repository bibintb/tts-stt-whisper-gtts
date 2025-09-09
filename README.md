# Malayalam Speech Processing App

A web-based application for Malayalam speech-to-text and text-to-speech conversion using OpenAI Whisper and Google Text-to-Speech.

## Features

- **Speech-to-Text**: Convert Malayalam audio to text with improved accuracy
- **Text-to-Speech**: Convert Malayalam text to audio using gTTS
- **Web Interface**: Easy-to-use Gradio interface
- **Offline Processing**: Whisper runs locally for privacy
- **Language Optimization**: Specifically tuned for Malayalam recognition

## Files

- `app.py` - Basic Malayalam speech processing app
- `malayalam_app.py` - Enhanced version with improved Malayalam detection
- `requirements.txt` - Python dependencies
- `run.bat` - Windows setup script

## Quick Start

### Option 1: Enhanced Malayalam App (Recommended)
```bash
source venv/bin/activate
python malayalam_app.py
```

### Option 2: Basic App
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
1. Upload or record Malayalam audio file
2. Click "Transcribe Malayalam" 
3. Get Malayalam text output

### Text-to-Speech Tab
1. Enter Malayalam text
2. Click "Generate Speech"
3. Download generated audio

## Technical Details

### Models Used
- **Whisper**: OpenAI's base model for speech recognition
- **gTTS**: Google Text-to-Speech for Malayalam synthesis

### Language Support
- **Input**: Malayalam audio (mp3, wav, m4a, etc.)
- **Output**: Malayalam text and audio
- **Optimization**: Initial prompt prevents Tamil misdetection

### Performance
- **Model Size**: ~140MB (Whisper base)
- **Processing**: Local CPU/GPU processing
- **Quality**: Good for most Malayalam dialects

## Improvements in malayalam_app.py

- **Better Recognition**: Uses Malayalam initial prompt "ഇത് മലയാളം ഭാഷയിലാണ്"
- **Forced Language**: Explicitly sets Malayalam language code
- **Enhanced UI**: Malayalam-specific labels and descriptions

## Dependencies

```
openai-whisper  # Speech recognition
gradio         # Web interface
gTTS           # Text-to-speech
```

## Troubleshooting

### Common Issues

**Getting Tamil instead of Malayalam:**
- Use `malayalam_app.py` instead of `app.py`
- Ensure clear Malayalam pronunciation in audio

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
- **Single Voice**: Only one female Malayalam voice available
- **Processing Time**: Larger audio files take longer to process
- **Audio Quality**: Input audio quality affects transcription accuracy

## License

Open source - uses OpenAI Whisper (MIT) and Google TTS services.