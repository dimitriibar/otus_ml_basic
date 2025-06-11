from main import AudioFile, VideoFile, PhotoFile, LocalStorage, CloudStorage, S3Storage

# Создание медиафайлов
audio = AudioFile("song.mp3", 5000000, duration=240, bitrate=320, 
                 sample_rate=44100, channels=2, owner="John")
video = VideoFile("movie.mp4", 50000000, duration=3600, resolution="1920x1080", 
                 frame_rate=30, codec="h264", owner="Alice")
photo = PhotoFile("image.jpg", 2000000, width=1920, height=1080, 
                 color_space="RGB", camera_model="Canon EOS", owner="Bob")

# Вывод информации о медиафайлах
print("Созданные медиафайлы:")
print(audio)
print(video)
print(photo)

# Вывод метаданных аудиофайла
print("\nМетаданные аудиофайла:")
print(audio.metadata)

# Создание экземпляров хранилищ
local_storage = LocalStorage()
cloud_storage = CloudStorage("Dropbox", {"api_key": "your_api_key"})
s3_storage = S3Storage("media-bucket", "us-west-2", "access_key", "secret_key")

# Вывод информации о хранилищах
print("\nЭкземпляры хранилищ:")
print(f"Локальное хранилище: {local_storage.__class__.__name__}")
print(f"Облачное хранилище: {cloud_storage.__class__.__name__}, Поставщик: {cloud_storage.provider}")
print(f"S3 хранилище: {s3_storage.__class__.__name__}, Бакет: {s3_storage.bucket}")