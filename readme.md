#Pythonを勉強したことの備忘録　　
##導入方法　　
###設定元の環境
OS　Windows10Pro(64bit)  
必要になったライブラリなどをこれから随時追加するかも？  
今回はseleniumを使用してWebテストを行いたいので
seleniumのインストールを行います。ですが、condaからではインストールできませんでした。  
`pip install selenium`  
そこで上記のようにpipを使用してinstallします。
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
