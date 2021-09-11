# NonMouse

Webカメラで自分の手元を写すことで、あたかも実体のないマウスがあるかのように見えるPythonスクリプトです。     
動作状況は[Youtube](https://youtu.be/ufvOJUTCF8M)にも公開しています。  


![github_e](https://user-images.githubusercontent.com/22733958/129839012-82915bcf-10a5-49d1-8e03-e4f0def7b778.gif)  


# インストール
実行可能形式ファイルをリリースしました。
## 1.実行可能形式ファイルとして実行
### Windows

### Mac
<img width="410" alt="スクリーンショット 2021-09-11 午後11 45 35" src="https://user-images.githubusercontent.com/22733958/132951664-d442bc2f-dad9-4f85-880f-1277ef5a3ec1.png">
を実行。すると、以下の画面が出るので、OKをクリック
<img width="372" alt="スクリーンショット 2021-09-11 午後11 56 39" src="https://user-images.githubusercontent.com/22733958/132952245-36befc8c-d751-4665-980e-a2fd2d5c2424.png">
次に、システム環境設定から「セキリュティとプライバシー」の「一般」の項目を開いて、一番下の「このまま開く」をクリック
<img width="780" alt="スクリーンショット 2021-09-11 午後11 56 56" src="https://user-images.githubusercontent.com/22733958/132952272-0850fcd2-498a-45dd-a046-257742ff2adb.png">
以下の画面が出るので、「開く」をクリック
<img width="372" alt="スクリーンショット 2021-09-11 午後11 57 08" src="https://user-images.githubusercontent.com/22733958/132952293-72de3d98-4164-425e-a479-d2b423d4e428.png">

これでも、アプリがカメラとマウスカーソルにアクセスできないので、システム環境設定から「セキリュティとプライバシー」の「プライバシー」で、「アクセシビリティ」と「カメラ」の項目において、以下のようにターミナルを追加。
<img width="780" alt="スクリーンショット 2021-09-12 午前0 02 20" src="https://user-images.githubusercontent.com/22733958/132952303-60625f12-ab31-4480-a0f9-31e5bb302333.png">
<img width="780" alt="スクリーンショット 2021-09-12 午前0 02 31" src="https://user-images.githubusercontent.com/22733958/132952309-e400f479-c082-456f-a82c-bd71f5ba15a9.png">
最初に、以上の手順を踏めば次からはクリックだけで実行できます。

### Linux

## 2.pythonファイルとして実行
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
## 実行
インストールの続きから、以下のスクリプトを実行
```sh
$ python3 app.py
```

実行すると、以下の画面が出ます。  
以下の画面でまずはカメラ、感度、モードの設定をします。

<img width="392" alt="スクリーンショット 2021-09-11 午後0 04 57" src="https://user-images.githubusercontent.com/22733958/132934634-581a47f7-7539-47f3-9dfd-272b383981b3.png">

- Mode  
Gesture, Mouse, Touchモードがあります。
   - Gesture  
      - webカメラを自分に向ける or ノートパソコンの内蔵カメラを使用する。
      - カメラに向かって、ジェスチャーのようにNonMouseの[手の動き](#手の動き)をする。
      <img width="1392" alt="スクリーンショット 2021-09-11 午後0 25 43" src="https://user-images.githubusercontent.com/22733958/132934740-25641174-eefe-4b93-8bac-34c339a45b64.png">

      
   - Mouse  
      - webカメラを自分の手元に向ける。
      - 手元でNonMouseの[手の動き](#手の動き)をする。
      <img width="1392" alt="スクリーンショット 2021-09-11 午後0 28 23" src="https://user-images.githubusercontent.com/22733958/132934790-e870d88e-42de-4789-b200-ff54ce427cbc.png">


   - Touch    
      - webカメラをディスプレイに向ける。
      - ディスプレイ上で[手の動き](#手の動き)をすることで、タッチしているようにカーソルを動かせる。
      <img width="1392" alt="スクリーンショット 2021-09-11 午後0 01 17" src="https://user-images.githubusercontent.com/22733958/132934076-b65d4013-4f28-4376-b56c-349754a56501.png">

- Camera  
カメラデバイスを選択してください。複数カメラが接続されている場合は、小さい番号から、順番に試してみてください。  

- Sensitivity  
感度を設定します。あまり大きくしすぎると、マウスカーソルが小刻みに揺れます。
      

設定が終わったら、continueをクリックしてください。すると、上記のようなカメラの映像が映し出され、選択した設定でNonMouseが使えるようになります。

## 手の動き
* カーソル
   * マウスカーソル: 人差し指の先端 → 青色の円が人差し指の先端に表示される
   * マウスカーソルの動きを止める: 人指し指の指先と中指の指先をくっつける → 青色の円が消える
* 左クリック
   * 左クリック: 親指の指先と人差し指の第２関節をくっつける → 黄色の円が人差し指の先端に表示される
   * 左クリックのリリース: 親指の指先と人差し指の第２関節を離す → 黄色の円が消える
   * ダブルクリック: 左クリックを0.5秒以内に2回行う
* その他
   * 右クリック: カーソルを動かさずに、クリック状態を１秒続ける → 赤色の円が人差し指の先端に表示される
   * スクロール: 人差し指を90°回転させて横にした状態で人差し指でスクロール

† 手元を明るくして使ってください。  
† カメラに対して、なるべく手をまっすぐ向けてください。

## プログラムの止め方
ターミナルウィンドウがアクティブのとき、Ctrl+C  
アプリケーションウィンドウがアクティブのときは、Escを押してください  

† ウィンドウのバツを押しても消えません。
