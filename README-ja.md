# NonMouse

これは、手そのものをマウスとして使うことができるアプリケーションです。  
このプログラムは、webカメラで手を認識して、マウスカーソルを操作します。 

動作状況は[Youtube](https://youtu.be/ufvOJUTCF8M)にも公開しています。

<img width="500" alt="スクリーンショット 2021-09-13 午後5 33 21" src="https://user-images.githubusercontent.com/22733958/135473409-9ddf2fc5-4722-4e55-8eef-64476635c10d.gif">

<img width="500" alt="スクリーンショット 2021-09-13 午後5 33 21" src="https://user-images.githubusercontent.com/22733958/129838897-86da6861-b3a5-4e14-98fe-400a27c894d7.gif">   

# 特徴
- 全く新しいマウス: ソフトウェアのアプローチによるマウスです。手を認識してマウスを動かします
- アプリケーションが非アクティブな状態でも、グローバルホットキーによりNonMouseを呼び出すことができる
- タイピングとの相性が良い  
- webカメラをディスプレイに向けることで、タッチディスプレイっぽくもできる
- 場所を選ばず、姿勢が自由
- 最新のリリースからダウンロードするだけで使える(windows, macのみ)

# インストール
## 📁 実行可能形式ファイルとして実行
最新のリリースから自分の環境に合ったZIPファイルをダウンロードしてください。

もしくは、
## 🐍 pythonファイルとして実行
以下のスクリプトを実行します。
```sh
$ git clone https://github.com/takeyamayuki/NonMouse
$ cd NonMouse
$ pip install -r requirements.txt
```
mediapipeのインストールで困ったら[公式サイト](https://google.github.io/mediapipe/getting_started/install.html)を見てください。

† macの場合、システム環境設定からセキリュティとプライバシーのアクセシビリティとカメラの項目にターミナルやVScodeなど、実行する場所を追加する必要があります。

# 使い方
## 📷 カメラの設置
 置き方は以下の3通りを想定しています。

- `Normal`: 普通にWebカメラを置いて、自分に向ける(ノートパソコンの内蔵カメラでも可)   
   | 設置方法の例 | 手のひらをカメラに向ける |
   | :---: | :---: |
   | <img width="300" alt="スクリーンショット 2021-09-13 午後5 33 21" src="https://user-images.githubusercontent.com/22733958/134456824-79c1a447-2b06-4b98-ba28-d06b552606e2.jpg"> <img width="300" alt="スクリーンショット 2021-09-13 午後5 33 21" src="https://user-images.githubusercontent.com/22733958/134465166-3c324aef-0ee6-4dd9-9810-b723e945e748.jpg"> | ![スクリーンショット 2021-09-23 044041](https://user-images.githubusercontent.com/22733958/134456933-0c81812d-c23d-4e52-860e-2a341d5bbe3c.png) |

- `Above`: 手の上に設置し、手元に向ける  
   | 設置方法の例 | 手の甲をカメラに向ける |
   | :---: | :---: |
   | <img width="300" alt="スクリーンショット 2021-09-13 午後5 33 21" src="https://user-images.githubusercontent.com/22733958/134124093-51c85b18-3d90-4935-8daa-a78761d1aaed.jpg"> | ![スクリーンショット 2021-09-23 044243](https://user-images.githubusercontent.com/22733958/134456961-755a2769-1d2d-4cca-8fbd-6b49c7b2c0b1.png) |

- `Behind`: 自分の後ろに設置し、ディスプレイに向ける    
   | 設置方法の例 | 手の甲をカメラに向ける |
   | :---: | :---: |
   | <img width="300" alt="スクリーンショット 2021-09-13 午後5 33 21" src="https://user-images.githubusercontent.com/22733958/134123691-19eb8a76-8f01-497d-b09b-ea93e72825d5.jpg"> | ![スクリーンショット 2021-09-23 044403](https://user-images.githubusercontent.com/22733958/134456968-aaf3660d-9ee2-45b8-b65a-9590a6aec4fe.png) |

## 🚀 実行
- [GitHub wiki](https://github.com/takeyamayuki/NonMouse/wiki/How-to-run-a--NonMouse-executable-file-in-each-OS#%E6%97%A5%E6%9C%AC%E8%AA%9E)の通りに実行可能ファイルを実行  

   もしくは、
- インストールの続きから、以下のスクリプトを実行  

   windowsの場合  
   ```sh
   $ python3 app.py
   ```

   macの場合は、実行権限が必要なので
   ```sh
   $ sudo python3 app.py
   ```
   
   linuxの場合は、グローバルホットキーなし（常に動く）のapp-s.pyを起動してください。
   ```sh
   $ python3 app-s.py
   ```

## 💻 設定
実行すると、以下の画面が出ます。この画面でカメラ、感度の設定をします。

![スクリーンショット 2021-10-04 205924](https://user-images.githubusercontent.com/22733958/135847704-97ae9d54-9572-4f47-beb6-a7bfe8bbaeaf.png)

- `Camera`  
カメラデバイスを選択してください。複数カメラが接続されている場合は、小さい番号から、順番に試してみてください。

- `How to place`   
カメラの置き場所を指定してください。「📷 カメラの設置」での`Normal`, `Above`, `Behind`のどれかの置き方をしてください。

- `Sensitivity`  
感度を設定します。あまり大きくしすぎると、マウスカーソルが小刻みに揺れます。

設定が終わったら、continueをクリックしてください。すると、カメラの映像が映し出され、選択した設定でNonMouseが使えるようになります。

## 👆 手の動き

| アクティブ化 | カーソル | 左クリック | 右クリック | スクロール |
| :---: | :---: |:---: |:---: |:---: |
|![](https://user-images.githubusercontent.com/22733958/134462214-af90785f-29fb-4230-a2b4-4618ee0b26dd.gif) | ![](https://user-images.githubusercontent.com/22733958/134462179-6bd5a666-92b4-4c87-a02e-711430dd5180.gif)| ![](https://user-images.githubusercontent.com/22733958/134462244-e2a4e47e-d183-44b9-ace5-b771b063289c.gif)| ![](https://user-images.githubusercontent.com/22733958/134462268-90a07833-4ecc-4b29-85c6-6925f106cbc2.gif) | ![](https://user-images.githubusercontent.com/22733958/134462278-a857012e-76a6-4abd-bdc3-53664c8cf643.gif) |


以下の手の動きが、`F4`を押している時だけ有効になります。ウィンドウがアクティブになっていなくても使えます。この機能はwindows, macのみ使えます。  
(linuxでは、この機能が制限されたapp-s.pyを使用してください。これはlinuxにおいて[keyboardライブラリ](https://github.com/boppreh/keyboard)がsudoで動かないことに起因します。動かせた人がいたら報告してほしいです。)

* カーソル  
   * マウスカーソル: 人差し指の先端 → 青色の円が人差し指の先端に表示される  
   * マウスカーソルの動きを止める: 人指し指の指先と中指の指先をくっつける → 青色の円が消える  
* 左クリック  
   * 左クリック: 親指の指先と人差し指の第２関節をくっつける → 黄色の円が人差し指の先端に表示される  
   * 左クリックのリリース: 親指の指先と人差し指の第２関節を離す → 黄色の円が消える  
   * ダブルクリック: 左クリックを0.5秒以内に2回行う  
* その他  
   * 右クリック: カーソルを動かさずに、クリック状態を１.5秒続ける → 赤色の円が人差し指の先端に表示される  
   * スクロール: 人差し指を折った状態で人差し指でスクロール  → 黒色の円が人差し指の先端に表示される

† 手元を明るくして使ってください。  
† カメラに対して、なるべく手をまっすぐ向けてください。

## 🔚 終了
ターミナルウィンドウがアクティブのとき、Ctrl+C  
アプリケーションウィンドウがアクティブのときは、閉じるボタン(windows, linuxのみ)かEscを押してください。

# ビルド
※ビルド済みバイナリファイルは、latest realeaseからダウンロード可能です。

app-mac.spec, app-win.specにおいて`pathex`を自分の環境に合わせて変更してください。  
各OSに合わせて以下のスクリプトを実行。

- windows

   `pip show mediapipe`で得られたLocationを`datas`にもとから書いてあるものを参考にしながらコピペする。  
   以下のスクリプトを実行。
   ```sh
   $ pip show mediapipe
   ...
   Location: c:\users\namik\appdata\local\programs\python\python37\lib\site-packages
   ...
   #app-win.specのdatasへコピペする
   $ pyinstaller app-win.spec
   ```
- mac

   venv環境を作ってから`pip install`してください。`datas`で指定しているディレクトリはvenv環境前提のため。  
   ```sh 
   $ python3 -m venv venv
   $ . venv/bin/activate
   (venv)$ pip install -r requirements.txt
   (venv)$ pyinstaller app-mac.spec
   ```