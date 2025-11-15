from pygame import *
import random
import math

class Paddle:
    def __init__(self, x, y, width, height, screen_height):
        self.rect = Rect(x, y, width, height)
        self.screen_height = screen_height

    def paddle_movement(self, key, up_key, down_key):
        # Paddle Movement
        if key[up_key] and self.rect.top > 0:
            self.rect.y -= 10
        if key[down_key] and self.rect.bottom < self.screen_height:
            self.rect.y += 10
            

class Ball:
    def __init__(self, x, y, screen_width, screen_height):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.radius = 7
        self.base_speed = 7
        self.angle = math.radians(random.randrange(0, 360, 10)) # Random initial angle
        self.speed_x = 7 #self.base_speed * math.cos(self.angle)
        self.speed_y = 7 #self.base_speed * math.sin(self.angle)

    def move(self, screen_height): # Move the ball
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off top and bottom
        if self.y-self.radius <= 0 or self.y + self.radius >= screen_height:
            self.speed_y = -self.speed_y
        #todo: improve bounce angle based on hit position
        
    def bounce_paddle(self, paddle): # Bounce off paddle            
        ball_rect = Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2) # Create ball rect for collision
        if ball_rect.colliderect(paddle.rect):
            self.speed_x = -(self.speed_x+1 if self.speed_x > 0 else self.speed_x-1) #!fix: score in high speed
    
    def stop(self): # Stop the ball
        self.speed_x = 0
        self.speed_y = 0
        
    def resume(self, speed_x, speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y
        #todo: implement resume functionality properly
        

    def reset(self, screen_width, screen_height):
        self.x = screen_width // 2
        self.y = screen_height // 2
        #angle = math.radians(pi/random.randrange(-90, 90, 12)) # Random initial angle
        if self.speed_x < 0:
            self.speed_x = 7#  * math.cos(angle)
        else:
            self.speed_x = -7# * math.cos(angle)
            
        self.speed_y = 7# * math.sin(angle)
        
        #todo: randomize direction after reset

class Game:
    def __init__(self):
        
        #Game Settings
        self.width = 800
        self.height = 600
        self.screen = display.set_mode((self.width, self.height))
        self.running = True
        self.colors = {"background": (0, 0, 0), "paddle": (255, 255, 255), "ball": (255, 0, 0)}


        #Game Objects
        self.ball = Ball(self.width//2, self.height//2, self.width, self.height)
        self.paddle_L = Paddle(self.width - 20, self.height//2 - 30, 10, 60, self.height) # Left Paddle
        self.paddle_R = Paddle(10, self.height//2 - 30, 10, 60, self.height) # Right Paddle
        self.pause_screen = Rect(self.width//2 - 100, self.height//2 - 50, 200, 100) # Pause Screen
        self.center_line = Rect(self.width//2 - 5, 0, 10, self.height) # Center Line

        self.score_L, self.score_R = 0, 0
        self.pause_game = False
        
        # Font for score display
        self.font = font.Font(None, 74)  

        display.set_caption("Pong Game - By BARO")

    def score_update(self):#, ball):
        side_x = self.ball.x - self.ball.radius  # Ball x edge
        if side_x <= 0:
            self.score_L += 1
            self.ball.reset(self.width, self.height)
        if side_x >= self.width:
            self.score_R += 1
            self.ball.reset(self.width, self.height)

        
init() #Initialize Pygame

#Setup Game        
clock = time.Clock()
game = Game() #Create Game Instance
game.running = True

#Game Loop
while game.running:
    for evt in event.get(): # Event Loop
        if evt.type == QUIT or (evt.type == KEYDOWN and evt.key == K_ESCAPE): # Exit on window close or ESC key
            game.running = False
        if evt.type == KEYDOWN:
            if evt.key == K_p: #!fix: toggle pause on 'P' key
                game.pause_game = not game.pause_game
                if game.pause_game:
                    game.ball.stop()


    game.screen.fill(game.colors["background"]) # Clear Screen

    pressed = key.get_pressed() # Key Presses
    game.paddle_L.paddle_movement(pressed, K_UP, K_DOWN) # Left Paddle Movement
    game.paddle_R.paddle_movement(pressed, K_w, K_s) # Right Paddle Movement

    # Draw Game Objects
    draw.rect(game.screen, game.colors["paddle"], game.paddle_L) # Draw left paddle
    draw.rect(game.screen, game.colors["paddle"], game.paddle_R) # Draw right paddle
    draw.circle(game.screen, game.colors["ball"], (game.ball.x, game.ball.y), game.ball.radius) # Draw the ball
    
    for i, y in enumerate(range(0, game.height, game.height//20)): # Draw center line
        if i % 2 == 1:
            continue
        draw.rect(game.screen, game.colors["paddle"], (game.width//2 - 5, y, 10, game.height//20)) 
    
    # Draw scores
    score_L_text = game.font.render(str(game.score_L), True, game.colors["paddle"])
    score_R_text = game.font.render(str(game.score_R), True, game.colors["paddle"])
    game.screen.blit(score_L_text, (game.width * 3//4 - score_L_text.get_width()//2, 20))
    game.screen.blit(score_R_text, (game.width * 1//4 - score_R_text.get_width()//2, 20))

    if not game.pause_game: # Update game only if not paused
        game.ball.move(game.height)
        game.ball.bounce_paddle(game.paddle_L)
        game.ball.bounce_paddle(game.paddle_R)
        game.score_update()
        
    # Update Display
    display.flip()
    clock.tick(60)

quit()