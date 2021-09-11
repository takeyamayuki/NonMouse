# NonMouse
日本語のREADMEは[こちら](README-ja.md)  

This is a Python script that uses a web camera to capture your hand, making it appear as if there is a mouse without any substance.     
The operation status is also available on [Youtube](https://youtu.be/ufvOJUTCF8M)   

![github_e](https://user-images.githubusercontent.com/22733958/129838897-86da6861-b3a5-4e14-98fe-400a27c894d7.gif)


# Installation
## 1.Run as executable file. 
Download the binary that matches your OS from the release. Then unzip it and follow the steps below.
### Windows
![image](https://user-images.githubusercontent.com/22733958/132952932-a0001c1b-b28b-44be-a7bd-30755ae8ca94.png)  
Run NonMouse.exe

### Mac  
<img width="400" alt="スクリーンショット 2021-09-12 午前0 21 58" src="https://user-images.githubusercontent.com/22733958/132952856-21526499-14c0-4548-8b9d-17235373bfd0.png">    

Run NonMouse, then the following screen will appear, click OK.  
<img width="372" alt="スクリーンショット 2021-09-11 午後11 56 39" src="https://user-images.githubusercontent.com/22733958/132952245-36befc8c-d751-4665-980e-a2fd2d5c2424.png">  

Next, go to System Preferences, go to "Security and Privacy," open the "General" section, and click "Open As..." at the bottom.  
<img width="780" alt="スクリーンショット 2021-09-11 午後11 56 56" src="https://user-images.githubusercontent.com/22733958/132952272-0850fcd2-498a-45dd-a046-257742ff2adb.png">  

When the following screen appears, click "Open".  
<img width="372" alt="スクリーンショット 2021-09-11 午後11 57 08" src="https://user-images.githubusercontent.com/22733958/132952293-72de3d98-4164-425e-a479-d2b423d4e428.png">  

This still doesn't allow the app to access the camera and mouse cursor, so I went to System Preferences and under "Privacy" in "Security and Privacy", in the "Accessibility" and "Camera" sections, I added a terminal as shown below.  

<img width="780" alt="スクリーンショット 2021-09-12 午前0 02 20" src="https://user-images.githubusercontent.com/22733958/132952303-60625f12-ab31-4480-a0f9-31e5bb302333.png">  
<img width="780" alt="スクリーンショット 2021-09-12 午前0 02 31" src="https://user-images.githubusercontent.com/22733958/132952309-e400f479-c082-456f-a82c-bd71f5ba15a9.png">    
The first step is to follow the instructions above, and the next is just a click away.  

### Linux
![Screenshot from 2021-09-12 00-36-46](https://user-images.githubusercontent.com/22733958/132953337-cf808fd8-0bf6-4cbc-9b9f-fb80268bd060.png)  
Run NonMouse in the folder. However, at the moment, it only gives about 10 fps, so I recommend running it as python.
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
From the continuation of the installation, run the following script.
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
