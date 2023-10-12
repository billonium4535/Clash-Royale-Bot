import random
import time

import mouse
import pygetwindow
import pyautogui


def get_window_location_size(windowTitle):
    try:
        window = pygetwindow.getWindowsWithTitle(windowTitle)[0]
        windowLocation = window.left, window.top
        windowSize = window.width, window.height
        return windowLocation, windowSize
    except IndexError:
        return None


def play():
    # press battle
    mouse.move(location[0] + 222, location[1] + 649)
    time.sleep(1)
    mouse.click()
    print("Clicked battle")

    # wait for the game to load
    time.sleep(10)
    print("Game loaded")

    # check if game is over
    screen_image = pyautogui.screenshot()
    okPixel = screen_image.getpixel((location[0] + 252, location[1] + 865))
    while abs(okPixel[0] - 105) != 0 and abs(okPixel[1] - 186) != 0 and abs(okPixel[2] - 255) != 0:
        time.sleep(1)

        # check if the ok button is there
        screen_image = pyautogui.screenshot()
        okPixel = screen_image.getpixel((location[0] + 252, location[1] + 865))

        # play the game
        card1Pixel = screen_image.getpixel((location[0] + 141, location[1] + 888))
        card2Pixel = screen_image.getpixel((location[0] + 225, location[1] + 888))
        card3Pixel = screen_image.getpixel((location[0] + 305, location[1] + 888))
        card4Pixel = screen_image.getpixel((location[0] + 386, location[1] + 888))

        randomCard = random.randint(0, 3)

        if randomCard == 0:
            # play card 1
            if abs(card1Pixel[0] - 208) > 30 or abs(card1Pixel[1] - 208) > 30 and abs(card1Pixel[2] - 208) > 30:
                mouse.move(random.randint(location[0] + 138, location[0] + 143), random.randint(location[1] + 880, location[1] + 892))
                time.sleep(1)
                mouse.click()
                if random.randint(0, 1) == 0:
                    mouse.move(random.randint(location[0] + 346, location[0] + 350), random.randint(location[1] + 486, location[1] + 492))
                    time.sleep(1)
                    mouse.click()
                else:
                    mouse.move(random.randint(location[0] + 98, location[0] + 106), random.randint(location[1] + 486, location[1] + 492))
                    time.sleep(1)
                    mouse.click()
                print("Played card 1")
                time.sleep(1)

        elif randomCard == 1:
            # play card 2
            if abs(card2Pixel[0] - 208) > 30 or abs(card2Pixel[1] - 208) > 30 and abs(card2Pixel[2] - 208) > 30:
                mouse.move(random.randint(location[0] + 220, location[0] + 230),
                           random.randint(location[1] + 880, location[1] + 892))
                time.sleep(1)
                mouse.click()
                if random.randint(0, 1) == 0:
                    mouse.move(random.randint(location[0] + 346, location[0] + 350),
                               random.randint(location[1] + 486, location[1] + 492))
                    time.sleep(1)
                    mouse.click()
                else:
                    mouse.move(random.randint(location[0] + 98, location[0] + 106),
                               random.randint(location[1] + 486, location[1] + 492))
                    time.sleep(1)
                    mouse.click()
                print("Played card 2")
                time.sleep(1)

        elif randomCard == 2:
            # play card 3
            if abs(card3Pixel[0] - 208) > 30 or abs(card3Pixel[1] - 208) > 30 and abs(card3Pixel[2] - 208) > 30:
                mouse.move(random.randint(location[0] + 300, location[0] + 310),
                           random.randint(location[1] + 880, location[1] + 892))
                time.sleep(1)
                mouse.click()
                if random.randint(0, 1) == 0:
                    mouse.move(random.randint(location[0] + 346, location[0] + 350),
                               random.randint(location[1] + 486, location[1] + 492))
                    time.sleep(1)
                    mouse.click()
                else:
                    mouse.move(random.randint(location[0] + 98, location[0] + 106),
                               random.randint(location[1] + 486, location[1] + 492))
                    time.sleep(1)
                    mouse.click()
                print("Played card 3")
                time.sleep(1)

        elif randomCard == 3:
            # play card 4
            if abs(card4Pixel[0] - 208) > 30 or abs(card4Pixel[1] - 208) > 30 and abs(card4Pixel[2] - 208) > 30:
                mouse.move(random.randint(location[0] + 380, location[0] + 390),
                           random.randint(location[1] + 880, location[1] + 892))
                time.sleep(1)
                mouse.click()
                if random.randint(0, 1) == 0:
                    mouse.move(random.randint(location[0] + 346, location[0] + 350),
                               random.randint(location[1] + 486, location[1] + 492))
                    time.sleep(1)
                    mouse.click()
                else:
                    mouse.move(random.randint(location[0] + 98, location[0] + 106),
                               random.randint(location[1] + 486, location[1] + 492))
                    time.sleep(1)
                    mouse.click()
                print("Played card 4")
                time.sleep(1)

    # click the ok button
    mouse.move(location[0] + 252, location[1] + 865)
    time.sleep(1)
    mouse.click()
    print("Clicked ok button")

    # wait for menu to load
    time.sleep(5)
    print("Menu loaded")


window_title = "FP4"
window_info = get_window_location_size(window_title)

if window_info is not None:
    location, size = window_info
    print("Window Location:", location)
    print("Window Size:", size)
else:
    print("Window not found.")


while True:
    print("Starting in 5s")
    time.sleep(5)
    play()
    # x, y = pyautogui.position()
    # print(pyautogui.pixel(x, y))
    # print("({}, {})".format((mouse.get_position()[0] - location[0]), mouse.get_position()[1] - location[1]))
