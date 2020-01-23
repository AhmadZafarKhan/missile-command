
import spgl


class City(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)

class Silo(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)

class PlayerMissile(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)

class EnemyMissile(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)


city = 