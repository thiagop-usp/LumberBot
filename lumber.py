import time
from pynput.keyboard import Key, Controller, Listener
import numpy as np
import mss
import pyautogui as pag

keyboard = Controller()

# left branches in game window:

num_branches = 6
# from left to right in px
branches_x = [121,121,121,121,121,121]
# from top to bottom in px
branches_y = [458, 408, 359, 309, 259, 209]

wood_rgba = [64, 114, 167, 255] 

def is_tree(img_matrix, i):
    x_pos = branches_x[i]
    y_pos = branches_y[i]
    spot = img_matrix[y_pos][x_pos]
    print(str((y_pos, x_pos)) + " " + str(spot))
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
        time.sleep(0.16)
    def move_left(self):
        keyboard.press(Key.left)
        keyboard.release(Key.left)
        time.sleep(0.16)

    #the automation itself:
    def play(self):
        screen = mss.mss()
        game = {
            'top': 130,
            'left': 570,
            'width': 300,
            'height': 636
        }
        self.move_right()
        self.move_right()
        
        while True:

            img = screen.grab(game)
            img_matrix = np.array(img)

            hit = []

            for i in range(num_branches):
                if is_tree(img_matrix, i):
                    hit.append(0)
                    hit.append(0)
                else:
                    hit.append(1)
                    hit.append(1)

            for h in hit:
                if h == 0:
                    self.move_right()
                else:
                    self.move_left()
            
            time.sleep(0.5)
        

if __name__ == '__main__':
    game = Bot()
    game.start()

