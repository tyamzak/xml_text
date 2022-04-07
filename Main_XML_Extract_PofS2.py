
# XMLファイル: 指定された要素型の実現値変更
# 入力ファイル: test.xml
# 出力ファイル: result.xml

import sys
import csv                           #追加
from sys import argv                 # コマンドライン引数利用
from xml.etree.ElementTree import *  # XMLモジュール

ifileX = argv[1]                     # 入力ファイル(XML)
ofileX = argv[2]                     # 出力ファイル(XML)


tree = parse(ifileX)                 # 入力ファイル(XML)の読み込み
root = tree.getroot()                # ルート要素を取得(Element型)

with open(argv[2],'w', newline='') as f:   #ファイル名指定
	w = csv.writer(f)							      #
	for elements in root.iter("エントリ"):            # 繰り返しの要素型(レコード)
   		tag1 = elements.find(argv[3])  # 実現値変更対象の要素型
//   		tag2 = elements.find(".//第2カテゴリ品詞名")  # 実現値変更対象の要素型
   		tag2 = elements.find(argv[4])  # 実現値変更対象の要素型

   		if (tag1.text == argv[3]) :
   	  		w.writerow([tag1.text,tag2.text])         # debug用

print("fileを作成しました")
