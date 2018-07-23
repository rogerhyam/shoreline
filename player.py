import pygame
import os

os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()

pygame.joystick.init()
js =pygame.joystick.Joystick(0)
js.init()

pygame.mixer.init()

def playTrack(track_id):
    pygame.mixer.music.load('mp3/' + str(track_id) + '.mp3')
    pygame.mixer.music.set_volume(1.0)
    print('mp3/' + str(track_id) + '.mp3')
    print(pygame.mixer.music.get_volume())
    pygame.mixer.music.play()


done = False

while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something        
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
            print(event.button)
            playTrack(event.button)

