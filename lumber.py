import time
from pynput.keyboard import Key, Controller, Listener
import numpy as np
import mss
import pyautogui as pag

keyboard = Controller()

# left branches in game window:

num_branches = 6
# from left to right in px
branches_x = [181, 181, 181, 181, 181, 181]
# from top to bottom in px
branches_y = [400, 335, 270, 205, 134, 67]

wood_rgba = [64, 114, 167, 255] 

def is_tree(img_matrix, i):
    x_pos = branches_x[i]
    y_pos = branches_y[i]
    spot = img_matrix[y_pos][x_pos]
    return spot[0] == wood_rgba[0] and spot[1] == wood_rgba[1] and spot[2] == wood_rgba[2]

class Bot:  

    def start(self):
        try:
            button = pag.locateCenterOnScreen('play.png')
            pag.moveTo(button)
            pag.click()
            self.play()
        except:
            button = pag.locateCenterOnScreen('replay.png')
            pag.moveTo(button)
            pag.click()
            self.play()

    # how the bot moves:
    def move_right(self):
        keyboard.press(Key.right)
        keyboard.release(Key.right)
        time.sleep(0.016)
    def move_left(self):
        keyboard.press(Key.left)
        keyboard.release(Key.left)
        time.sleep(0.016)

    #the automation itself:
    def play(self):
        time.sleep(0.1)
        screen = mss.mss()
        game = {
            'top': 130,
            'left': 517,
            'width': 400,
            'height': 636
        }
        
        while True:
            img = screen.grab(game)
            img_matrix = np.array(img)

            for i in range(num_branches):
                if(is_tree(img_matrix, i)):
                    self.move_right()
                    self.move_right()
                else:
                    self.move_left()
                    self.move_left()
        

if __name__ == '__main__':
    game = Bot()
    game.start()

