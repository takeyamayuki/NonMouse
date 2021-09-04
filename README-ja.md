# NonMouse

Webカメラで自分の手元を写すことで、あたかも実体のないマウスがあるかのように見えるPythonスクリプトです。     
動作状況は[Youtube](https://youtu.be/ufvOJUTCF8M)にも公開しています。  
(感度調整なしのver.1は[こちら](https://github.com/takeyamayuki/NonMouse))   

![github_drug](https://user-images.githubusercontent.com/22733958/129838994-f1499648-a179-4e0d-a62f-a4d983ba380a.gif)  

![github_e](https://user-images.githubusercontent.com/22733958/129839012-82915bcf-10a5-49d1-8e03-e4f0def7b778.gif)  


# インストール

以下のスクリプトを実行します。
mediapipeのインストールだけ、OS毎に異なります。困ったら、[公式サイト](https://google.github.io/mediapipe/getting_started/install.html)を見てください。macとlinuxのやり方は、以下に示します。  
mac
```sh
# mediapipeのインストール
$ brew install bazelisk 
$ git clone https://github.com/google/mediapipe.git 
$ cd mediapipe 
$ brew install opencv@3 
$ brew uninstall --ignore-dependencies glog 
```
linux
```sh
# mediapipeのインストール
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
共通部分+実行
```sh
# その他パッケージインストール 
$ git clone https://github.com/takeyamayuki/NonMouse
$ cd NonMouse
$ pip install -r requirements.txt
# 実行
$ python3 app.py
```
※ macの場合、システム環境設定からセキリュティとプライバシーのアクセシビリティの項目にターミナルやVScodeなど、実行する場所を追加する必要があります。

# 使い方
### 実行
インストールの続きから、以下のスクリプトを実行
```sh
$ python3 app.py
```
実行すると、以下の画面が出ます。

<img width="412" alt="スクリーンショット 2021-09-04 午後7 03 24" src="https://user-images.githubusercontent.com/22733958/132090867-c705311a-e078-4114-be52-4991cf478da0.png">

- Camera：カメラデバイスを選択してください。複数カメラが接続されている場合は、小さい番号から、順番に試してみてください。  

- Mode：Normalモードと、Touchモードがあります。Touchモードは開発中です。Normalモードを使用してください。  

- Direction：webカメラの上下方向が逆になる場合、Invertを選択してください。たとえば、webカメラを下に向けて、webカメラの下と自分の手の下が逆になる場合はInvertを選択します。ノートパソコンのフロントカメラを使用する場合は、Normalです。

- Sensitivity：感度を設定します。あまり大きくしすぎると、マウスカーソルが小刻みに揺れるので、デフォルトの状態が最良です。

設定が終わったら、continueをクリックしてください。すると、選択した設定でNonMouseが使えるようになります。

<img width="1392" alt="スクリーンショット 2021-09-04 午後7 28 46" src="https://user-images.githubusercontent.com/22733958/132091539-c897226a-9d60-4344-88a1-cb87d7ab64b4.png">


### 手の動き
* カーソル
   * マウスカーソル: 人差し指の先端  
   * マウスカーソルの動きを止める: 人指し指の指先と中指の指先をくっつける   
* 左クリック
   * 左クリック: 親指の指先と人差し指の第２関節をくっつける
   * 左クリックのリリース: 親指の指先と人差し指の第２関節を離す  
   * ダブルクリック: 左クリックを0.5秒以内に2回行う
* その他
   * 右クリック: カーソルを動かさずに、クリック状態を１秒続ける
   * スクロール: 人差し指を90°回転させて横にした状態で人差し指でスクロール

### プログラムの止め方
ターミナルウィンドウがアクティブのとき、Ctrl+C  
アプリケーションウィンドウがアクティブのときは、Escを押してください  
