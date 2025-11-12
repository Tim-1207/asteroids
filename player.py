# player.py
import pygame
from circleshape import CircleShape  # <- Player braucht CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS  # <- Player braucht diese Konstante
from shot import Shot

class Player(CircleShape):  # <- Player IST EINE Art von CircleShape
    def __init__(self, x, y):  # <- Wenn jemand einen Player erstellt, gibt er nur x und y an
        super().__init__(x, y, PLAYER_RADIUS)  # <- Aber intern rufst DU CircleShape mit x, y UND dem festen Radius auf
        self.rotation = 0
        self.shot_cooldown_timer = 0
    
# in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]    

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.shot_cooldown_timer = max(0, self.shot_cooldown_timer - dt)
            
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)        
        forward = unit_vector.rotate(self.rotation) 
        forward *= PLAYER_SPEED * dt
        self.position += forward

    def shoot(self):
        spawn_position = self.position + pygame.Vector2(0, 1).rotate(self.rotation) * self.radius
        if self.shot_cooldown_timer > 0:
            return        
        else:   
            bullet = Shot(spawn_position[0], spawn_position[1])
            bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS


