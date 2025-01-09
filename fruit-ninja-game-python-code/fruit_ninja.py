import pygame
import sys
import os
import random
from pygame import mixer

# Constants
WIDTH = 800
HEIGHT = 500
FPS = 12

player_lives = 3
score = 0
fruits = ['watermelon', 'big_watermelon', 'coconut', 'big_coconut', 'pomegranate', 'big_pomegranate',
          'apple', 'big_apple', 'bomb', 'TNT']

# Initialize Pygame and mixer
pygame.init()
mixer.init()

pygame.display.set_caption('Better FRUIT NINJA--DataFlair')
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load background and font
gameDisplay.fill(BLACK)
background = pygame.image.load('back.jpg')
font = pygame.font.Font(os.path.join(os.getcwd(), 'PSLCDMatrixII.ttf'), 32)


# Generalized structure of the fruit Dictionary
data = {}

def generate_random_fruits(fruit):
    fruit_path = "image/" + fruit + ".png"
    data[fruit] = {
        'img': pygame.image.load(fruit_path),
        'x': random.randint(100, 500),
        'y': 800,
        'speed_x': random.randint(-10, 10),
        'speed_y': random.randint(-80, -60),
        'throw': random.random() >= 0.75,
        't': 0,
        'hit': False,
    }

# Generate initial fruits
for fruit in fruits:
    generate_random_fruits(fruit)

# Method to draw fonts
def draw_text(display, text, size, x, y, font_name):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    display.blit(text_surface, text_rect)

# Draw player lives
def draw_lives(display, x, y, lives, image):
    for i in range(lives):
        img = pygame.image.load(image)
        img_rect = img.get_rect()
        img_rect.x = int(x + 35 * i)
        img_rect.y = y
        display.blit(img, img_rect)


# Hide cross lives
def hide_cross_lives(x, y):
    gameDisplay.blit(pygame.image.load("image/red_lives.png"), (x, y))


# Show game over screen
def show_gameover_screen():
    mixer.music.load("Gaming_Music.mp3")
    mixer.music.play(-1)


    gameDisplay.blit(background, (0, 0))
    draw_text(gameDisplay, "FRUIT NINJA!", 64, WIDTH / 2, HEIGHT / 4, os.path.join(os.getcwd(), 'PSLCDMatrixII.ttf'))


    if not game_over:
        draw_text(gameDisplay, "SCORE : " + str(score), 40, WIDTH / 2, HEIGHT / 250, os.path.join(os.getcwd(), 'PSLCDMatrixII.ttf'))
        draw_text(gameDisplay, "TIME : " + str(countdown_timer), 40, WIDTH / 2, HEIGHT / 2 + 50, os.path.join(os.getcwd(), 'PSLCDMatrixII.ttf'))


        draw_text(gameDisplay, "Press a key to go to SETTINGS", 30, WIDTH / 2, 400, os.path.join(os.getcwd(), 'PSLCDMatrixII.ttf'))
    #draw_text(gameDisplay, "Press a key to begin!", 30, WIDTH / 2, HEIGHT * 3 / 4, os.path.join(os.getcwd(), 'comic.ttf'))
    pygame.display.flip()


    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


# Show settings screen
def show_settings_screen():
    global time_limit_seconds, countdown_timer, selected_time  # เพิ่ม selected_time


    gameDisplay.blit(background, (0, 0))
    draw_text(gameDisplay, "SETTINGS", 64, WIDTH / 3, HEIGHT / 16, os.path.join(os.getcwd(), 'PSLCDMatrixII.ttf'))
    draw_text(gameDisplay, "Sound Effects", 30, WIDTH / 2, 175, os.path.join(os.getcwd(), 'PSLCDMatrixII.ttf'))


    sound_enabled = True
    sound_text = "Sound: ON" if sound_enabled else "Sound: OFF"
    draw_text(gameDisplay, sound_text, 24, WIDTH / 2, 225, os.path.join(os.getcwd(), 'PSLCDMatrixII.ttf'))


    draw_text(gameDisplay, "Time Duration", 30, WIDTH / 2, 275, os.path.join(os.getcwd(), 'PSLCDMatrixII.ttf'))
    draw_text(gameDisplay, "Caution : You must select the time!", 18, WIDTH / 2, 320, os.path.join(os.getcwd(), 'PSLCDMatrixII.ttf'))
    draw_text(gameDisplay, "60 seconds : press 1", 24, WIDTH / 2, 345, os.path.join(os.getcwd(), 'PSLCDMatrixII.ttf'))
    draw_text(gameDisplay, "30 seconds : press 2", 24, WIDTH / 2, 375, os.path.join(os.getcwd(), 'PSLCDMatrixII.ttf'))


    draw_text(gameDisplay, "Press 'Q' to start game!", 30, WIDTH / 2, 420, os.path.join(os.getcwd(), 'PSLCDMatrixII.ttf'))
    pygame.display.flip()


    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    waiting = False
                elif event.key == pygame.K_1:
                    selected_time = 60
                    print("Time Duration set to 60 seconds")
                elif event.key == pygame.K_2:
                    selected_time = 30
                    print("Time Duration set to 30 seconds")


            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos


                if WIDTH / 2 - 50 < mouseX < WIDTH / 2 + 50 and 225 < mouseY < 250 :
                    sound_enabled = not sound_enabled


                    if sound_enabled:
                        mixer.music.play(-1)
                    else:
                        mixer.music.stop()
# Game Loop
first_round = True
game_over = True
game_running = True
selected_time = 0
countdown_timer = 0
# เพิ่มตัวแปร countdown_timer และกำหนดค่าเริ่มต้น

while game_running:
    if game_over:
        if first_round:
            show_gameover_screen()
            pygame.display.flip()

            waiting = True
            while waiting:
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYUP:
                        #if event.key == pygame.K_TAB:
                            waiting = False
                            show_settings_screen()
            first_round = False
            
        
        game_over = False
        player_lives = 3
        score = 0
     
        show_settings_screen()

        countdown_timer = selected_time
        pygame.time.set_timer(pygame.USEREVENT, 1000)


    gameDisplay.blit(background, (0, 0))
   
    # แสดงคะแนนและเวลาบนหน้าจอ
    draw_text(gameDisplay, 'SCORE : ' + str(score), 32, WIDTH / 10, 0, os.path.join(os.getcwd(), 'PSLCDMatrixII.ttf'))
    draw_text(gameDisplay, 'TIME : ' + str(countdown_timer), 32, WIDTH / 2, 2, os.path.join(os.getcwd(), 'PSLCDMatrixII.ttf'))
   
    draw_lives(gameDisplay, 690, 5, player_lives, 'image/red_lives.png')


    for key, value in data.items():
        if value['throw']:
            value['x'] += value['speed_x']
            value['y'] += value['speed_y']
            value['speed_y'] += (1 * value['t'])
            value['t'] += 1


            if value['y'] <= 800:
                gameDisplay.blit(value['img'], (value['x'], value['y']))
            else:
                generate_random_fruits(key)


            current_position = pygame.mouse.get_pos()


            if not value['hit'] and current_position[0] > value['x'] and current_position[0] < value['x'] + 60 \
                    and current_position[1] > value['y'] and current_position[1] < value['y'] + 60:
                if key == 'bomb' :
                    player_lives -= 1
                    if player_lives == 0:
                        hide_cross_lives(690, 15)
                    elif player_lives == 1 :
                        hide_cross_lives(725, 15)
                    elif player_lives == 2 :
                        hide_cross_lives(760, 15)
                  
                    if player_lives < 0 :
                        show_gameover_screen()
                        game_over = True

                    half_fruit_path = "image/explosion.png"

                elif key == 'TNT' :
                    player_lives -= 1
                    if player_lives == 0:
                        hide_cross_lives(690, 15)
                    elif player_lives == 1 :
                        hide_cross_lives(725, 15)
                    elif player_lives == 2 :
                        hide_cross_lives(760, 15)
                  
                    if player_lives < 0 :
                        show_gameover_screen()
                        game_over = True

                    half_fruit_path = "image/explosion.png"
                else:
                    half_fruit_path = "image/" + "half_" + key + ".png"


                    if key != 'TNT' or 'bomb' :
                       if key == 'big_watermelon' or key == 'big_coconut' or key == 'big_pomegranate' or key =='big_apple' :
                          score += 2
                       elif key == 'watermelon' or key == 'coconut' or key == 'pomegranate' or key == 'apple' :
                          score += 1
                    else :
                          score = score

                value['img'] = pygame.image.load(half_fruit_path)
                value['speed_x'] += 10
                value['hit'] = True
        else:
            generate_random_fruits(key)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.USEREVENT:
            countdown_timer -= 1
            if countdown_timer <= 0:
                show_gameover_screen()
                game_over = True
                

    pygame.display.update()
    
    clock.tick(FPS)
    


pygame.quit()
