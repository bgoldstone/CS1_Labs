# whackABell.py
#   A game that a user uses a mallet to hit the bell sprite a certain number of times to win before time runs out
#
# Date: 11/30/2020
# Name: Ben Goldstone
from random import randint
import pygame, os, datetime
# from label import Label
pygame.init()
pygame.mixer.init()
file = "highScores.txt"
if file not in os.listdir():
    tmp = open(file, "x")
    tmp.close()
highScoresFile = open(file, "a+")
hitSound = pygame.mixer.Sound("soundFX/hitSFX.ogg")
endingSound = pygame.mixer.Sound("soundFX/endingSFX.ogg")
missSound = pygame.mixer.Sound("soundFX/missSFX.wav")
# Constants
SCREEN_SIZE = (1280, 720)
NUM_TO_WIN = 5
MAX_SPEED = 20
TIME = 30 # seconds
TIME -= 1
gamePaused = False
mute = False
# Images
BG = "bg.png"

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("WACK A BELL — A game by Benjamin Goldstone!")


# Bell Sprite
class Bell(pygame.sprite.Sprite):
    def __init__(self, image, special):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.special = special
        self.wall = False
        self.size = 150
        if special:
            self.size -= 50
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.center = (randint(0, screen.get_width()), randint(0, screen.get_height()))
        # makes sure speed != 0
        self.int = 0
        while self.int == 0:
            self.int = randint(-MAX_SPEED, MAX_SPEED)
        self.dx = self.int
        # makes sure speed != 0
        self.int = 0
        while self.int == 0:
            self.int = randint(-MAX_SPEED, MAX_SPEED)
        self.dy = self.int

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        # if wall...
        if self.rect.left > screen.get_width():
            self.rect.right = 0
            self.wall = True
        elif self.rect.right < 0:
            self.rect.right = screen.get_width()
            self.wall = True
        elif self.rect.top > screen.get_height():
            self.rect.top = 0
            self.wall = True
        elif self.rect.bottom < 0:
            self.rect.bottom = screen.get_height()
            self.wall = True
        if self.wall:
            # makes sure speed != 0
            self.int = 0
            while self.int == 0:
                self.int = randint(-MAX_SPEED, MAX_SPEED)
            self.dx = self.int
            # makes sure speed != 0
            self.int = 0
            while self.int == 0:
                self.int = randint(-MAX_SPEED, MAX_SPEED)
            self.dy = self.int
            self.wall = False


# Mallet Sprite
class Mallet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        self.image = self.malletStationary
        self.rect = self.image.get_rect()
        self.hit = False
        self.frame = 0
        self.delay = 3
        self.pause = 0

    def update(self):
        if self.hit:
            pygame.mouse.set_visible(False)
            self.pause += 1
            # print(self.malletImages)
            if self.pause > self.delay:
                # reset pause and advance animation
                self.pause = 0
                self.frame += 2
                if self.frame < len(self.malletImages):
                    self.image = self.malletImages[self.frame]
                else:
                    self.frame = 0
                    self.hit = False
                    self.image = self.malletStationary
        else:
            self.rect.center = pygame.mouse.get_pos()
            self.rect.center = pygame.mouse.get_pos()
            pygame.mouse.set_visible(True)

    def loadImages(self):
        self.malletStationary = pygame.image.load("mallet/frame_00_delay-0.04s.png")
        self.malletStationary = self.malletStationary.convert()
        transColor = self.malletStationary.get_at((1, 1))
        self.malletStationary.set_colorkey(transColor)
        self.malletImages = []
        os.chdir("mallet")
        for file in os.listdir():
            if file != "frame_00_delay-0.04s.png":
                tmpImage = pygame.image.load(file)
                tmpImage = tmpImage.convert()
                transColor = tmpImage.get_at((1, 1))
                tmpImage.set_colorkey(transColor)
                self.malletImages.append(tmpImage)
        os.chdir("..")


def titleScreen():
    background = pygame.Surface(screen.get_size())  # Construct a background
    background = background.convert()
    background.fill((110, 255, 100))  # Clear the background
    screen.blit(background, (0, 0))  # Blit background to screen only once.

    # Construct labels for a title and game instructions.
    topMsg = Label("Wack A Bell!", (screen.get_width() // 2, 100), None, 30, (0, 0, 0), )
    upperMiddleMsg = Label(
        f"To win: click left mouse button to \"whack the golden\" bell {NUM_TO_WIN} times in the given time",
        (screen.get_width() // 2, 300), None, 30, (0, 0, 0))
    lowerMiddleMsg = Label(
        f"If you hit the background or any other bell, the number of bells to whack will increase! If time runs out, you loose!!",
        (screen.get_width() // 2, 400), None, 30, (0, 0, 0))
    bottomMsg0 = Label(f"hit \"p\" or spacebar to pause and \"m\" to mute sound", (screen.get_width() // 2, 510), None,
                       30, (0, 0, 0))

    bottomMsg = Label("Click to start", (screen.get_width() // 2, 620), None, 30, (0, 0, 0))
    # Add the labels to a group
    labelGroup = pygame.sprite.Group(topMsg, upperMiddleMsg, lowerMiddleMsg, bottomMsg0, bottomMsg)
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)  # Frame rate 30 frames per second.
        for event in pygame.event.get():  # Handle any events
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Title screen ends
                keepGoing = False  # when mouse clicked
            elif event.type == pygame.KEYDOWN:  # or any key pressed
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    keepGoing = False

        labelGroup.clear(screen, background)  # Update the display
        labelGroup.update()
        labelGroup.draw(screen)

        pygame.display.flip()


def playAgain(winLose):
    global mute
    background = pygame.Surface(screen.get_size())  # Construct a background
    background = background.convert()

    if winLose:
        fillColor = (110, 255, 100)
        labelText = "You Win :)"
        labelColor = (128, 0, 0)
        if not (mute):
            endingSound.play()
    else:
        fillColor = (128, 0, 0)
        labelText = "You Lose :("
        labelColor = (110, 255, 100)

    background.fill(fillColor)
    screen.blit(background, (0, 0))

    # Construct Labels
    label0 = Label(labelText, (screen.get_width() // 2, 110), None, 60, labelColor, False)
    label1 = Label("Play again?", (screen.get_width() // 2, 280), None, 60, labelColor, False)
    label2 = Label("(Y/N)", (screen.get_width() // 2, 380), None, 60, labelColor, False)
    labelGroup = pygame.sprite.Group(label0, label1, label2)

    clock = pygame.time.Clock()
    keepGoing = True
    replay = False

    while keepGoing:

        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    replay = True
                    keepGoing = False
                    endingSound.stop()
                elif event.key == pygame.K_n or event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    keepGoing = False
                elif event.key == pygame.K_m:
                    mute = not mute
                    if mute:
                        pygame.mixer.stop()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False

        labelGroup.clear(screen, background)
        labelGroup.update()
        labelGroup.draw(screen)

        pygame.display.flip()

    return replay


def endScreen():
    background = pygame.Surface(screen.get_size())  # Construct a background
    background = background.convert()
    background.fill((0, 255, 255))
    screen.blit(background, (0, 0))  # Blit background to screen only once.

    # Construct a Label object to display the message and add it to a group.
    label1 = Label("Good Bye...", (screen.get_width() // 2, 210), None, 60, (0, 0, 0), False)
    label2 = Label("A Game by Benjamin Goldstone", (screen.get_width() // 2, 320), None, 30, (0, 0, 0), False)
    labelGroup = pygame.sprite.Group(label1, label2, )

    clock = pygame.time.Clock()
    keepGoing = True
    frames = 0  # 5 seconds will be 150 frames

    while keepGoing:

        clock.tick(30)  # Frame rate 30 frames per second.
        frames = frames + 1  # Count the number of frames displayed
        if frames == 150:  # After 5 seconds end the message display
            keepGoing = False

        for event in pygame.event.get():  # Impatient people can quit earlier
            if (event.type == pygame.QUIT or
                    event.type == pygame.KEYDOWN or
                    event.type == pygame.MOUSEBUTTONDOWN):
                keepGoing = False

        labelGroup.clear(screen, background)
        labelGroup.update()
        labelGroup.draw(screen)

        pygame.display.flip()


class Label(pygame.sprite.Sprite):
    def __init__(self, textStr, center, font, fontSize, textColor, background=True):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(font, fontSize)
        self.text = textStr
        self.center = center
        self.textColor = textColor
        self.background = background

    def update(self):
        self.image = self.font.render(self.text, 1, self.textColor)
        self.rect = self.image.get_rect()
        self.rect.center = self.center
        self.surface = (
            self.rect.left - 25, self.rect.top - 25, self.image.get_size()[0] + 50, self.image.get_size()[1] + 50)
        # print(self.surface)
        if self.background:
            pygame.draw.rect(screen, (255, 255, 255), self.surface, 0)


def paused():
    global gamePaused
    background = pygame.Surface(screen.get_size())  # Construct a background
    background = background.convert()
    background.fill((0, 0, 0))
    background.set_alpha(200)
    screen.blit(background, (0, 0))
    pauseText = Label("Game Paused", (screen.get_width() // 2, screen.get_height() // 2 - 100), None, 50,
                      (255, 255, 255), False)
    pauseText2 = Label("To start again hit Spacebar or \"p\"",
                       (screen.get_width() // 2, screen.get_height() // 2 + 100), None, 50, (255, 255, 255), False)
    labelSprites = pygame.sprite.Group(pauseText, pauseText2)
    while gamePaused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamePaused = not gamePaused
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    gamePaused = not gamePaused
                if event.key == pygame.K_p or event.key == pygame.K_SPACE:
                    gamePaused = not gamePaused
        labelSprites.clear(screen, background)

        labelSprites.update()

        labelSprites.draw(screen)

        pygame.display.flip()
    labelSprites.clear(screen, background)

def highScores(time):
    writeString = f"Player whacked {time[2]} bells on " + str(datetime.datetime.now()) + " and was completed in " + str(time[0]) + ":" + str(time[1]) + " seconds"
    print(writeString)
    highScoresFile.write(writeString)
    highScoresFile.write("\n")
    highScoresFile.close()
def game():
    # Background Setup
    global gamePaused, mute
    background = pygame.image.load(BG).convert()
    screen.blit(background, (0, 0))

    # Generates Bell Objects
    bells = []
    os.chdir("bells")
    bells.append(Bell("bell.png", True))
    for file in os.listdir():
        if not (file == "bell.png"):
            bells.append(Bell(file, False))
    os.chdir("..")

    # Generates Mallet Objects
    # mallets = []
    mallet = Mallet()
    # for file in os.listdir():
    #     if file == (not("frame_00_delay-0.04s.png")):
    #         mallets.append(Hammer(file))
    # os.chdir("..")
    # Labels
    scoreboard = Label("Number to Win: ", (screen.get_width() - 200, screen.get_height() - 50), None, 40, (0, 0, 0))
    timeLeft = Label("Time Left: ", (200, screen.get_height() - 50), None, 40, (0, 0, 0))
    # Sprite Groups
    # bell = pygame.sprite.Group(bells[0])
    bellGroup = pygame.sprite.Group(bells)
    # mallet = pygame.sprite.Group(mallets[0])
    # malletGroup = pygame.sprite.Group(mallets[1:])
    activeSprites = pygame.sprite.Group(bells, mallet)
    labelSprite = pygame.sprite.Group(scoreboard, timeLeft)

    # vars
    keepGoing = True
    win = False
    clock = pygame.time.Clock()
    fps = 30
    frames = 0
    numToWin = NUM_TO_WIN
    # game loop
    while keepGoing:
        clock.tick(fps)
        frames += 1
        if (numToWin <= 0):
            win = True
            keepGoing = False
        # if time is out
        if fps * TIME <= frames:
            keepGoing = False
            win = False
        whackList = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    keepGoing = False
                # Pauses Game
                if event.key == pygame.K_p or event.key == pygame.K_SPACE:
                    gamePaused = not gamePaused
                # Mutes Sound
                if event.key == pygame.K_m:
                    mute = not mute
                    if mute:
                        pygame.mixer.stop()
            # if pressed and collided, append to whacklist

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_visible(False)
                whackList = pygame.sprite.spritecollide(mallet, bellGroup, False)
                if not (whackList):
                    numToWin += 1
                    if pygame.mixer.get_busy():
                        pygame.mixer.stop()
                    if not mute:
                        missSound.play()
            else:
                pygame.mouse.set_visible(True)
        for bell in whackList:  # whackList is all the bells that are currently being hit
            if bell.special:
                numToWin -= 1
                # if already playing sound
                if pygame.mixer.get_busy():
                    pygame.mixer.stop()
                if not (mute):
                    hitSound.play()
                mallet.hit = True
                break
            # Any other bell
            else:
                numToWin += 1
                if pygame.mixer.get_busy():
                    pygame.mixer.stop()
                if not mute:
                    missSound.play()

        if gamePaused:
            paused()
            screen.blit(background, (0, 0))
        scoreboard.text = "Bells remaining: " + str(numToWin)
        timeLeft.text = "Time Left: " + str(TIME - (frames // fps))  # + ":" +str(fps - (frames%fps))
        activeSprites.clear(screen, background)
        labelSprite.clear(screen, background)

        activeSprites.update()
        labelSprite.update()

        activeSprites.draw(screen)
        labelSprite.draw(screen)

        pygame.display.flip()

    pygame.mixer.stop()
    time = [(TIME - (frames // fps)),(fps - (frames%fps)), NUM_TO_WIN]
    return [win,time]

def main():
    titleScreen()
    replay = True
    while replay:
        result,time = game()
        replay = playAgain(result)
        if result:
            highScores(time)
    endScreen()


main()
pygame.quit()