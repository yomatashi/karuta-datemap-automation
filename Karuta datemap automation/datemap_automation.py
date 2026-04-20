import pyautogui
import time

'''
author      :   @yomatashi
description :   automate Karuta date-solver map based on solution's direction from any date solver bot
version     :   1.0 
note        :   if it clicks on a different location of the emoji, set region like "juice" 
'''

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1
directions = pyautogui.prompt('paste the map sovler direction here.')
direction_list = directions.split()
delay_time = 5

for direction in direction_list:
    match direction:
        case ":arrow_up_small:":
            up = pyautogui.locateCenterOnScreen("img/u.png", confidence=0.9)
            print("up ",up)
            pyautogui.click(up)
            pyautogui.moveTo(1200,573)
            time.sleep(delay_time)
        case ":arrow_down_small:":
            down = pyautogui.locateCenterOnScreen("img/d.png", confidence=0.9)
            print("down ",down)
            pyautogui.click(down)
            pyautogui.moveTo(1200,573)
            time.sleep(delay_time)
        case ":arrow_forward:":
            right = pyautogui.locateCenterOnScreen("img/r.png", confidence=0.9)
            print("right ",right)
            pyautogui.click(right)
            pyautogui.moveTo(1200,573)
            time.sleep(delay_time)
        case ":arrow_backward:":
            left = pyautogui.locateCenterOnScreen("img/l.png", confidence=0.95)
            print("left ",left)
            pyautogui.click(left)
            pyautogui.moveTo(1200,573)
            time.sleep(delay_time)
        case ":sandwich:":
            sandwhich = pyautogui.locateCenterOnScreen("img/s.png",region=(433,577,500,220), confidence=0.95)
            print("sandwhich shop",sandwhich)
            pyautogui.click(sandwhich)
            pyautogui.moveTo(1200,573)
            time.sleep(delay_time)
        case ":blossom:":
            blossom = pyautogui.locateCenterOnScreen("img/f.png",region=(433,577,500,220), confidence=0.9)
            print("flower ",blossom)
            pyautogui.click(blossom)
            pyautogui.moveTo(1200,573)
            time.sleep(delay_time)
        case ":coffee:":
            coffee = pyautogui.locateCenterOnScreen("img/c.png", confidence=0.9)
            print("coffeehouse ",coffee)
            pyautogui.click(coffee)
            pyautogui.moveTo(1200,573)
            time.sleep(delay_time)
        case ":fuelpump:":
            fuelpump = pyautogui.locateCenterOnScreen("img/g.png",confidence=0.9)
            print("gas ",fuelpump)
            pyautogui.click(fuelpump)
            pyautogui.moveTo(1200,573)
            time.sleep(delay_time)
        case ":spaghetti:":
            spaghetti = pyautogui.locateCenterOnScreen("img/i.png",confidence=0.9)
            print("italian restauran ",spaghetti)
            pyautogui.click(spaghetti)
            pyautogui.moveTo(1200,573)
            time.sleep(delay_time)
        case ":ferris_wheel:":
            ferris_wheel = pyautogui.locateCenterOnScreen("img/fair.png", confidence=0.85)
            print("fun fair ",ferris_wheel)
            pyautogui.click(ferris_wheel)
            pyautogui.moveTo(1200,573)
            time.sleep(delay_time)
        case ":taco:":
            taco = pyautogui.locateCenterOnScreen("img/t.png", confidence=0.9)
            print("taco ",taco)
            pyautogui.click(taco)
            pyautogui.moveTo(1200,573)
            time.sleep(delay_time)
        case ":tropical_drink:":
            tropical_drink = pyautogui.locateCenterOnScreen("img/n.png", confidence=0.9)
            print("night club ",tropical_drink)
            pyautogui.click(tropical_drink) 
            pyautogui.moveTo(1200,573)
            time.sleep(delay_time)
        case ":performing_arts:":
            performing_arts = pyautogui.locateCenterOnScreen("img/theater.png", region=(433,577,500,220), confidence=0.9)
            print("theater ",performing_arts)
            pyautogui.click(performing_arts)
            pyautogui.moveTo(1200,573)
            time.sleep(delay_time)
        case ":beverage_box:":
            beverage_box = pyautogui.locateCenterOnScreen("img/j.png", region=(433,577,500,220), confidence=0.9)
            print("juice ",beverage_box)
            pyautogui.click(beverage_box)
            pyautogui.moveTo(1200,573)
            time.sleep(delay_time)
        case ":dancer:":
            dancer = pyautogui.locateCenterOnScreen("img/b.png", confidence=0.9)
            print("ballroom ",dancer)
            pyautogui.click(dancer)
            pyautogui.moveTo(1200,573)
            time.sleep(delay_time)
        case ":shopping_bags:":
            shopping_bags = pyautogui.locateCenterOnScreen("img/mall.png", confidence=0.9)
            print("shopping mall ",shopping_bags)
            pyautogui.click(shopping_bags)
            pyautogui.moveTo(1200,573)
            time.sleep(delay_time)
        case ":ring:":
            ring = pyautogui.locateCenterOnScreen("img/ring.png", confidence=0.9)
            print("ring ",ring)
            pyautogui.click(ring) 
            pyautogui.moveTo(1200,573)
            time.sleep(delay_time)
        case ":airplane:":
            airplane = pyautogui.locateCenterOnScreen("img/plane.png", confidence=0.9)
            print("airplane ",airplane)
            pyautogui.click(airplane)
            pyautogui.moveTo(1200,573)
            time.sleep(delay_time)
        case ":house:":
            house = pyautogui.locateCenterOnScreen("img/home.png", confidence=0.9)
            print("home ",house)
            pyautogui.click(house)
            pyautogui.moveTo(1200,573)
            time.sleep(delay_time)
        case _:
            print("error emoji ",direction)
            pyautogui.alert('emoji "'+direction+'" does not exists')
            break

pyautogui.alert('date-solver map DONE')
