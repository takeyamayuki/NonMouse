# NonMouse
日本語のREADMEは[こちら](README-ja.md)  

This is a Python script that uses a web camera to capture your hand, making it appear as if there is a mouse without any substance.     
The operation status is also available on [Youtube](https://youtu.be/ufvOJUTCF8M)   

![github_e](https://user-images.githubusercontent.com/22733958/129838897-86da6861-b3a5-4e14-98fe-400a27c894d7.gif)


# Installation
## 1.Run as executable file. 
See the wiki [here](https://github.com/takeyamayuki/NonMouse/wiki/How-to-run-a--NonMouse-executable-file-in-each-OS)

## 2.Run as python
Run the following script.
Only the installation of mediapipe is different for each OS. If you have trouble, see the [official site](https://google.github.io/mediapipe/getting_started/install.html). The mac and linux instructions are shown below.   

mac
```sh
# install mediapipe
$ brew install bazelisk 
$ git clone https://github.com/google/mediapipe.git 
$ cd mediapipe 
$ brew install opencv@3 
$ brew uninstall --ignore-dependencies glog 
```
linux
```sh
# install mediapipe
$ sudo apt install nodejs 
$ sudo apt install npm 
$ sudo npm install -g @bazel/bazelisk 
$ cd $HOME
$ git clone https://github.com/google/mediapipe.git 
$ cd mediapipe 
$ sudo apt-get install -y \ 
    libopencv-core-dev \ 
    libopencv-highgui-dev \ 
    libopencv-calib3d-dev \ 
    libopencv-features2d-dev \ 
    libopencv-imgproc-dev \ 
    libopencv-video-dev 
```
Common part + run
```sh
# install other packages 
$ git clone https://github.com/takeyamayuki/NonMouse
$ cd NonMouse
$ pip install -r requirements.txt
# run
$ python3 app.py
```

※ For mac, you need to add the location where you want to run it, such as Terminal or VScode, to the Security and Privacy Accessibility section in System Preferences.

# Usage
### Run

- Follow the [wiki](https://github.com/takeyamayuki/NonMouse/wiki/How-to-run-a--NonMouse-executable-file-in-each-OS) to run the executable file.

- Or, run the following script, from the continuation of the installation.
    ```sh
    $ python3 app.py
    ``` 

When you run it, you will see the following screen.  
In the following screen, you will first set the camera, sensitivity, and mode.

<img width="392" alt="スクリーンショット 2021-09-11 午後0 04 57" src="https://user-images.githubusercontent.com/22733958/132934634-581a47f7-7539-47f3-9dfd-272b383981b3.png">

- Mode  
There are Gesture, Mouse, and Touch modes.
    - Gesture    
        - Point the web camera at yourself or use the built-in camera of your laptop.  
        - Make NonMouse hand movements like a gesture toward the camera.  

        <img width="1392" alt="スクリーンショット 2021-09-11 午後0 25 43" src="https://user-images.githubusercontent.com/22733958/132934740-25641174-eefe-4b93-8bac-34c339a45b64.png">

    - Mouse    
        - Point the web camera at your hand.  
        - Make NonMouse [hand movements](#HandMovements) with your hand.  
        
        <img width="1392" alt="スクリーンショット 2021-09-11 午後0 28 23" src="https://user-images.githubusercontent.com/22733958/132934790-e870d88e-42de-4789-b200-ff54ce427cbc.png">
    - Touch  
        - Point the web camera at the display.
        - You can move the cursor as if you were touching it by doing [hand movements](#HandMovements) on the display.

        <img width="1392" alt="スクリーンショット 2021-09-11 午後0 01 17" src="https://user-images.githubusercontent.com/22733958/132934076-b65d4013-4f28-4376-b56c-349754a56501.png">

- Camera  
Select your camera device. If you have multiple cameras connected, try them in order, starting with the smallest number.  

- Sensitivity  
Set the sensitivity. If you set it too high, the mouse cursor will wiggle.

When you are done with the settings, click continue. Then you can use NonMouse with the settings you selected.

### Hand Movements
- cursor
    * Mouse cursor: tip of index finger → A blue circle will appear at the tip of your index finger. 
    * Stop mouse cursor: Attach the tip of your index finger to the tip of your middle finger. → The blue circle disappears.
- left click
    * Left click: Attach the fingertips of your thumb to the second joint of your index finger → A yellow circle will appear on the tip of your index finger.
    * Left click release: Release the thumb fingertip and the second joint of the index finger. → The yellow circle disappears.
    * Double click: Left click twice within 0.5 seconds.
- etc
    * Right click: Hold the click state for 1 second without moving the cursor. → A red circle will appear at the tip of your index finger.
    * Scrolling: Scroll with your index finger while rotating your index finger 90° to the side.

† Use it with a bright light at hand.
† Keep your hand as straight as possible to the camera.
### Stop a program
Press Ctrl+C, when a terminal window is active.     
Press Esc, when an application window is active.  

† The window will not disappear even if you press the "X" button on the window.
