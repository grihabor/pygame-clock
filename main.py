# Example file showing a circle moving on screen
from datetime import datetime
import math
import pygame
from contextlib import contextmanager
from dataclasses import dataclass


@contextmanager
def pygame_init():
    pygame.init()
    try:
        yield
    finally:
        pygame.quit()


@dataclass
class Clock:
    hand_color: str
    center: pygame.Vector2
    size: float

    def draw_second_hand(self, screen, second: int):
        hand = pygame.Vector2(0, -self.size).rotate(second / 60 * 360)
        self._draw_hand(screen, hand)

    def draw_minute_hand(self, screen, minute: int):
        hand = pygame.Vector2(0, -self.size * 3 / 4).rotate(minute / 60 * 360)
        self._draw_hand(screen, hand, width=2)

    def draw_hour_hand(self, screen, hour: int):
        hand = pygame.Vector2(0, -self.size / 2).rotate(hour / 24 * 360)
        self._draw_hand(screen, hand, width=4)

    def _draw_hand(self, screen, hand: pygame.Vector2, width: int = 1):
        pygame.draw.line(
            screen, self.hand_color, self.center, self.center + hand, width=width
        )


def main():
    width, height = (1280, 720)
    screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
    game_clock = pygame.time.Clock()
    running = True
    dt = 0

    clock = Clock(
        center=pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2),
        size=min(screen.get_width() / 3, screen.get_height() / 3),
        hand_color="white",
    )

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        now = datetime.now()
        clock.draw_second_hand(screen, now.second)
        clock.draw_minute_hand(screen, now.minute)
        clock.draw_hour_hand(screen, now.hour)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    with pygame_init():
        main()
