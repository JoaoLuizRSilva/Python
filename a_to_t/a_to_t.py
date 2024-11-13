import whisper

# Carregar o modelo Whisper (o modelo "base" é uma boa escolha para começar)
model = whisper.load_model("base")

# Caminho do arquivo de áudio
audio_file = "audio_extraido.wav"

# Transcrever o áudio
result = model.transcribe(audio_file, language="pt")

# Exibir o texto transcrito
print("Texto transcrito:", result['text'])