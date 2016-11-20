#Pythonを勉強したことの備忘録　　
##導入方法　　
###設定元の環境
OS　Windows10Pro(64bit)  
####python3.5.1
####selenuim
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
戻す方法は知ればてない(-_=;;)  
大丈夫かな？  

とりあえずseleniumのversionが2.536→3.0.1になりました。 
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
`browser = webdriver.Firefox(firefox_binary=binary)'  
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
`browser = webdriver.Firefox(firefox_binary=binary)'  
に書き換えたらエラーなく動きました。  
ここまで調べると、もしかしたらそもそもseleniumのversionUP必要なかったのではと恐ろしい  
結論が出そうです；；  
まあ、Chromeなども動かすのに引数が一つ増えたけどそれだけなのでとりあえず、良しとします  
`browserc = webdriver.Chrome(r'C:\Windows\SysWOW64\chromedriver.exe')`  
