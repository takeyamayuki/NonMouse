# NonMouse
![GitHub](https://img.shields.io/github/license/takeyamayuki/nonmouse) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/takeyamayuki/nonmouse) ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/takeyamayuki/nonmouse) ![zenn](https://img.shields.io/badge/Zenn%20Likes-91-blue) 

日本語のREADMEは[こちら](README-ja.md)  

This is an application that allows you to use your hand itself as a mouse.  
The program uses a web camera to recognize your hand and control the mouse cursor.  

The video is available on [Youtube](https://youtu.be/ufvOJUTCF8M)   

![github_e](https://user-images.githubusercontent.com/22733958/129838897-86da6861-b3a5-4e14-98fe-400a27c894d7.gif)

Global hotkeys allow you to move the mouse cursor even when the program is inactive, but only on windows. linux and mac do not support this feature.

# Installation
## 1. Run as executable file. 
Download the zip file that matches your environment from the latest release. 

## 2. Run as python
Run the following script.

```sh
$ git clone https://github.com/takeyamayuki/NonMouse
$ cd NonMouse
$ pip install -r requirements.txt
```
If you have trouble installing mediapipe, please visit the [official website].  

※ For mac, you need to add the location where you want to run it, such as Terminal or VScode, to the Security and Privacy Accessibility and Cammera section in System Preferences.

# Usage
## 1. Install the camera
The following three ways of placing the device are assumed. If you place it in one of the following ways and put out your right hand, it will automatically recognize where it is placed.

- Point it at yourself (you can use your laptop's built-in camera).   
   | Example of installation methods|Point the palm of your hand at the camera|
   | :---: | :---: |
   | <img width="300" alt="スクリーンショット 2021-09-13 午後5 33 21" src="https://user-images.githubusercontent.com/22733958/134456824-79c1a447-2b06-4b98-ba28-d06b552606e2.jpg">　
   <img width="300" alt="スクリーンショット 2021-09-13 午後5 33 21" src="https://user-images.githubusercontent.com/22733958/134465166-3c324aef-0ee6-4dd9-9810-b723e945e748.jpg"> | ![スクリーンショット 2021-09-23 044041](https://user-images.githubusercontent.com/22733958/134456933-0c81812d-c23d-4e52-860e-2a341d5bbe3c.png) |
- Point it at your hand.  
   | Example of installation methods | Point the back of your hand at the camera. |
   | :---: | :---: |
   | <img width="300" alt="スクリーンショット 2021-09-13 午後5 33 21" src="https://user-images.githubusercontent.com/22733958/134124093-51c85b18-3d90-4935-8daa-a78761d1aaed.jpg"> | ![スクリーンショット 2021-09-23 044243](https://user-images.githubusercontent.com/22733958/134456961-755a2769-1d2d-4cca-8fbd-6b49c7b2c0b1.png) |

- Point it at the display.    
   | Example of installation methods | Point the back of your hand at the camera. |
   | :---: | :---: |
   | <img width="300" alt="スクリーンショット 2021-09-13 午後5 33 21" src="https://user-images.githubusercontent.com/22733958/134123691-19eb8a76-8f01-497d-b09b-ea93e72825d5.jpg"> | ![スクリーンショット 2021-09-23 044403](https://user-images.githubusercontent.com/22733958/134456968-aaf3660d-9ee2-45b8-b65a-9590a6aec4fe.png) |

## 2. Run
- Run the executable as described in the [GitHub wiki](https://github.com/takeyamayuki/NonMouse/wiki/How-to-run-a--NonMouse-executable-file-in-each-OS#%E6%97%A5%E6%9C%AC%E8%AA%9E).

- Or, from the continuation of the installation, run the following script
   ```sh
   $ python3 app.py
   ```
   
   For mac and linux, please run app-s.py without global hotkeys (it always works).
   ```sh
   $ python3 app-s.py
   ```

## 3. Settings
When you run the program, the following screen will appear. On this screen, you can set the camera and sensitivity.

![image](https://user-images.githubusercontent.com/22733958/133983075-48f5c72a-a3a8-4d1d-bd0b-d29b01d255ca.png)

- Camera  
Select a camera device. If multiple cameras are connected, try them in order, starting with the smallest number.
          
- Sensitivity  
Set the sensitivity. If set too high, the mouse cursor will shake slightly.

When you are done with the settings, click continue. The camera image will then be displayed, and you can use NonMouse with the settings you selected.

## 4. Hand Movements

| Activate | Cursor | Left Click | Right Click | Scroll |
| :---: | :---: |:---: |:---: |:---: |
|![](https://user-images.githubusercontent.com/22733958/134462214-af90785f-29fb-4230-a2b4-4618ee0b26dd.gif) | ![](https://user-images.githubusercontent.com/22733958/134462179-6bd5a666-92b4-4c87-a02e-711430dd5180.gif)| ![](https://user-images.githubusercontent.com/22733958/134462244-e2a4e47e-d183-44b9-ace5-b771b063289c.gif)| ![](https://user-images.githubusercontent.com/22733958/134462268-90a07833-4ecc-4b29-85c6-6925f106cbc2.gif) | ![](https://user-images.githubusercontent.com/22733958/134462278-a857012e-76a6-4abd-bdc3-53664c8cf643.gif) |

Only the right hand is supported.  
The following hand movements are enabled only when you hold down Alt. They can be used even if no window is active. (This feature is only available on windows).
On mac, linux, the cursor is always moving. 

- cursor
    * Mouse cursor: tip of index finger → A blue circle will appear at the tip of your index finger. 
    * Stop mouse cursor: Attach the tip of your index finger to the tip of your middle finger. → The blue circle disappears.
- left click
    * Left click: Attach the fingertips of your thumb to the second joint of your index finger → A yellow circle will appear on the tip of your index finger.
    * Left click release: Release the thumb fingertip and the second joint of the index finger. → The yellow circle disappears.
    * Double click: Left click twice within 0.5 seconds.
- other
    * Right click: Hold the click state for 1.5 second without moving the cursor. → A red circle will appear at the tip of your index finger.
    * Scroll: Scroll with the index finger with the index finger folded → a black circle will appear. 

† Use it with a bright light at hand.
† Keep your hand as straight as possible to the camera.

## 5. Stop the application
Press Ctrl+C, when a terminal window is active.     
Press close button(Valid only on windows, linux) or Esc key, when an application window is active.   
