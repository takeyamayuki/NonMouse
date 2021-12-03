# NonMouse
![GitHub](https://img.shields.io/github/license/takeyamayuki/nonmouse) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/takeyamayuki/nonmouse) ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/takeyamayuki/nonmouse) ![zenn](https://img.shields.io/badge/Zenn%20Likes-93-blue) 

日本語のREADMEは[こちら](README-ja.md)  

This is an application that allows you to use your hand itself as a mouse.  
The program uses a web camera to recognize your hand and control the mouse cursor.  

The video is available on [Youtube](https://youtu.be/ufvOJUTCF8M)   

<img width="500" alt="スクリーンショット 2021-09-13 午後5 33 21" src="https://user-images.githubusercontent.com/22733958/135473409-9ddf2fc5-4722-4e55-8eef-64476635c10d.gif">

<img width="500" alt="スクリーンショット 2021-09-13 午後5 33 21" src="https://user-images.githubusercontent.com/22733958/129838897-86da6861-b3a5-4e14-98fe-400a27c894d7.gif">

# Feature
- Entirely new mouse: a mouse with a software approach. It recognizes your hand and works as a mouse.
- NonMouse can be invoked by the global hotkey even when this application is inactive.
- Works well with typing    
- You can make it look like a touch display, by pointing the web camera at the display. 
- You can use the mouse wherever you want.
- Just download from the latest release (windows, mac only)  

# Installation
## 📁 Run as executable file 
Download the zip file that matches your environment from the latest release. 

OR
## 🐍 Run as python
Run the following script.

```sh
$ git clone https://github.com/takeyamayuki/NonMouse
$ cd NonMouse
$ pip install -r requirements.txt
```
If you have trouble installing mediapipe, please visit the [official website](https://google.github.io/mediapipe/getting_started/install.html).  

† For mac, you need to add the location where you want to run it, such as Terminal or VScode, to the Security and Privacy Accessibility and Cammera section in System Preferences.

# Usage
## 📷 Install a camera
The following three ways of placing the device are assumed.

- `Normal`: Place a webcam normally and point it at yourself (or use your laptop's built-in camera)   
   | Examples of installation methods|Point the palm of your hand at the camera|
   | :---: | :---: |
   | <img width="300" alt="スクリーンショット 2021-09-13 午後5 33 21" src="https://user-images.githubusercontent.com/22733958/134456824-79c1a447-2b06-4b98-ba28-d06b552606e2.jpg"> 
   <img width="300" alt="スクリーンショット 2021-09-13 午後5 33 21" src="https://user-images.githubusercontent.com/22733958/134465166-3c324aef-0ee6-4dd9-9810-b723e945e748.jpg"> | ![スクリーンショット 2021-09-23 044041](https://user-images.githubusercontent.com/22733958/134456933-0c81812d-c23d-4e52-860e-2a341d5bbe3c.png) |
- `Above`: Place it above your hand and point it towards your hand.  
   | An example of installation methods | Point the back of your hand at the camera. |
   | :---: | :---: |
   | <img width="300" alt="スクリーンショット 2021-09-13 午後5 33 21" src="https://user-images.githubusercontent.com/22733958/134124093-51c85b18-3d90-4935-8daa-a78761d1aaed.jpg"> | ![スクリーンショット 2021-09-23 044243](https://user-images.githubusercontent.com/22733958/134456961-755a2769-1d2d-4cca-8fbd-6b49c7b2c0b1.png) |

- `Behind`: Place it behind you and point it at the display.    
   | An example of installation methods | Point the back of your hand at the camera. |
   | :---: | :---: |
   | <img width="300" alt="スクリーンショット 2021-09-13 午後5 33 21" src="https://user-images.githubusercontent.com/22733958/134123691-19eb8a76-8f01-497d-b09b-ea93e72825d5.jpg"> | ![スクリーンショット 2021-09-23 044403](https://user-images.githubusercontent.com/22733958/134456968-aaf3660d-9ee2-45b8-b65a-9590a6aec4fe.png) |

## 🚀 Run
- Run the executable as described in the [GitHub wiki](https://github.com/takeyamayuki/NonMouse/wiki/How-to-run-a--NonMouse-executable-file-in-each-OS#%E6%97%A5%E6%9C%AC%E8%AA%9E).

   OR
-  Run the following script from the continuation of the installation.

   For windows
   ```sh
   $ python3 app.py
   ```

   For MacOS, you need execute permission.
   ```sh
   $ sudo python3 app.py
   ```
   
   For linux, please run app-s.py without global hotkeys (it always works).
   ```sh
   $ python3 app-s.py
   ```

## 💻 Settings
When you run the program, You will see a screen similar to the following. On this screen, you can set the camera and sensitivity.

![スクリーンショット 2021-12-02 154251](https://user-images.githubusercontent.com/22733958/144371606-d6b8cb07-f376-4097-95c3-c6cd7b3141ca.png)

- `Camera`  
Select a camera device. If multiple cameras are connected, try them in order, starting with the smallest number.

- `How to place`  
Select the location where you placed the camera. Place the camera in one of the following positions: `Normal`, `Above`, `Behind` in [📷 Install a Camera].

- `Sensitivity`  
Set the sensitivity. If set too high, the mouse cursor will shake slightly.

When you are done with the settings, click continue. The camera image will then be displayed, and you can use NonMouse with the settings you selected.

## 👆 Hand Movements

| Activate | Cursor | Left Click | Right Click | Scroll |
| :---: | :---: |:---: |:---: |:---: |
|![](https://user-images.githubusercontent.com/22733958/134462214-af90785f-29fb-4230-a2b4-4618ee0b26dd.gif) | ![](https://user-images.githubusercontent.com/22733958/134462179-6bd5a666-92b4-4c87-a02e-711430dd5180.gif)| ![](https://user-images.githubusercontent.com/22733958/134462244-e2a4e47e-d183-44b9-ace5-b771b063289c.gif)| ![](https://user-images.githubusercontent.com/22733958/134462268-90a07833-4ecc-4b29-85c6-6925f106cbc2.gif) | ![](https://user-images.githubusercontent.com/22733958/134462278-a857012e-76a6-4abd-bdc3-53664c8cf643.gif) |

 
The following hand movements are enabled only when you hold down `Alt`(Windows), `Command`(MacOS). You can use this function even if the window is not active.This feature is only available on windows and mac.  
(On linux, use app-s.py which has this feature restricted. This is due to the fact that the [keyboard](https://github.com/boppreh/keyboard) does not work with `sudo` on linux. If anyone can get it to work, please report back at issue.)

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

## 🔚 Quit
Press Ctrl+C, when a terminal window is active.     
Press close button(Valid only on windows, linux) or Esc key, when an application window is active.   

# Build
† The built binary files can be downloaded from latest realease.


In app-mac.spec and app-win.spec, change `pathex` to fit your environment.   
Run the following scripts for each OS.  

- windows

   Copy and paste the location obtained by `pip show mediapipe` into `datas`, referring to what is written originally.  
   Run the following script.
   ```sh
   $ pip show mediapipe
   ...
   Location: c:\users\namik\appdata\local\programs\python\python37\lib\site_packages
   ...
   #Copy and paste into the datas in app-win.spec
   $ pyinstaller app-win.spec
   ... ````
- mac

   Create a venv environment and perform `pip install`, because the directory specified in `datas` is for an assumed venv environment. 
   ```sh 
   $ python3 -m venv venv
   $ . venv/bin/activate
   (venv)$ pip install -r requirements.txt
   (venv)$ pyinstaller app-mac.spec
   ```
