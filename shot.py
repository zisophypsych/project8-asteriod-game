from constants import * 
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(x, y)
        self.radius = SHOT_RADIUS
        self.add(self.containers)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255),(self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)