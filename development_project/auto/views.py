from django.shortcuts import render
from django.http import HttpResponse
import pyautogui
import time

def home(request):
    return render(request, 'auto/home.html', {'title': 'Home'})

def usage(request):
    time.sleep(5)
    for _ in range(1):
        pyautogui.click(828,476)
        pyautogui.click(811,504)
        time.sleep(0.5)
        pyautogui.write("New Patient OK")

        pyautogui.click(886,547)
        time.sleep(0.5)
        pyautogui.click(878,621)
        pyautogui.click(1290,790)

    return render(request, 'auto/usage.html')