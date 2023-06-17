# MK8DX_Rank-Collector
Sorry, README.md and program comment out is all Japanese program...

This bot support English !

## 概要
このBotはDiscord上でMK8DXでのコース順位を入力することで記録し、平均順位や過去の記録を見れるようにしたり、外部ファイルにエクスポートをする機能を提供するBotです。
（Github上で公開しているコードには現在はエクスポートの機能を除いてあります。）

## Special Thanks!!
※敬称略

*  → 

  Twitter：[https://twitter.com/](https://twitter.com/)

## 招待URL
* [Invite](https://discord.com/api/oauth2/authorize?client_id=1115779746198999103&permissions=8&scope=applications.commands%20bot)

## Download
* [Download Link](https://github.com/Ay2416/Rank-Collector/archive/refs/heads/main.zip)

## 注意
* 

## 使い方（Discord上）
下記のスラッシュコマンドを使用して使うことができます。

* 

# ↓ここから先はプログラムについての話になります↓

## 動作確認済み環境
* 

* Windows11

  python 3.10.11

## 使い方（プログラムの動作のさせ方）
※DiscordのBotの作成やトークンの取得はできている前提で説明させていただきます。

※Botをプログラム側で起動できたことが確認できるまで、サーバーへBotの招待を行わないでください。
* これは、英語対応をさせた時にサーバーの入退出でそれを判定するファイルが生成される仕様にしたためです。
そのため、先にBotが起動していない状態でサーバーへ招待を行うとコマンドの仕様ができません。
申し訳ないです。

1. 最初にPythonをインストールしてください。（導入済みの方は飛ばしていただいて結構です。）

※もしかしたら導入済みの可能性もありますので、Windowsの場合はコマンドプロンプト、Linuxの場合はターミナルで「python --version」と打ち、「Python 〇.〇.〇」みたいな表記がでれば導入されているかが確認できます。
* Windows：[Link](https://www.javadrive.jp/python/install/index1.html)

* Linux(Ubuntu)：[Link](https://self-development.info/ubuntu%E3%81%AB%E6%9C%80%E6%96%B0%E3%83%90%E3%83%BC%E3%82%B8%E3%83%A7%E3%83%B3%E3%81%AEpython%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B/)

2. 次にこのページの１番上の方にある、「Download」を押して、「Rank-Collector-main.zip」をダウンロードします。（Linuxでターミナルで行っている場合はwget等を使用して、ダウンロードしてください。）

3. そしてそのファイルを解凍し、「.env」をテキストエディタで開き、「your_discord_bot_token」という部分にDiscordのBotトークンを入れてください。

  ※「.env」が見えない場合、隠しファイル扱いとなっている可能性が高いため、下記を参考に表示できるようにしてください。

* Windows10：[Link](https://pc-karuma.net/windows-10-show-hidden-files-folders/)

* Windows11：[Link](https://www.fmworld.net/cs/azbyclub/qanavi/jsp/qacontents.jsp?PID=8511-2971)

* Linux(Ubuntu かつ デスクトップ画面からの操作の場合)：[Link](https://linuxfan.info/show-hidden-files-in-nautilus#toc_id_3)

4. コマンドプロンプトまたは、ターミナルで「main.py」があるディレクトリまで移動し、「pip install -r requirements.txt
」を打ってから、「python main.py」と打つことでプログラムを開始し、使用することが可能になります。

※ディレクトリの移動方法

* Windowsの場合は簡単な操作でそのディレクトリからコマンドプロンプトを起動する方法があります。 → [Link](https://qiita.com/windows222/items/2ac133a244f4a9527022)

* Linux(Ubuntu)の場合：[Link](https://uxmilk.jp/27431)（簡単に行けそうな方法を見つけようとしたのですが、自分の力では見つけることができませんでした...。）


### Botを作成する際、必要となる権限は以下の通りです。

* addモード、deleteモードにおいて10分操作がなかった場合のメッセージを送信する際にエラーが発生してしまうのを防ぐため、設定された投稿先のチャンネルを全て標準で見えるようにするためAdministratorを標準の権限にすることにしました！

## ライセンス
* MIT LICENCE↓

  [https://github.com/Ay2416/Rank-Collector/blob/main/LICENSE](https://github.com/Ay2416/Rank-Collector/blob/main/LICENSE)

## 利用させていただいたライブラリ
* 
