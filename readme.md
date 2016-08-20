#Pythonを勉強したことの備忘録　　
##導入方法　　
###設定元の環境
OS　Windows10Pro(64bit)  
必要になったライブラリなどをこれから随時追加するかも？  
###導入手順
 まず、<https://www.continuum.io/downloads>から
 anacond 3.5 Installする〈64bit番〉  
python2.7なども使えるように環境を構築する  
まずは、インストールしたAnacondaをそのまま展開(環境変数なども自動で設定してもらった)  
 インストール後、コマンドプロンプトを開いて以下を実行する  
 `conda create -n p27 python=2.7 anaconda`  
 これでpython2.7の環境構築も終了です。 
 py27の部分には自分で分かるような名前を付けるといいと思います。  
 作った環境を見るためには以下のコマンドで確認できます　　
`conda env list`
で実際に作った環境に変更するにはlistで表示された名前を以下のコマンドに入力します。　　
今回の場合だとPython2.7の環境にするには以下脳用になります。
`activate py27`
最後に変更を戻す方法ですが　　
`deactivate`
を入力すればしょきせてちに戻ります。
 
 
