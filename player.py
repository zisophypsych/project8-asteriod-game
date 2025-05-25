from circleshape import *
from constants import *
from main import * 
# from main import shots
from shot import *

class Player(CircleShape):
    def __init__(self, x, y,):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.player_timer = 0

        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen,(255,255,255), self.triangle(),2)
    
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED* dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt*(-1))
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move((-1)*dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        self.player_timer -= dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):

        direction = pygame.Vector2(0,1)
        direction = direction.rotate(self.rotation)

        velocity = direction * PLAYER_SHOOT_SPEED

        if self.player_timer <= 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = velocity
            self.player_timer = PLAYER_SHOOT_COOLDOWN

        
        

        # shots.add(shot) 