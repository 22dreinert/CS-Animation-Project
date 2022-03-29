# imports
import pygame, os, sys

# center pygame window on display
# technique found at https://stackoverflow.com/questions/5814125/how-to-designate-where-pygame-creates-the-game-window
os.environ['SDL_VIDEO_CENTERED'] = '1'

# initialize pygame
pygame.init()

# constants
WIDTH = 1440
HEIGHT = 900
FPS = 3

# RGB colors
white = (255, 255, 255)
black = (0, 0, 0)

# variables
image_count = 0 # counter for images
clock = pygame.time.Clock() # clock object
running = True
timer = 0

# load images into pygame
my_images = [
pygame.image.load('./assets/sarah_v1_1.png'),
pygame.image.load('./assets/sarah_v1_2.png'),
pygame.image.load('./assets/sarah_v1_3.png')
]

# changes size of all images to fit screen
for i in range(len(my_images)):
  my_images[i] = pygame.transform.scale(my_images[i], (200, 200))

# set Window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Turtle")
WINDOW.fill(white)

# set up your font
font = pygame.font.Font('./fonts/Roboto-Medium.ttf', 12)

# create your text
text1 = font.render('hello', True, black, white)
text2 = font.render('Designed by Sarah Dougherty', True, black, white) 
text3 = font.render('Programed by Allen and Dillon', True, black, white)
text1Rect = text1.get_rect()
text2Rect = text2.get_rect()
text3Rect = text3.get_rect()

# position the text
text1Rect.center = (WIDTH // 2, HEIGHT // 7)
text2Rect.center = (WIDTH // 1.3, HEIGHT // 3)
text3Rect.center = (WIDTH // 1.3, HEIGHT // 2)
# display text
WINDOW.blit(text1, text1Rect)
WINDOW.blit(text2, text2Rect)
WINDOW.blit(text3, text3Rect)
pygame.display.flip()

# draw shape function
def drawShape():
  global my_images
  global image_count
  if (image_count == 3):
    image_count = 0
  WINDOW.blit(my_images[image_count], (0, 100))
  pygame.display.flip()
  image_count += 1
  
# main animation Loop that will run for 10 seconds
while running and timer < 50:

  # upadate screen according to FPS value
  clock.tick(FPS)

  # update timer
  timer += 1

  # check if "X" is clicked by user 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
      sys.exit()

  # call to drawShape function
  drawShape()
