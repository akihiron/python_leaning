#Pythonを勉強したことの備忘録(環境構築)　　
##導入方法　　
###設定元の環境
OS　Windows10Pro(64bit)  
####python3.5.1
####selenuim 3.0.1
####opencv3.1.0 
必要になったライブラリなどをこれから随時追加するかも？  
今回はseleniumを使用してWebテストを行いたいので
seleniumのインストールを行います。ですが、condaからではインストールできませんでした。  
`pip install selenium`  
そこで上記のようにpipを使用してinstallします。
続いて導入したのはopencvです。  
opencvには[2016-08-21]現在2，3というライブラリが存在していて  
どちらを使うか悩んだのですが、勉強するなら新しい方と思い、  
opennnncv3を導入します。(webの文献は２のほうが多そうだからそのうち２も入れると思うなーたぶん)  
###導入手順
 まず、<https://www.continuum.io/downloads>から
 anacond 3.5 Installする〈64bit番〉  
python2.7なども使えるように環境を構築する  
まずは、インストールしたAnacondaをそのまま展開(環境変数なども自動で設定してもらった)  
 インストール後、コマンドプロンプトを開いて以下を実行する  
 `conda create -n p27 python=2.7 anaconda`  
 これでpython2.7の環境構築も終了です。 
 この他にも同じコマンドで仮想の環境がいくつでも作れるそうです。  
 py27の部分には自分で分かるような名前を付けるといいと思います。  
 作った環境を見るためには以下のコマンドで確認できます  
`conda env list`  
で実際に作った環境に変更するにはlistで表示された名前を以下のコマンドに入力します。  
今回の場合だとPython2.7の環境にするには以下になります。  
`activate py27`  
最後に変更を戻す方法ですが  　　
`deactivate`  
を入力すれば初期設定地に戻ります。  
また用意した環境が必要なくなった場合には  
`conda remove -n py2`
でいなくなる    
>https://gist.github.com/aphlysia/d5fcee79ff81b8272faf   

さらに上のサイトよりpipでインストールするパッケージを  
condaで管理できるように以下のコマンドを実行します。  
`conda skeleton pypi selenium`  
ところがpythonのエラーにより失敗しました。  
>https://github.com/conda/conda-build/issues/119   

そこで上のサイトを参考に  
`conda update conda`  
`conda install conda-build`  
を試したところうまくいきました。  
管理に追加して具体的にどうなるのかは  
 `conda list | find "selenium"`  
 を実行してみると以下のように表示されて  
 selenium                  2.53.6                    <pip>  
管理に追加されたことが分かります  
Chromedriver.exeを下記のURLからダウンロードする
>http://chromedriver.storage.googleapis.com/index.html?path=2.23/

あとはseleniumからCrhomeを操るためのtestChrome.pyを作ります。  

＊後々調べたところ  
pipからinstallせずとも  
`conda search selenium`  
の指示に従って、
`anaconda search -t conda  selenium`  
を使い表示されたリストからPlatformsの条件を選んで  
`anaconda show conda-forge/selenium`  
を実行すれば  
`conda install --channel https://conda.anaconda.org/conda-forge selenium`  
と表示されるのでここからinstallできるかもしれない(実行はしていませんが(;´･ω･))  

opencvは上記の方法を実行したいと思います  
上記の順番で実行すると  
` conda install --channel https://conda.anaconda.org/menpo opencv3`  
にたどり着きこいつを実行すると・・・
問題なくインストールできました。
`conda list |find "open"`で確認すると
>opencv3                   3.1.0                    py35_0    menpo

のようにインストールしたpackageの名前が最後に入るんですね
適当なこと言ってますが、間違ってたら教えてください。


#[2016.10.30]追記
以前ダウンロードしたseleniumを使用して  
Firefoxを起動したところ、以下のように表示され、動かなくなっていた  
selenium.common.exceptions.WebDriverException: Message: Can't load the profile. Profile Dir: C:\Users\Akihiro\AppData\Local\Temp\tmpt9vrpaat If you specified a log_file in the FirefoxBinary constructor, check it for details.
そこで、まずはseleniumのversionUPを行った。  
Version変更方法は  
`pip install -U selenium`  
pipにはVersionアップのコマンドがないらしく  
-Uオプションを使用してversionを変えるらしい  
戻す方法は調べてない(-_=;;)  
大丈夫かな？  
⇒[20170204]インストールするときにversionを指定すればいいっぽいので次で元に戻せる  
`pip install -U selenium==2.53.6`  
とりあえずseleniumのversionが2.53.6→3.0.1になりました。 
以前の方法で管理しているのでcondaの方にもきちんと  
`conda list | find "selenium"`  
で確かめたところ反映されていました.  
しかし、まだ動いてくれません。以下のコマンドで動作確認したところ  
`from selenium import webdriver`  
`webdriver.Firefox()`  
今度は以下のメッセージが出るようになりました。  
selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.  
調べても最新のFirefoxを動かすためには、  
geckodriverをとりあえずダウンロードしてpathを通しなさい  
しか出てこないので仕方なくダウンロード  
情報元：http://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path  
以下のサイトからWin64bit用をダウンロード  
https://github.com/mozilla/geckodriver/releases    
とりあえずPATHが通っているAnaconda内において実行してみる  
上記のサイト通り同じことで怒られました。ちょっと安心(~_~)  
selenium.common.exceptions.WebDriverException: Message: Expected browser binary location, but unable to find binary in default location, no 'moz:firefoxOptions.binary' capability provided, and no binary flag set on the command line  
とりあえず、指示に従って以下を実行  
`from selenium import webdriver`  
`from selenium.webdriver.firefox.firefox_binary import FirefoxBinary`    
`binary = FirefoxBinary('path/to/installed firefox binary')`  
`browser = webdriver.Firefox(firefox_binary=binary)`  
以下のエラーメッセージという仕打ちです。正直勘弁してほしかったのですが  
selenium.common.exceptions.WebDriverException: Message: Failed to start browser:
entity not found  
以下のサイトを見ると  
情報源：http://stackoverflow.com/questions/20950748/cannot-find-firefox-binary-in-path-make-sure-firefox-is-installed   
どうやらバイナリに指定するのはMozilla Firefoxのexeファイルのよう  
そこで先ほどのコマンドを  
`from selenium import webdriver`  
`from selenium.webdriver.firefox.firefox_binary import FirefoxBinary`  
`binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')`  
`browser = webdriver.Firefox(firefox_binary=binary)`  
に書き換えたらエラーなく動きました。  
ここまで調べると、もしかしたらそもそもseleniumのversionUP必要なかったのではと恐ろしい  
結論が出そうです；；  
まあ、Chromeなども動かすのに引数が一つ増えたけどそれだけなのでとりあえず、良しとします  
`browserc = webdriver.Chrome(r'C:\Windows\SysWOW64\chromedriver.exe')`  

#2016/11/20　Android seleniumについて  
##環境構築  
今回は以下のページを参考にAndroidのselenium導入についてやっていきます。
<http://zafiel.wingall.com/archives/6919>
さてとまずは、
コマンドプロンプトからadbを実行して・・・
(;;)残念Android-SDKが未導入でした。
まずはそっからかよ(;´д｀)トホホ
方法がわからない方はこの辺参考にしてください
http://www.javadrive.jp/android/install/index1.html
###Android-SDK環境の構築
念のため、導入手順を書いておくと
1．https://developer.android.com/studio/index.html#downloadsからandroid-sdk_r24.4.1-windows.zip
インストーラなしをダウンロードする  
2．zipフォルダを展開して、SDK Manager.exeを実行  
⇒失敗(javaがインストールされてなかったw)  
3.上記の失敗を踏まえてJDKをhttp://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.htmlから
ダウンロードPathの設定をする。  
4.SDKが実行できるようになっていたので  
Android SDK Tools,Android SDK Platform-Toolsをダウンロード
これでADB周りは整うはず,ちなみに以下の[サイト][make_uiautomator.jar]に従ってAPI16のSDK Platformをインストールしたところ
platforms\android-16にuiautomator.jarを確認できた(動作は未確認)  
⇒動作しないことが判明[詳細][uiautomator.jar]  
[make_uiautomator.jar][]  
!!!android-server-2.21.0.apkダウンロードとか書いてあるけど  
リンクは違うSeleniumHQとかに飛んでダウンロードできそうにない  

###[2016_11_26]
まぁ、リンク先が変わったのでしょうよくあることなのでもうちょっといろんなサイトから情報を集めてこようと思います  
で、分かったこと  
1.Android版のSeleniumをダウンロードするにはAppiumが使えるみたい(Appiumが最も精力的に開発されている模様)[参考][Appiumのまとめ]
2.Android 4.1以前のネイティブアプリをテストする場合、その再生ロジックは内部的にSelendroidが使われている(古い機種はSelendroidを使用する)  
3.appiumをダウンロードするにはnpmが必要[参考][Appium_download]  
以上であります。(￣▽￣)ゞラジャ  
おいちょっと待てそもそもnpmって何ぞや！？俺は思った。
>>googleさんはおしえてくれた。[こちら][npm]

ようするにnode.jsのパッケージ管理ツールだそうです  
で、node.jsっていうのはjavascriptにライブラリ機能を  
実装するためのツール？？何度読んでもわからないので機会があるときまた勉強します。＞＜  
まぁ、何はともあれ必要なんだろnpmってことで
###npmを使ったnode.js環境構築by Windows10
まずはググった[npmをダウンロードする方法][npm_DL]
意外と楽そうなので書いておきます  
1．[node.js][node.js_DL]へアクセスしてダウンローダをダウンロード  
以上。パスなんかも自動で通してくれるし、ダウンローダーの説明見るとわかるけど  
npm(パッケージ管理ツール)も自動でインストールしてくれる。
念のため、コマンドプロンプトから`npm -version`と打ってパスが通っていることを確認  

ふぃーここまで終わった
あとはさっきの[Appiumのダウンロードのページを参考][Appium_download]にAppiumを入れよう
で、まずは何もProxyなど設定しないでいきなり下記のコマンドインストールしてしまったが、以下のログ以外には問題がなかった。  
`npm -g install appium`  
とりあえずできたと考えることにする。  
>>npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@^1.0.12 (node_modules\appium\node_modules\fsevents):
npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.0.15: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})

追々、こっちも実行するかも[参考][Appium_root]  
`npm install wd         # get appium client`  
`appium &               # start appium`  
`node your-appium-test.js`  
次にサンプルコードを動かすため[sample][Appium_Python]のreadme.mdをみながら準備します。
Anacondaを使って以下の通りコマンドを入力しました。  
`conda install Appium-Python-Client`  
`anaconda search -t conda appium-python-client`  
`anaconda show hargup/appium-python-client`  
しかし、PlatformがLinux版しかないとな！！
なら上の方法でとりあえずpipからインストールするか
`pip install Appium-Python-Client`  
おお、動いた。でもpip version upしろって言ってたな  
現pip(ver8.1.2)最新は9.0.1らしい  
ま、トリマ無視して  
`conda skeleton pypi Appium-Python-Client`  
これでAppiumも管理できるはずしかし、version0.2.3ってだいぶ古い気がする
さっきみたlinuxのはPython client for Appium 1.3.6だったからなー  
まぁいいや  
では、sampleの動かし方だが、  
1.サンプルのテストを[公式サイト][appium_sample]からgitpullする  
2.Appiumサーバーを起動する  
3.%homepath%\python_leaning\Appium\sample-code\sample-code\examples\pythonandroid_simple.pyのplatformVersionをAndroidのversionと合わせる(6.0)  
4.サンプルスクリプトを実行する

【条件】
Androidのロックが外れていること、Android SDK-Toolが入っていることなど[参考はこちら][App_python_sample]  
以下,動かしたときの実施コマンド  
`cd %homepath%/python_learning`  
`mkdir appium`  
`git clone https://github.com/appium/sample-code`  
`start cmd`  
`appium &`  
もとのコマンドに戻って  
`cd %homepath%\python_leaning\Appium\sample-code\sample-code\examples\python`  
`py.test android_simple.py`  
動いたーとりあえずここまでで終わります。


[uiautomator.jar]:https://github.com/akihiron/Java_learning/blob/master/decompile/Decompile.md "Uiautomator"
[make_uiautomator.jar]http://qiita.com/setsulla/items/923f0ec9e69aff9e15a4 "uiautomator.jar作成参考ページ"
[Appiumのまとめ]:http://blog.trident-qa.com/2014/04/selenium-mobile/ "seleniumモバイルの開発概要"
[Appium_download]: http://qiita.com/siguremon/items/44ddba891119c3f78508 "Appiumインストール手順(Win)"
[npm]: http://qiita.com/megane42/items/2ab6ffd866c3f2fda066　”npmとは”
[npm_DL]: http://qiita.com/taipon_rock/items/9001ae194571feb63a5e "npmダウンロードツール"
[node.js_DL]:https://nodejs.org/en/ "node.jsの公式サイト"
[Appium_root]:http://appium.io/ "Appium_公式サイト"
[appium_sample]:https://github.com/appium/sample-code "appiumの公式ページのサンプルスクリプト"
[Appium_Python]:https://github.com/appium/sample-code/tree/master/sample-code/examples/python "Appium_pythonの導入"
[App_python_sample]:http://qiita.com/skinoshita/items/211ca23edbb5f2776771 "appium実行するまでのブログ？"
