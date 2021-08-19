# NonMouse
日本語のREADMEは[こちら](README-ja.md)  

This is a Python script that uses a web camera to capture your hand, making it appear as if there is a mouse without any substance.   
It is mainly intended to be used as a cheap alternative to liquid tabs and board tabs when drawing.    
The operation status is also available on [Youtube](https://youtu.be/ufvOJUTCF8M)  
(Ver.1 without sensitivity adjustment is [here](https://github.com/takeyamayuki/NonMouse))  


![github_drug](https://user-images.githubusercontent.com/22733958/129838867-e5b28dfc-3e7c-4064-9d17-93e24e7f7064.gif)

![github_e](https://user-images.githubusercontent.com/22733958/129838897-86da6861-b3a5-4e14-98fe-400a27c894d7.gif)


# Installation

### Install as usual
```sh
$ git clone https://github.com/takeyamayuki/NonMouse
$ cd NonMouse
$ pip install -r requirements.txt    # Install packages from requirements.txt   
```
### If you don't want to pollute your local environment
```sh
$ git clone https://github.com/takeyamayuki/NonMouse
$ cd NonMouse
$ . NonMouse/bin/activate           # Enter the virtual environment. 
```
Exit the virtual environment with `$ deactivate`.  

※ For mac, you need to add the location where you want to run it, such as Terminal or VScode, to the Security and Privacy Accessibility section in System Preferences.

# Usage
### Run
From the continuation of the installation, run the following script.
```sh
$ python3 app.py
```
or
```sh
$ chmod 755 *.sh                    # Authorize Execution of .sh file
$ ./launch.sh                       # Run a shell script
```
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
    * Scrolling: If you put your middle and ring fingers together, you can use your index finger to scroll like on a smartphone.

### Arguments
* If you have more than one camera installed, you can use `--device X` to select a camera (default 0,  0,1,2... can be selected)   
    ```sh
    $ python3 app.py --device 0
    ```
* Use `--direciton X` to specify the direction the mouse cursor moves in relation to the direction your finger moves (default 0,  0,1 can be selected).  
    * When using a web camera facing down: 0     
    * When using the camera that comes with the laptop: 1
    ```sh
    $ python3 app.py --direction 0
    ```
* Define the touch distance with `--distance X` (the further the distance, the smaller the value, the closer the distance, the larger the value) (default 65, can be selected as an integer)   
[Approximate].
    * When the distance between the web camera and your hand is 50cm, 65
    * When the distance between the webcam and your hand is 110cm, 50
    ```sh
    $ python3 app.py --distance 50
    ```
* Define the mouse sensitivity with `--kando X` (don't make it too large because it will shake in small increments if you make it too large) (default 1.5, selectable in decimal fraction)  
[Approximate].
    * 1.5 when the distance between the web camera and your hand is 50cm.
    * When the distance between the webcam and your hand is 110cm, 5
    ```sh
    $ python3 app.py --kando 5
    ```
I have put these arguments into a shell script so that they can be specified together.  
```sh
$ chmod 755 *.sh                    # Authorize Execution of .sh file
$ ./launch.sh                       # Run a shell script
```
You can also run launch-ceiling.sh and launch-frcam.sh in the same way.
* [launch-frcam.sh](launch-frcam.sh) is a script to use a laptop web camera  
* [launch-ceiling.sh](launch-ceiling.sh) is a script to use a ceiling-mounted webcam.
### Stop a program
Press Ctrl+C, when a terminal window is active.     
Press Esc, when an application window is active.    
