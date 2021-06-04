# NonMouse2
指で動かす実体のないマウス

Webカメラで自分の手元を写すことで、あたかも実体のないマウスが出来上がっているかのように見えるプログラムです。  
[ver.1](https://github.com/takeyamayuki/NonMouse)  
動作状況は[Youtube](https://youtu.be/ufvOJUTCF8M)にも公開しています。

## Installation
### 1. Install Mediapipe  
[公式ドキュメント](https://google.github.io/mediapipe/getting_started/install.html#installing-on-macos)に従って、Mediapipeのインストール


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

* スクロールと右クリックについては未実装です 

### quit
Ctrl+CかEscを押してください
