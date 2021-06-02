# NonMouse
指で動かす実態のないマウス

Webカメラで自分の手元を写すことで、あたかも実態のないマウスが出来上がっているかのように見えるプログラムです。  

## Installation
### 1. Install Mediapipe　　
以下の公式ドキュメントに従って、Mediapipeのインストール  
https://google.github.io/mediapipe/getting_started/install.html#installing-on-macos

### 2. Install pynput
```sh:Install
% pip install pynput  
```
macの場合、システム環境設定からセキリュティとプライバシーのアクセシビリティの項目にターミナルやVScodeなど、実行する場所を追加する必要があります。

## Usage
### run
NonMouseフォルダーをダウンロード、解凍する。
```sh
% cd ~/.../NonMouse
% python3 app.py
```

### hands movement
* 人差し指の先端がマウスカーソルに対応。

* 人指し指の指先と中指の指先をつけると、マウスカーソルの動きが止まる。

* 親指の指先と人差し指の第２関節をくっつけると左クリック、離すと左クリックのリリース

### quit
Ctrl+CかEscを押してください
