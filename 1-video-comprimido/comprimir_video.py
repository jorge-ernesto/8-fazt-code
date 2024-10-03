from moviepy.editor import VideoFileClip

def comprimir_video(input_video, output_video, bitrate="500k"):
    # Cargar el video
    clip = VideoFileClip(input_video)
    
    # Especificar parámetros de salida, incluyendo el bitrate para reducir el tamaño
    clip.write_videofile(output_video, bitrate=bitrate, codec='libx264', audio_codec='aac')

# Ruta del video de entrada y salida
input_video = "Videos/2024-08-24 19-33-21.mkv"
output_video = "Videos/video_comprimido.mp4"

# Llamar a la función para comprimir el video
comprimir_video(input_video, output_video)
