from django.shortcuts import render
from django.http import HttpResponse
import pyautogui
import time

def home(request):
    return render(request, 'auto/home.html', {'title': 'Home'})

def usage(request):
    time.sleep(1)

    position = pyautogui.position()
    print(position)
    pyautogui.moveTo(position.x+100,position.y, duration = 0.25)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click(918,40)
    time.sleep(1)
    pyautogui.click(1050,40)
    time.sleep(1)
    pyautogui.click(800,40)
    pyautogui.move(0,100, duration = 0.25)
    for i in range(5):
        pyautogui.scroll(200)
    return render(request, 'auto/usage.html')