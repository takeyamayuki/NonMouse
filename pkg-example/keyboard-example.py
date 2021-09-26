import keyboard
hotkey='F4'

while True:
    keyboard.wait(hotkey)
    print('hotkey was pressed! Waiting on it again...')


# while True:
#     if keyboard.is_pressed(hotkey):
#         print('hotkey was pressed! Waiting on it again...')