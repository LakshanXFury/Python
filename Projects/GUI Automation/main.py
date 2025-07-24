import pyautogui
from PIL import ImageGrab
import time
import webbrowser


def detect_obstacle():
    # Take a screenshot of the area just in front of the dinosaur
    # You may need to adjust these coordinates based on your screen and game location
    bbox = (214, 732, 443, 785)  # (left, top, right, bottom) y=368
    img = ImageGrab.grab(bbox)
    pixels = img.load()

    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            if r < 150 and g < 150 and b < 150:  # RGB in GREY
                return True
    return False


def is_game_over():
    x, y = 627, 923
    pixel = ImageGrab.grab().load()[x, y]
    r, g, b = pixel
    return r > 200 and g > 200 and b > 200


def main():
    # Open the URL in a new browser tab
    webbrowser.open_new_tab("https://elgoog.im/dinosaur-game/")

    # Wait for the page to load
    time.sleep(5)

    # Start the game
    pyautogui.press("space")

    time.sleep(1)  # Short delay before detection starts

    while True:
        if detect_obstacle():
            pyautogui.press("space")
        time.sleep(0.01)  # Small delay to reduce CPU usage


main()

""" Using only PyAutoGui to open the browser"""

# def main():
#     # Pause for user to focus on Chrome
#     user_input = pyautogui.prompt(text="Focus Chrome now", title="To start the game")
#
#     # Short delay to allow Chrome to fully focus
#     time.sleep(1)
#
#     # Open new tab
#     pyautogui.hotkey("ctrl", "t")
#     time.sleep(0.5)  # small delay after opening tab
#
#     # Type the URL
#     pyautogui.write("https://elgoog.im/dinosaur-game/")
#     time.sleep(0.5)
#
#     # Press Enter to open the page
#     pyautogui.press("enter")
#
#
# main()
