import pyautogui, time
time.sleep(5)
f = open("kalimat", "r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
  
