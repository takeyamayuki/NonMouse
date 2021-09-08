# NonMouse
日本語のREADMEは[こちら](README-ja.md)  

This is a Python script that uses a web camera to capture your hand, making it appear as if there is a mouse without any substance.     
The operation status is also available on [Youtube](https://youtu.be/ufvOJUTCF8M)  
(Ver.1 without sensitivity adjustment is [here](https://github.com/takeyamayuki/NonMouse))  


![github_drug](https://user-images.githubusercontent.com/22733958/129838867-e5b28dfc-3e7c-4064-9d17-93e24e7f7064.gif)

![github_e](https://user-images.githubusercontent.com/22733958/129838897-86da6861-b3a5-4e14-98fe-400a27c894d7.gif)


# Installation
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
From the continuation of the installation, run the following script.
```sh
$ python3 app.py
```
When you run it, you will see the following screen.  
In the following screen, you will first set the camera, sensitivity, and mode.

<img width="392" alt="スクリーンショット 2021-09-08 午後8 19 35" src="https://user-images.githubusercontent.com/22733958/132500418-569f03e8-7b18-454e-adf3-a896ed18333c.png">

- Camera  
Select your camera device. If you have multiple cameras connected, try them in order, starting with the smallest number.  

- Sensitivity  
Set the sensitivity. If you set it too high, the mouse cursor will wiggle.

- Mode  
There are Gesture, Mouse, and Touch modes.
    - Gesture    
        Point the web camera at yourself or use the built-in camera of your laptop.  
        Make NonMouse hand movements like a gesture toward the camera.
        <img width="1392" alt="スクリーンショット 2021-09-04 午後7 28 46" src="https://user-images.githubusercontent.com/22733958/132091539-c897226a-9d60-4344-88a1-cb87d7ab64b4.png">

    - Mouse    
        Point the web camera at your hand.  
        Make NonMouse hand movements with your hand.  
        <img width="1392" alt="スクリーンショット 2021-09-08 午後8 12 39" src="https://user-images.githubusercontent.com/22733958/132499605-17ec6cfb-6638-43bc-a3a7-6fb19f7b2428.png">
    - Touch: under development  
        Point the web camera at the display.  
        When you select this option, you will first be prompted to select the four corners of the display, and if you follow the instructions, the tip of your index finger will be recognized as the absolute position on the display.

When you are done with the settings, click continue. Then you can use NonMouse with the settings you selected.


### Hand Movements
- cursor
    * Mouse cursor: tip of index finger  
    * Stop mouse cursor: Attach the tip of your index finger to the tip of your middle finger  
- left click
    * Left click: Attach the fingertips of your thumb to the second joint of your index finger
    * Left click release: Release the thumb fingertip and the second joint of the index finger  
    * Double click: Left click twice within 0.5 seconds
- etc
    * Right click: Hold the click state for 1 second without moving the cursor
    * Scrolling: Scroll with your index finger while rotating your index finger 90° to the side.

### Stop a program
Press Ctrl+C, when a terminal window is active.     
Press Esc, when an application window is active.    
The window will not disappear even if you press the "X" button on the window.
