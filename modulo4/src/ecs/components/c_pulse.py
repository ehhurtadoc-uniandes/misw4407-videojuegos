import pygame


class CPulse:
    def __init__(self, radius: int, pulse_info: dict) -> None:
        self.radius = radius
        self.expand_time = pulse_info["expand_time"]
        self.thickness = pulse_info["thickness"]
        self.color = pygame.Color(pulse_info["color"]["r"],
                                  pulse_info["color"]["g"],
                                  pulse_info["color"]["b"])
        self.elapsed_time = 0.0
