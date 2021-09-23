# NonMouse

これは、手そのものをマウスとして使うことができるアプリケーションです。  
このプログラムは、webカメラで手を認識して、マウスカーソルを操作します。  

動作状況は[Youtube](https://youtu.be/ufvOJUTCF8M)にも公開しています。  

![github_e](https://user-images.githubusercontent.com/22733958/129839012-82915bcf-10a5-49d1-8e03-e4f0def7b778.gif)  

グローバルホットキーにより、プログラムが非アクティブでも、マウスカーソルが動かせるのはwindowsのみです。linux, macはその機能をサポートしていません。

# インストール
## 1. 実行可能形式ファイルとして実行
最新のリリースから自分の環境に合ったZIPファイルをダウンロードしてください。
windows, mac版があります。
<img width="1164" alt="スクリーンショット 2021-09-13 午後5 33 21" src="https://user-images.githubusercontent.com/22733958/133051109-28f82312-5090-4431-a743-954a9c8cfe3c.png">


## 2. pythonファイルとして実行
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
共通部分
```sh
# その他パッケージインストール 
$ git clone https://github.com/takeyamayuki/NonMouse
$ cd NonMouse
$ pip install -r requirements.txt
```
※ macの場合、システム環境設定からセキリュティとプライバシーのアクセシビリティとカメラの項目にターミナルやVScodeなど、実行する場所を追加する必要があります。

# 使い方
## 実行
- [GitHub wiki](https://github.com/takeyamayuki/NonMouse/wiki/How-to-run-a--NonMouse-executable-file-in-each-OS#%E6%97%A5%E6%9C%AC%E8%AA%9E)の通りに実行可能ファイルを実行

- もしくは、インストールの続きから、以下のスクリプトを実行
   ```sh
   $ python3 app.py
   ```
   
   mac,linuxの場合は、グローバルホットキーなし（常に動く）の機能が削減されたapp-s.pyを起動してください。
   ```sh
   $ python3 app-s.py
   ```

## 設定
実行すると、以下の画面が出ます。この画面でカメラ、感度の設定をします。

   ![image](https://user-images.githubusercontent.com/22733958/133983075-48f5c72a-a3a8-4d1d-bd0b-d29b01d255ca.png)

- Camera  
カメラデバイスを選択してください。複数カメラが接続されている場合は、小さい番号から、順番に試してみてください。

   なるべく画質の良いカメラを使うことを推奨します。  

   置き方は以下の3通りを想定しています。

   - 自分に向ける
      - ノートパソコンの内蔵カメラやwebカメラを自分に向ける  
      - 手のひらをカメラに向ける
      - 俯瞰
         
   - 自分の手元に向ける  
      - webカメラの向き  
         <img width="500" alt="スクリーンショット 2021-09-13 午後5 33 21" src="https://user-images.githubusercontent.com/22733958/134124093-51c85b18-3d90-4935-8daa-a78761d1aaed.jpg">  
      - 手の甲をカメラに向ける
      - 俯瞰
           
   - ディスプレイに向ける  
      - webカメラの向き  
         <img width="500" alt="スクリーンショット 2021-09-13 午後5 33 21" src="https://user-images.githubusercontent.com/22733958/134123691-19eb8a76-8f01-497d-b09b-ea93e72825d5.jpg">  
      - 手の甲をカメラに向ける
      - 俯瞰
          

- Sensitivity  
感度を設定します。あまり大きくしすぎると、マウスカーソルが小刻みに揺れます。

設定が終わったら、continueをクリックしてください。すると、カメラの映像が映し出され、選択した設定でNonMouseが使えるようになります。

## 手の動き
右手のみサポートしています。  
以下の手の動きをAltを押している時だけ有効になります。ウィンドウがアクティブになっていなくても使えます。(この機能はwindowsのみ使えます)

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
windows,linuxでは、閉じるボタンで終了できます  macではEscキーで終了してください。
