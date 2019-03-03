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

wood_rgba = [64, 114, 167, 255]

def is_tree(spot, i):
    print(spot[i])
    similarity = np.corrcoef(spot[i], wood_rgba)[1][0]
    print(similarity)
    return similarity >= 0.98

class Bot:  

    def start(self):
        try:
            button = pag.locateCenterOnScreen('play.png')
            pag.moveTo(button)
            pag.click()
            self.move_right()
            time.sleep(0.03)
            self.move_right()
            time.sleep(0.5)
            self.play()
        except:
            button = pag.locateCenterOnScreen('replay.png')
            pag.moveTo(button)
            pag.click()
            self.move_right()
            time.sleep(0.03)
            self.move_right()
            time.sleep(0.5)
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

            tree = [img_matrix[y, branches_x] for y in branches_y]

            hit = []

            for i in range(num_branches):
                if is_tree(tree, i):
                    #print('direita')
                    #self.move_right()
                    keyboard.press(Key.right)
                    keyboard.release(Key.right)
                    time.sleep(0.025)
                    keyboard.press(Key.right)
                    keyboard.release(Key.right)
                else:
                    #print('esquerda')
                    #self.move_left()
                    keyboard.press(Key.left)
                    keyboard.release(Key.left)
                    time.sleep(0.025)
                    keyboard.press(Key.left)
                    keyboard.release(Key.left)
                    #self.move_left()
            time.sleep(0.25)
        

if __name__ == '__main__':
    game = Bot()
    game.start()

