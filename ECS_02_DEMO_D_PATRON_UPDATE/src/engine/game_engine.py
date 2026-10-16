import pygame

from src.create.prefab_creator import create_square

# EC Object manager imports
from src.ec.GameObjectManager import GameObjectManager


class GameEngine:
    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption("DEMO - PATRÓN UPDATE (ECS 'IMPURO')")
        self._screen: pygame.Surface = pygame.display.set_mode((640, 360), pygame.SCALED)
        self._screen_rect: pygame.FRect = self._screen.get_frect()

        self._clock: pygame.Clock = pygame.time.Clock()
        self._framerate: int = 60
        self._delta_time: float = 0

        self._bg_color: pygame.Color = pygame.Color(0, 200, 128)

        # EC ObjectManager
        self._game_object_manager: GameObjectManager = GameObjectManager()

        self._is_running: bool = True

    def run(self) -> None:
        self._create()
        while self._is_running:
            self._process_events()
            self._calculate_time()
            self._update()
            self._draw()
        self._shutdown()

    def _create(self):
        # Create via EC Object Manager
        create_square(
            game_object_manager=self._game_object_manager,
            size=pygame.Vector2(50, 50),
            pos=pygame.Vector2(100, 100),
            vel=pygame.Vector2(100, 100),
            col=pygame.Color(255, 255, 100),
            screen=self._screen,
            screen_rect=self._screen_rect,
        )

    def _process_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._is_running = False

    def _calculate_time(self) -> None:
        self._clock.tick(self._framerate)
        self._delta_time = self._clock.get_time() / 1000.0

    def _update(self) -> None:
        # Pre loop for EC Object manager (ECS could have systems here as well)
        self._game_object_manager.pre_loop()

        # Update via EC Object Manager
        self._game_object_manager.update(self._delta_time)

    def _draw(self) -> None:
        # Rendering start
        self._screen.fill(self._bg_color)

        # Render via EC Object Manager
        self._game_object_manager.draw()
        self._game_object_manager.post_draw()

        pygame.display.flip()

        # Post loop for EC Object manager (ECS could have systems here as well)
        self._game_object_manager.post_loop()

    def _shutdown(self) -> None:
        # Shut down via EC Object Manager
        self._game_object_manager.clear_all()
        pygame.quit()
