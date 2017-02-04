#Pythonを勉強したことの備忘録(環境構築)　　
##導入方法　　
###設定元の環境
iOS macOS Sierra version 10.12.2(VMware)
####python2.7.10
####selenuim
####opencv3.1.0 
今回用意するもの
1.iOSエミュレータ
2.appiumサーバーのインストール
3.seleniumのインストール等々

それでは[こちら][iOS]を参考に1のエミュレータの作成から始めます。
1．XcodeをMacAppStoreからinstallします。
2.Androidと同じようにnpmのversion管理ツールの導入  
brew install npm  
3.npmからappiumのインストール  
npm install -g appium  


途中brewのアクセス権限のエラーが発生して  
以下のエラーが発生していたが  
Permission denied - /usr/local/etc  
[こちら][brew_error]を参考にして  
`sudo chown -R $USER /usr/local`  
解決できました。
あちこち見て申し訳ないですが、
ここから先は[こちら][appium_fomal]の手順に従って実行しています。  
`brew install ios-webkit-debug-proxy`  

続いて
1．provisioning profileを作る。http://appium.io/slate/en/master/?ruby#setup67
2．SafariLauncherを作ったプロファイルで動かしたいiOSバージョン向けにビルドする。 xcodebuild -sdk iphoneos9.2
3．/usr/local/lib/node_modules/appium/node_modules/appium-ios-driver/build/SafariLauncherへSafariLauncher.appを配置する。
をしなければいけないらしいのだが、provisioning profileってどうやって作るの？
公式ページからの回答は以下になります。
Apple Developers Member Center 
Step 1: Create a new App Id and select the WildCard App ID option and set it to “*”
Step 2: Create a new Development Profile and for App Id select the one created in step 1.
Step 3: Select your certificate(s) and device(s) and click next.
Step 4: Set the profile name and generate the profile.
Step 5: Download the profile and open it with a text editor.
Step 6: Search for the UUID and the string for it is your identity code.

なるほど分からん。まぁ一つ一つこなしてみると
0.Apple Developers Member Centerにアクセス 
1．アップルIDを作成してAppIDに"*″っていう何でもいいよを指定する

[iOS]:https://liginc.co.jp/web/tool/mac-iphone/45329 "iOSのエミュレータ作成"
[iOS_selenium]:http://qiita.com/jbking/items/be6042259d905f96e92a"selenium‗iOS環境構築"
[brew_error]:http://chick307.hatenablog.com/entry/20120531/1338471979"brew Permission error の参考"
[appium_fomal]:http://appium.io/slate/en/master/?ruby#mobile-safari-on-a-real-ios-device"set upを参考にした"