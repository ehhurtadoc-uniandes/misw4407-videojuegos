import pygame

class SoundsService:
    def __init__(self) -> None:
        self._sounds = {}

    
    def play(self, path: str):
        if path not in self._sounds:
            self._sounds[path] = pygame.mixer.Sound(path)
        self._sounds[path].play()

    def play_loop(self, path: str) -> None:
        if path not in self._sounds:
            self._sounds[path] = pygame.mixer.Sound(path)
        self._sounds[path].play(loops=-1)

    def stop(self, path: str) -> None:
        if path in self._sounds:
            self._sounds[path].stop()

    def pause_all(self) -> None:
        pygame.mixer.pause()

    def resume_all(self) -> None:
        pygame.mixer.unpause()