import pyautogui
from time import sleep as s

comment = input("What is the comment you want to send: ")
howmanytimes = input("How many times do u want to comment: ")

for i in range(int(howmanytimes)):
    # Commenting
    s(1) 
    pyautogui.click(1841,692)
    s(2)
    pyautogui.click(1461,913)
    pyautogui.write(comment, interval=0)
    s(1)
    pyautogui.click(1847,881)
    s(2)
    pyautogui.click(1849,516)
    s(1)

    # Scrolling
    pyautogui.scroll(-10)


