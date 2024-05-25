"""Encapsulation:

Create abstract classes or interfaces for File and Encrypter.
Implement concrete classes for different file types (e.g., TextFile, ImageFile, AudioFile) that inherit from the File class and encapsulate file-specific details (such as content, extension).
Implement concrete classes for different encryption algorithms (e.g., AESEncrypter, DESEncrypter) that inherit from the Encrypter class and encapsulate encryption logic."""

from abc import ABC, abstractmethod

# Abstract class for File
class File(ABC):
    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, content):
        pass

# Concrete classes for different file types
class TextFile(File):
    def read(self):
        # Read text file specific logic
        print(f"Reading text from {self.filename}")

    def write(self, content):
        # Write text file specific logic
        print(f"Writing text to {self.filename}: {content}")

class ImageFile(File):
    def read(self):
        # Read image file specific logic
        print(f"Reading image from {self.filename}")

    def write(self, content):
        # Write image file specific logic
        print(f"Writing image to {self.filename}")

class AudioFile(File):
    def read(self):
        # Read audio file specific logic
        print(f"Reading audio from {self.filename}")

    def write(self, content):
        # Write audio file specific logic
        print(f"Writing audio to {self.filename}")

# Abstract class for Encrypter
class Encrypter(ABC):
    @abstractmethod
    def encrypt(self, data):
        pass

    @abstractmethod
    def decrypt(self, data):
        pass

# Concrete classes for different encryption algorithms
class AESEncrypter(Encrypter):
    def encrypt(self, data):
        # AES encryption logic
        print("AES encryption applied")

    def decrypt(self, data):
        # AES decryption logic
        print("AES decryption applied")

class DESEncrypter(Encrypter):
    def encrypt(self, data):
        # DES encryption logic
        print("DES encryption applied")

    def decrypt(self, data):
        # DES decryption logic
        print("DES decryption applied")

# Example usage
if __name__ == "__main__":
    text_file = TextFile("my_text.txt")
    text_file.read()
    text_file.write("Hello, world!")

    image_file = ImageFile("my_image.jpg")
    image_file.read()
    image_file.write("Image data...")

    aes_encrypter = AESEncrypter()
    aes_encrypter.encrypt("Sensitive data")
    aes_encrypter.decrypt("Encrypted data")

    des_encrypter = DESEncrypter()
    des_encrypter.encrypt("Confidential info")
    des_encrypter.decrypt("Encrypted info")
