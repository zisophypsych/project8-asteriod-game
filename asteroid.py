from circleshape import *
from constants import *
import random



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255),(self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return "This was a small asteroid and we're done"
        
        self.kill()
        random_angle = random.uniform(20, 50)
        # pygame.math.Vector2.rotate(self.velocity, random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle)*1.2
        asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, (-1)*random_angle)

        

