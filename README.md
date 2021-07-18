# NonMouse2
日本語のREADMEは[こちら](README-ja.md)  

Insubstantial mouse moved by finger.      
![nonmouse twi drug-アニメーションイメージ（大）](https://user-images.githubusercontent.com/22733958/121180947-7054ef80-c89c-11eb-9c7a-42a9e1f3f02a.gif)  
![nonmouse twi21 oe-アニメーションイメージ（大）](https://user-images.githubusercontent.com/22733958/121180967-75b23a00-c89c-11eb-82fa-4f5d9abda320.gif)  


This is a Python script that uses a web camera to capture your hand, making it appear as if there is a mouse without any substance. (Ver.1 without sensitivity adjustment is [here](https://github.com/takeyamayuki/NonMouse))  
The operation status is also available on [Youtube](https://youtu.be/ufvOJUTCF8M)

# Installation
### Install Mediapipe  
Follow the [official documentation](https://google.github.io/mediapipe/getting_started/install.html#installing-on-macos) to install Mediapipe.

### Install pynput
```sh:Install
% pip install pynput  
```
For mac, you need to add the location where you want to run it, such as Terminal or VScode, to the Security and Privacy Accessibility section in System Preferences.

# Usage
### Run
Download the NonMouse folder, unzip it, and run the following script
```sh
% cd ~/.../NonMouse2-main
% python3 app.py
```
### Hand Movements
* The tip of the index finger corresponds to the mouse cursor.  
* Attaching the fingertips of the index finger and the middle finger stops the mouse cursor from moving.  
* Attaching the fingertip of the thumb to the second joint of the index finger releases the left click, releasing it releases the left click  
* Scrolling and right-clicking are not implemented yet.

### Args
* If you have more than one camera installed, you can use `--device X` to select a camera (default 0,  0,1,2... can be selected)   
    ```sh
    % python3 app.py --device 0
    ```
* Use `--direciton X` to specify the direction the mouse cursor moves in relation to the direction your finger moves (default 0,  0,1 can be selected).  
    * When using a web camera facing down: 0     
    * When using the camera that comes with the laptop: 1
    ```sh
    % python3 app.py --direction 0
    ```
* Define the touch distance with `--distance X` (the further the distance, the smaller the value, the closer the distance, the larger the value) (default 65, can be selected as an integer)   
[Approximate].
    * When the distance between the web camera and your hand is 50cm, 65
    * When the distance between the webcam and your hand is 110cm, 50
    ```sh
    % python3 app.py --distance 50
    ```
* Define the mouse sensitivity with `--kando X` (don't make it too large because it will shake in small increments if you make it too large) (default 1.5, selectable in decimal fraction)  
[Approximate].
    * 1.5 when the distance between the web camera and your hand is 50cm.
    * When the distance between the webcam and your hand is 110cm, 5
    ```sh
    % python3 app.py --kando 5
    ```
We have put these arguments into a shell script so that they can be specified together.  
* [launch-frcam.sh](launch-frcam.sh) is a script to use a laptop web camera  
* [launch-ceiling.sh](launch-ceiling.sh) is a script to use a ceiling-mounted webcam.
```sh
% cd ~/.../NonMouse2-main
% chmod 755 launch-frcam.sh
% chmod 755 launch-ceiling.sh
% chmod 755 launch.sh
```
Drag the .sh file to the terminal and enter    
### Stop a program
When a terminal window is active, press Ctrl+C    
When an application window is active, press Esc    