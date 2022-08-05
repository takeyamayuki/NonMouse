<div align="center">
   <img src="https://user-images.githubusercontent.com/22733958/183041432-cf6cc6f4-3a6f-4070-91a8-d0a7f7abf59f.JPG" width="600">
</div>

<div align="center">
   Virtual gesture mouse with webcam for easy use with hands on desk  
</div>

<p align="center">
  <a href="https://github.com/takeyamayuki/NonMouse/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/takeyamayuki/nonmouse" />
  </a>
  <a href="https://github.com/takeyamayuki/NonMouse/releases">
    <img src="https://img.shields.io/github/v/release/takeyamayuki/nonmouse" />
  </a>
  <a href="https://zenn.dev/ninzin/articles/94b05fdb9edf53">
    <img src="https://img.shields.io/badge/Zenn%20Likes-102-blue" />
  </a>  
</p>

---

<table>
<tr>
<td><img src="https://user-images.githubusercontent.com/22733958/135473409-9ddf2fc5-4722-4e55-8eef-64476635c10d.gif"></td>
<td><img src="https://user-images.githubusercontent.com/22733958/129838897-86da6861-b3a5-4e14-98fe-400a27c894d7.gif"></td>
</tr>
</table>


# Feature
- No need for anything other than a webcam and host PC
- Gesture-based HCI has been around for some time, but shooting from above makes the mouse easier to use.
- NonMouse can be invoked by the global hotkey even when this application is inactive.
- Works well with typing.    
- Just download from the latest release (windows, mac only)  

# Installation
## 📁 Run as executable file 
Download the zip file that matches your environment from the [latest release](https://github.com/takeyamayuki/NonMouse/releases). 

OR
## 🐍 Run as python
Run the following script.

```sh
$ git clone https://github.com/takeyamayuki/NonMouse
$ cd NonMouse
$ pip install -r requirements.txt
```
If you have trouble installing mediapipe, please visit the [official website](https://google.github.io/mediapipe/getting_started/install.html).  

> **Note**   
> For mac, you need to add the location where you want to run it, such as Terminal or VScode, to the Security and Privacy Accessibility and Cammera section in System Preferences.

# Usage
## 1. Install a camera
The following three ways of placing the device are assumed.

- `Normal`: Place a webcam normally and point it at yourself (or use your laptop's built-in camera)   

   <table>
   <tr>
   <td><img width="300" alt="スクリーンショット 2021-09-13 午後5 33 21" src="https://user-images.githubusercontent.com/22733958/134465166-3c324aef-0ee6-4dd9-9810-b723e945e748.jpg"></td>
   <td><img width="300" alt="スクリーンショット 2021-09-13 午後5 33 21" src="https://user-images.githubusercontent.com/22733958/134456933-0c81812d-c23d-4e52-860e-2a341d5bbe3c.png"></td>
   </tr>
   </table>

- `Above`: Place it above your hand and point it towards your hand.  

   <table>
   <tr>
   <td><img width="300" alt="スクリーンショット 2021-09-13 午後5 33 21" src="https://user-images.githubusercontent.com/22733958/134124093-51c85b18-3d90-4935-8daa-a78761d1aaed.jpg"></td>
   <td><img width="300" alt="スクリーンショット 2021-09-13 午後5 33 21" src="https://user-images.githubusercontent.com/22733958/134456961-755a2769-1d2d-4cca-8fbd-6b49c7b2c0b1.png"></td>
   </tr>
   </table>

- `Behind`: Place it behind you and point it at the display.  

   <table>
   <tr>
   <td><img width="300" alt="スクリーンショット 2021-09-13 午後5 33 21" src="https://user-images.githubusercontent.com/22733958/134123691-19eb8a76-8f01-497d-b09b-ea93e72825d5.jpg"></td>
   <td><img width="300" alt="スクリーンショット 2021-09-13 午後5 33 21" src="https://user-images.githubusercontent.com/22733958/134456968-aaf3660d-9ee2-45b8-b65a-9590a6aec4fe.png"></td>
   </tr>
   </table>

## 2. Run
- Run the executable as described in the [GitHub wiki](https://github.com/takeyamayuki/NonMouse/wiki/How-to-run-a--NonMouse-executable-file-in-each-OS#%E6%97%A5%E6%9C%AC%E8%AA%9E).

   OR
-  Run the following script from the continuation of the installation.

   For windows, linux(global hotkey function does not work in linux.)
   ```sh
   $ python3 app.py
   ```

   For MacOS, you need execute permission.
   ```sh
   $ sudo /path/to/python3 app.py
   # When you invoke python with sudo, the system python is invoked, so you must specify the python you want to run yourself.
   ```

## 3. Settings
When you run the program, You will see a screen similar to the following. On this screen, you can set the camera and sensitivity.

![スクリーンショット 2021-12-02 154251](https://user-images.githubusercontent.com/22733958/144371606-d6b8cb07-f376-4097-95c3-c6cd7b3141ca.png)

- `Camera`  
Select a camera device. If multiple cameras are connected, try them in order, starting with the smallest number.

- `How to place`  
Select the location where you placed the camera. Place the camera in one of the following positions: `Normal`, `Above`, `Behind` in [📷 Install a Camera].

- `Sensitivity`  
Set the sensitivity. If set too high, the mouse cursor will shake slightly.

When you are done with the settings, click continue. The camera image will then be displayed, and you can use NonMouse with the settings you selected.

## 4. Hand Movements

| stop cursor | left click | right click | scroll |
| :---: |:---: |:---: |:---: |
| <img width="300" alt="aaa" src="https://user-images.githubusercontent.com/22733958/146399363-d90dbef0-0972-46b4-a03b-a76a6c97222f.gif">|<img width="300" alt="aaa" src="https://user-images.githubusercontent.com/22733958/146399342-d3ccb518-5950-4c69-aad4-c6fc9ad4a378.gif"> |<img width="300" alt="aaa" src="https://user-images.githubusercontent.com/22733958/146399353-0fb9304d-4f6c-4e5d-890c-0beb1dc921d2.gif"> | <img width="300" alt="aaa" src="https://user-images.githubusercontent.com/22733958/146399372-6551c367-5424-45a1-a963-c475c7ea895a.gif"> |

 
The following hand movements are enabled only when you hold down `Alt`(Windows), `Command`(MacOS). You can define your own global hotkeys by rewriting [here](https://github.com/takeyamayuki/NonMouse/blob/578afd6a7206258b68327421f64370c4009dedfd/app.py#L16-L21). You can use this function even if the window is not active.This feature is only available on windows and mac.  

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

> **Note**
> - Use it with a bright light at hand.  
> - Keep your hand as straight as possible to the camera.

## 5. Quit
Press Ctrl+C, when a terminal window is active.     
Press close button(Valid only on windows, linux) or Esc key, when an application window is active.   

# Build
> **Note**  
> The built binary files can be downloaded from latest realease.


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
