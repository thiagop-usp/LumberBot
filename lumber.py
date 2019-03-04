import time
from pynput.keyboard import Key, Controller, Listener
import numpy as np
import mss
import pyautogui as pag

keyboard = Controller()

# left branches in game window:
num_branches = 6
# from left to right in px
branches_x = 121
# from top to bottom in px
branches_y = [435, 385, 335, 285, 235, 186]

# this is a bgra match for the wood color in the game (blue, green, red, alpha)
wood_rgba = [64, 114, 167, 255]

# checks if a pixel is tree-colored (I used the correlation feature because it can handle minor differences)
def is_tree(spot, i):
    similarity = np.corrcoef(spot[i], wood_rgba)[1][0]
    return similarity >= 0.98

class Bot:  
    # starts the game
    def start(self):
        pag.moveTo(20, 20)
        try:
            # play button
            button = pag.locateCenterOnScreen('play.png')
            pag.moveTo(button)
            pag.click()
            # these moves are done so that the bot gets aligned for the algorithm (See README for a better explanation)
            self.move_right()
            time.sleep(0.03)
            self.move_right()
            time.sleep(0.4)
            self.play()
        except:
            # replay button
            button = pag.locateCenterOnScreen('replay.png')
            pag.moveTo(button)
            pag.click()
            # these moves are done so that the bot gets aligned for the algorithm (See README for a better explanation)
            self.move_right()
            time.sleep(0.03)
            self.move_right()
            time.sleep(0.4)
            self.play()

    # how the bot moves:
    def move_right(self):
        keyboard.press(Key.right)
        keyboard.release(Key.right)
    def move_left(self):
        keyboard.press(Key.left)
        keyboard.release(Key.left)

    #the automation itself:
    def play(self):

        # This matches the game window on a 1366x768 resolution monitor. You can tweak it in case you wanna test it in your screen.
        game = {
            'top': 130,
            'left': 570,
            'width': 300,
            'height': 636
        }
        
        screen = mss.mss()
        while True:
            img = screen.grab(game)
            img_matrix = np.array(img)

            # getting tree pixels
            tree = [img_matrix[y, branches_x] for y in branches_y]

            hit = []

            for i in range(num_branches):
                if is_tree(tree, i):
                    self.move_right()
                    time.sleep(0.015)
                    self.move_right()
                else:
                    self.move_left()
                    time.sleep(0.015)
                    self.move_left()

            # these waits are crucial. The bot will go to fast without em and wont work.
            time.sleep(0.25)
        

if __name__ == '__main__':

    game = Bot()
    game.start()

