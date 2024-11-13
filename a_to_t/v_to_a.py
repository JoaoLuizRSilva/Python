from moviepy.editor import VideoFileClip

# Carregar o vídeo
video = VideoFileClip("./seu_video.mp4")

# Extrair o áudio
audio = video.audio

# Salvar o áudio em um arquivo WAV
audio.write_audiofile("audio_extraido.wav")