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
## 実行
インストールの続きから、以下のスクリプトを実行
```sh
$ python3 app.py
```

実行すると、以下の画面が出ます。  
以下の画面でまずはカメラ、感度、モードの設定をします。

<img width="392" alt="スクリーンショット 2021-09-08 午後8 19 35" src="https://user-images.githubusercontent.com/22733958/132500418-569f03e8-7b18-454e-adf3-a896ed18333c.png">

- Camera  
カメラデバイスを選択してください。複数カメラが接続されている場合は、小さい番号から、順番に試してみてください。  

- Sensitivity  
感度を設定します。あまり大きくしすぎると、マウスカーソルが小刻みに揺れます。

- Mode  
Gesture, Mouse, Touchモードがあります。
   - Gesture  
      - webカメラを自分に向ける or ノートパソコンの内蔵カメラを使用する。
      - カメラに向かって、ジェスチャーのようにNonMouseの[手の動き](#手の動き)をする。
      <img width="1392" alt="スクリーンショット 2021-09-04 午後7 28 46" src="https://user-images.githubusercontent.com/22733958/132091539-c897226a-9d60-4344-88a1-cb87d7ab64b4.png">
      
   - Mouse  
      - webカメラを自分の手元に向ける。
      - 手元でNonMouseの[手の動き](#手の動き)をする。
      <img width="1392" alt="スクリーンショット 2021-09-08 午後8 12 39" src="https://user-images.githubusercontent.com/22733958/132499605-17ec6cfb-6638-43bc-a3a7-6fb19f7b2428.png">

   - Touch:開発中  
      - webカメラをディスプレイに向ける。
      - これを選択すると、最初にディスプレイの四隅を選択する画面が出るので、指示に従うとディスプレイにおける自分の人差し指の先端が絶対的な位置として認識される。

設定が終わったら、continueをクリックしてください。すると、選択した設定でNonMouseが使えるようになります。

## 手の動き
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

## プログラムの止め方
ターミナルウィンドウがアクティブのとき、Ctrl+C  
アプリケーションウィンドウがアクティブのときは、Escを押してください  
※ウィンドウのバツを押しても消えません。
