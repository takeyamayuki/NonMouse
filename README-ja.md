# NonMouse

Webカメラで自分の手元を写すことで、あたかも実体のないマウスがあるかのように見えるPythonスクリプトです。  
使用用途は主に絵を書く際、液タブなどに対する安価な代替として使うことを想定しています。    
動作状況は[Youtube](https://youtu.be/ufvOJUTCF8M)にも公開しています。  
(感度調整なしのver.1は[こちら](https://github.com/takeyamayuki/NonMouse))   

![github_drug](https://user-images.githubusercontent.com/22733958/129838994-f1499648-a179-4e0d-a62f-a4d983ba380a.gif)  

![github_e](https://user-images.githubusercontent.com/22733958/129839012-82915bcf-10a5-49d1-8e03-e4f0def7b778.gif)  


# インストール

### 普通にインストール
```sh
$ git clone https://github.com/takeyamayuki/NonMouse
$ cd NonMouse
$ pip install -r requirements.txt    # requirements.txtからパッケージインストール
```

### ローカル環境を汚したくない場合
```sh
$ git clone https://github.com/takeyamayuki/NonMouse
$ cd NonMouse
$ . NonMouse/bin/activate           # 仮想環境に入る
```
`$ deactivate`で仮想環境から抜ける  

※ macの場合、システム環境設定からセキリュティとプライバシーのアクセシビリティの項目にターミナルやVScodeなど、実行する場所を追加する必要があります。

# 使い方
### 実行
インストールの続きから、以下のスクリプトを実行
```sh
$ python3 app.py
```
もしくは、
```sh
$ chmod 755 *.sh                    # .shファイルに実行権限を与える
$ ./launch.sh                       # シェルスクリプトの実行(launch.shの中身は[$ python3 app.py]です)
```
### 手の動き
* マウスカーソル: 人差し指の先端  
* マウスカーソルの動きを止める: 人指し指の指先と中指の指先をくっつける   
* 左クリック: 親指の指先と人差し指の第２関節をくっつける
* 左クリックのリリース: 親指の指先と人差し指の第２関節を離す  
* ダブルクリック: 左クリックを0.5秒以内に2回行う
* 右クリック: カーソルを動かさずに、クリック状態を１秒続ける
* スクロール: 中指と薬指をくっつけると人差し指でスマホのようにスクロールできる

### 引数
* `--device X`でカメラを複数搭載している場合、引数でカメラを選択できます(デフォルト0で0,1,2...が選択可能)  
   ```sh
   $ python3 app.py --device 0
   ```
* `--direciton X`で指の動かす向きに対するマウスカーソルの動く向きを指定できます(デフォルト0で0,1が選択可能)  
    * webカメラを下に向けて使用する場合：0     
    * ラップトップ付属のカメラを使用する場合：１    
   ```sh
   $ python3 app.py --direction 0
   ```
* `--distance X`でタッチ距離を定義（遠いほど小さく、近いほど大きい値にする）(デフォルト65で、整数で選択可能)  
[目安]
    * webカメラと手の距離が50cmのとき、65
    * webカメラと手の距離が110cmのとき、50
   ```sh
   $ python3 app.py --distance 50
   ```
* `--kando X`でマウス感度を定義（大きくしすぎると小刻みに震えるので大きくしすぎないこと）(デフォルト1.5で、小数で選択可能)  
[目安]
    * webカメラと手の距離が50cmのとき、1.5
    * webカメラと手の距離が110cmのとき、5
   ```sh
   $ python3 app.py --kando 5
   ```
これらの引数をまとめて指定できるようにシェルスクリプトにまとめました。  
```sh
$ chmod 755 *.sh                    # .shファイルに実行権限を与える
$ ./launch.sh                       # シェルスクリプトの実行
```
launch-ceiling.sh, launch-frcam.sh も同様に実行できます。
* launch-frcam.shはラップトップのwebカメラを使用するためのスクリプト  
* launch-ceiling.shは天井に取り付けたwebカメラを使用するためのスクリプト
### プログラムの止め方
ターミナルウィンドウがアクティブのとき、Ctrl+C  
アプリケーションウィンドウがアクティブのときは、Escを押してください  
