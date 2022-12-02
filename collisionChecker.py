from gameplatform import GamePlatform
from doodler import Doodler


class CollisionChecker:
    @staticmethod
    def check_collision(platform: GamePlatform, doodler: Doodler):
        borders = platform.get_borders()
        # (x1, y1, x2, y2)
        doodler_collider = doodler.canvas.coords(doodler.rect_collider,)

        if borders[2] < doodler_collider[1] < borders[3] and (
                borders[0] < doodler_collider[0] < borders[1] or borders[0] < doodler_collider[2] < borders[1]):
            return True
        else:
            return False
