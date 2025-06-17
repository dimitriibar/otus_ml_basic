from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, Any, List, Optional


class MediaFile(ABC):
    """
    Абстрактный базовый класс для всех медиафайлов.
    Содержит общие атрибуты и методы для всех типов медиафайлов.
    """

    def __init__(
        self, name: str, size: int, created_at: datetime = None, owner: str = None, metadata: Dict[str, Any] = None
    ):
        self.name = name
        self.size = size
        self.created_at = created_at or datetime.now()
        self.owner = owner
        self.metadata = metadata or {}

    @abstractmethod
    def get_file_type(self) -> str:
        """Возвращает тип медиафайла."""
        pass

    @abstractmethod
    def extract_features(self) -> Dict[str, Any]:
        """Извлекает специфические характеристики медиафайла."""
        pass

    @abstractmethod
    def convert(self, target_format: str) -> "MediaFile":
        """Конвертирует медиафайл в другой формат."""
        pass

    def update_metadata(self, metadata: Dict[str, Any]) -> None:
        """Обновляет метаданные медиафайла."""
        self.metadata.update(metadata)

    def __str__(self) -> str:
        return f"{self.get_file_type()}: {self.name} ({self.size} bytes)"


class AudioFile(MediaFile):
    """Класс для аудиофайлов с аудио-специфичными метаданными и операциями."""

    def __init__(
        self,
        name: str,
        size: int,
        duration: float = None,
        bitrate: int = None,
        sample_rate: int = None,
        channels: int = None,
        **kwargs,
    ):
        super().__init__(name, size, **kwargs)
        # Аудио-специфичные метаданные
        self.metadata.update(
            {"duration": duration, "bitrate": bitrate, "sample_rate": sample_rate, "channels": channels}
        )

    def get_file_type(self) -> str:
        return "Audio"

    def extract_features(self) -> Dict[str, Any]:
        """
        Извлекает аудио-специфичные характеристики, такие как частотный спектр,
        темп, высота тона и т.д.
        """
        # В реальной реализации использовались бы библиотеки обработки аудио
        print(f"Извлечение аудио характеристик из {self.name}")
        return {
            "feature_type": "audio",
            # Дополнительные характеристики извлекались бы здесь
        }

    def convert(self, target_format: str) -> "AudioFile":
        """Конвертирует аудиофайл в другой формат (mp3, wav и т.д.)."""
        print(f"Конвертация {self.name} в {target_format}")
        # В реальной реализации использовались бы библиотеки конвертации аудио
        new_name = f"{self.name.split('.')[0]}.{target_format}"
        return AudioFile(new_name, self.size, **self.metadata)

    def adjust_volume(self, level: float) -> None:
        """Регулирует громкость аудиофайла."""
        print(f"Регулировка громкости {self.name} до уровня {level}")
        # Реализация находилась бы здесь


class VideoFile(MediaFile):
    """Класс для видеофайлов с видео-специфичными метаданными и операциями."""

    def __init__(
        self,
        name: str,
        size: int,
        duration: float = None,
        resolution: str = None,
        frame_rate: float = None,
        codec: str = None,
        **kwargs,
    ):
        super().__init__(name, size, **kwargs)
        # Видео-специфичные метаданные
        self.metadata.update(
            {"duration": duration, "resolution": resolution, "frame_rate": frame_rate, "codec": codec}
        )

    def get_file_type(self) -> str:
        return "Video"

    def extract_features(self) -> Dict[str, Any]:
        """
        Извлекает видео-специфичные характеристики, такие как смена сцен,
        векторы движения и т.д.
        """
        # В реальной реализации использовались бы библиотеки обработки видео
        print(f"Извлечение видео характеристик из {self.name}")
        return {
            "feature_type": "video",
            # Дополнительные характеристики извлекались бы здесь
        }

    def convert(self, target_format: str) -> "VideoFile":
        """Конвертирует видеофайл в другой формат (mp4, avi и т.д.)."""
        print(f"Конвертация {self.name} в {target_format}")
        # В реальной реализации использовались бы библиотеки конвертации видео
        new_name = f"{self.name.split('.')[0]}.{target_format}"
        return VideoFile(new_name, self.size, **self.metadata)

    def extract_frame(self, timestamp: float) -> "PhotoFile":
        """Извлекает кадр из видео в указанной временной метке."""
        print(f"Извлечение кадра в {timestamp} из {self.name}")
        # Реализация находилась бы здесь
        frame_name = f"{self.name.split('.')[0]}_{timestamp}.jpg"
        # Предполагаем небольшой размер извлеченного кадра
        return PhotoFile(frame_name, 100000, width=1920, height=1080)


class PhotoFile(MediaFile):
    """Класс для фотофайлов с фото-специфичными метаданными и операциями."""

    def __init__(
        self,
        name: str,
        size: int,
        width: int = None,
        height: int = None,
        color_space: str = None,
        camera_model: str = None,
        **kwargs,
    ):
        super().__init__(name, size, **kwargs)
        # Фото-специфичные метаданные
        self.metadata.update(
            {"width": width, "height": height, "color_space": color_space, "camera_model": camera_model}
        )

    def get_file_type(self) -> str:
        return "Photo"

    def extract_features(self) -> Dict[str, Any]:
        """
        Извлекает фото-специфичные характеристики, такие как цветовые гистограммы,
        границы, лица и т.д.
        """
        # В реальной реализации использовались бы библиотеки обработки изображений
        print(f"Извлечение характеристик фото из {self.name}")
        return {
            "feature_type": "photo",
            # Дополнительные характеристики извлекались бы здесь
        }

    def convert(self, target_format: str) -> "PhotoFile":
        """Конвертирует фотофайл в другой формат (jpg, png и т.д.)."""
        print(f"Конвертация {self.name} в {target_format}")
        # В реальной реализации использовались бы библиотеки конвертации изображений
        new_name = f"{self.name.split('.')[0]}.{target_format}"
        return PhotoFile(new_name, self.size, **self.metadata)

    def resize(self, width: int, height: int) -> "PhotoFile":
        """Изменяет размер фото до указанных размеров."""
        print(f"Изменение размера {self.name} до {width}x{height}")
        # Реализация находилась бы здесь
        new_name = f"{self.name.split('.')[0]}_resized.{self.name.split('.')[-1]}"
        return PhotoFile(new_name, self.size, width=width, height=height)


class Storage(ABC):
    """
    Абстрактный базовый класс для различных типов хранилищ.
    Определяет интерфейс для операций с хранилищем.
    """

    @abstractmethod
    def save(self, media_file: MediaFile, path: str) -> bool:
        """Сохраняет медиафайл в хранилище."""
        pass

    @abstractmethod
    def load(self, path: str) -> MediaFile:
        """Загружает медиафайл из хранилища."""
        pass

    @abstractmethod
    def delete(self, path: str) -> bool:
        """Удаляет медиафайл из хранилища."""
        pass

    @abstractmethod
    def list_files(self, directory: str) -> List[str]:
        """Список всех файлов в директории."""
        pass


class LocalStorage(Storage):
    """Реализация хранилища для локального диска."""

    def save(self, media_file: MediaFile, path: str) -> bool:
        """Сохраняет медиафайл на локальный диск."""
        print(f"Сохранение {media_file.name} на локальный диск в {path}")
        # Реализация использовала бы операции файлового ввода/вывода
        return True

    def load(self, path: str) -> MediaFile:
        """Загружает медиафайл с локального диска."""
        print(f"Загрузка файла с локального диска из {path}")
        # Реализация определяла бы тип файла и создавала соответствующий объект
        # Упрощенный пример
        if path.endswith((".mp3", ".wav", ".flac")):
            return AudioFile(path.split("/")[-1], 1000000)
        elif path.endswith((".mp4", ".avi", ".mov")):
            return VideoFile(path.split("/")[-1], 5000000)
        elif path.endswith((".jpg", ".png", ".gif")):
            return PhotoFile(path.split("/")[-1], 500000)
        else:
            raise ValueError(f"Неподдерживаемый тип файла: {path}")

    def delete(self, path: str) -> bool:
        """Удаляет медиафайл с локального диска."""
        print(f"Удаление файла с локального диска из {path}")
        # Реализация использовала бы операции файлового ввода/вывода
        return True

    def list_files(self, directory: str) -> List[str]:
        """Список всех файлов в директории на локальном диске."""
        print(f"Список файлов в директории {directory} на локальном диске")
        # Реализация использовала бы os.listdir или подобное
        return ["example1.mp3", "example2.mp4", "example3.jpg"]


class CloudStorage(Storage):
    """Реализация хранилища для облачного хранилища (Google Drive, Dropbox)."""

    def __init__(self, provider: str, credentials: Dict[str, str]):
        self.provider = provider
        self.credentials = credentials

    def save(self, media_file: MediaFile, path: str) -> bool:
        """Сохраняет медиафайл в облачное хранилище."""
        print(f"Сохранение {media_file.name} в облако {self.provider} в {path}")
        # Реализация использовала бы API облачного провайдера
        return True

    def load(self, path: str) -> MediaFile:
        """Загружает медиафайл из облачного хранилища."""
        print(f"Загрузка файла из облака {self.provider} из {path}")
        # Реализация использовала бы API облачного провайдера
        # Упрощенный пример
        if path.endswith((".mp3", ".wav", ".flac")):
            return AudioFile(path.split("/")[-1], 1000000)
        elif path.endswith((".mp4", ".avi", ".mov")):
            return VideoFile(path.split("/")[-1], 5000000)
        elif path.endswith((".jpg", ".png", ".gif")):
            return PhotoFile(path.split("/")[-1], 500000)
        else:
            raise ValueError(f"Неподдерживаемый тип файла: {path}")

    def delete(self, path: str) -> bool:
        """Удаляет медиафайл из облачного хранилища."""
        print(f"Удаление файла из облака {self.provider} из {path}")
        # Реализация использовала бы API облачного провайдера
        return True

    def list_files(self, directory: str) -> List[str]:
        """Список всех файлов в директории облачного хранилища."""
        print(f"Список файлов в директории {directory} в облаке {self.provider}")
        # Реализация использовала бы API облачного провайдера
        return ["cloud_example1.mp3", "cloud_example2.mp4", "cloud_example3.jpg"]


class RemoteStorage(Storage):
    """Реализация хранилища для удаленного сервера (FTP, SFTP)."""

    def __init__(self, host: str, port: int, username: str, password: str):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def save(self, media_file: MediaFile, path: str) -> bool:
        """Сохраняет медиафайл на удаленный сервер."""
        print(f"Сохранение {media_file.name} на удаленный сервер {self.host}:{self.port}/{path}")
        # Реализация использовала бы библиотеки FTP/SFTP
        return True

    def load(self, path: str) -> MediaFile:
        """Загружает медиафайл с удаленного сервера."""
        print(f"Загрузка файла с удаленного сервера {self.host}:{self.port}/{path}")
        # Реализация использовала бы библиотеки FTP/SFTP
        # Упрощенный пример
        if path.endswith((".mp3", ".wav", ".flac")):
            return AudioFile(path.split("/")[-1], 1000000)
        elif path.endswith((".mp4", ".avi", ".mov")):
            return VideoFile(path.split("/")[-1], 5000000)
        elif path.endswith((".jpg", ".png", ".gif")):
            return PhotoFile(path.split("/")[-1], 500000)
        else:
            raise ValueError(f"Неподдерживаемый тип файла: {path}")

    def delete(self, path: str) -> bool:
        """Удаляет медиафайл с удаленного сервера."""
        print(f"Удаление файла с удаленного сервера {self.host}:{self.port}/{path}")
        # Реализация использовала бы библиотеки FTP/SFTP
        return True

    def list_files(self, directory: str) -> List[str]:
        """Список всех файлов в директории на удаленном сервере."""
        print(f"Список файлов в директории {directory} на удаленном сервере {self.host}:{self.port}")
        # Реализация использовала бы библиотеки FTP/SFTP
        return ["remote_example1.mp3", "remote_example2.mp4", "remote_example3.jpg"]


class S3Storage(Storage):
    """Реализация хранилища для S3-подобного объектного хранилища."""

    def __init__(self, bucket: str, region: str, access_key: str, secret_key: str):
        self.bucket = bucket
        self.region = region
        self.access_key = access_key
        self.secret_key = secret_key

    def save(self, media_file: MediaFile, path: str) -> bool:
        """Сохраняет медиафайл в S3-бакет."""
        print(f"Сохранение {media_file.name} в S3-бакет {self.bucket}/{path}")
        # Реализация использовала бы S3 API (boto3 для AWS)
        return True

    def load(self, path: str) -> MediaFile:
        """Загружает медиафайл из S3-бакета."""
        print(f"Загрузка файла из S3-бакета {self.bucket}/{path}")
        # Реализация использовала бы S3 API
        # Упрощенный пример
        if path.endswith((".mp3", ".wav", ".flac")):
            return AudioFile(path.split("/")[-1], 1000000)
        elif path.endswith((".mp4", ".avi", ".mov")):
            return VideoFile(path.split("/")[-1], 5000000)
        elif path.endswith((".jpg", ".png", ".gif")):
            return PhotoFile(path.split("/")[-1], 500000)
        else:
            raise ValueError(f"Неподдерживаемый тип файла: {path}")

    def delete(self, path: str) -> bool:
        """Удаляет медиафайл из S3-бакета."""
        print(f"Удаление файла из S3-бакета {self.bucket}/{path}")
        # Реализация использовала бы S3 API
        return True

    def list_files(self, directory: str) -> List[str]:
        """Список всех файлов в директории S3-бакета."""
        print(f"Список файлов в директории {directory} S3-бакета {self.bucket}")
        # Реализация использовала бы S3 API
        return ["s3_example1.mp3", "s3_example2.mp4", "s3_example3.jpg"]


# Фабрика для создания медиафайлов по расширению файла
class MediaFileFactory:
    """Фабричный класс для создания объектов MediaFile на основе расширения файла."""

    @staticmethod
    def create_from_path(path: str, size: int, **kwargs) -> MediaFile:
        """Создает объект MediaFile на основе расширения файла."""
        filename = path.split("/")[-1]
        if path.endswith((".mp3", ".wav", ".flac")):
            return AudioFile(filename, size, **kwargs)
        elif path.endswith((".mp4", ".avi", ".mov")):
            return VideoFile(filename, size, **kwargs)
        elif path.endswith((".jpg", ".png", ".gif")):
            return PhotoFile(filename, size, **kwargs)
        else:
            raise ValueError(f"Неподдерживаемый тип файла: {path}")


# Пример использования
def main():
    # Создание медиафайлов
    audio = AudioFile("song.mp3", 5000000, duration=240, bitrate=320, sample_rate=44100, channels=2, owner="John")
    video = VideoFile(
        "movie.mp4", 50000000, duration=3600, resolution="1920x1080", frame_rate=30, codec="h264", owner="Alice"
    )
    photo = PhotoFile(
        "image.jpg", 2000000, width=1920, height=1080, color_space="RGB", camera_model="Canon EOS", owner="Bob"
    )

    print("\n--- Созданные медиафайлы ---")
    print(audio)
    print(video)
    print(photo)

    # Обновление метаданных
    audio.update_metadata({"genre": "Rock", "artist": "Unknown"})
    print("\n--- Обновленные метаданные аудио ---")
    print(f"Метаданные аудио: {audio.metadata}")

    # Конвертация файлов
    new_audio = audio.convert("wav")
    new_video = video.convert("avi")
    new_photo = photo.convert("png")

    print("\n--- Конвертированные файлы ---")
    print(new_audio)
    print(new_video)
    print(new_photo)

    # Извлечение характеристик
    audio_features = audio.extract_features()
    video_features = video.extract_features()
    photo_features = photo.extract_features()

    # Специфичные операции
    audio.adjust_volume(0.8)
    frame = video.extract_frame(120.5)
    resized_photo = photo.resize(800, 600)

    print("\n--- Специфичные операции ---")
    print(f"Извлеченный кадр: {frame}")
    print(f"Измененное фото: {resized_photo}")

    # Примеры хранилищ
    local_storage = LocalStorage()
    cloud_storage = CloudStorage("Dropbox", {"api_key": "your_api_key"})
    remote_storage = RemoteStorage("example.com", 22, "user", "password")
    s3_storage = S3Storage("media-bucket", "us-west-2", "access_key", "secret_key")

    print("\n--- Операции с хранилищами ---")
    # Сохранение файлов в разные хранилища
    local_storage.save(audio, "/music/song.mp3")
    cloud_storage.save(video, "/videos/movie.mp4")
    remote_storage.save(photo, "/photos/image.jpg")
    s3_storage.save(audio, "audio/song.mp3")

    # Загрузка файлов из разных хранилищ
    loaded_audio = local_storage.load("/music/another_song.mp3")
    loaded_video = cloud_storage.load("/videos/another_movie.mp4")
    loaded_photo = s3_storage.load("photos/another_image.jpg")

    print("\n--- Загруженные файлы ---")
    print(loaded_audio)
    print(loaded_video)
    print(loaded_photo)

    # Удаление файлов
    local_storage.delete("/music/old_song.mp3")

    # Список файлов
    local_files = local_storage.list_files("/music")
    cloud_files = cloud_storage.list_files("/videos")

    print("\n--- Список файлов ---")
    print(f"Локальные файлы: {local_files}")
    print(f"Облачные файлы: {cloud_files}")

    # Использование фабрики для создания медиафайлов
    print("\n--- Файлы, созданные фабрикой ---")
    factory_audio = MediaFileFactory.create_from_path("music/new_song.mp3", 3000000)
    factory_video = MediaFileFactory.create_from_path("videos/new_movie.mp4", 40000000)
    factory_photo = MediaFileFactory.create_from_path("photos/new_image.jpg", 1500000)

    print(factory_audio)
    print(factory_video)
    print(factory_photo)


if __name__ == "__main__":
    main()