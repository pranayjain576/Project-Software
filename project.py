import os
import numpy as np
import pygame

audio_directory = "playlist"
pygame.mixer.init()

while True:
    audio_files = [os.path.join(audio_directory, f) for f in os.listdir(audio_directory) if f.endswith(".mp3")]
    np.random.shuffle(audio_files)
    
    for audio_file in audio_files:
        pygame.mixer.music.load(audio_file)
        song_name = os.path.basename(audio_file)
        pygame.mixer.music.play()

        print("playing:", song_name)
        while pygame.mixer.music.get_busy():
            command = input("Enter command (n: next): ")

            if command == "n":
                pygame.mixer.music.stop()
                break

    np.random.shuffle(audio_files)
