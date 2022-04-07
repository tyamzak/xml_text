#
# リスト((多次元可変長)配列)に対する読み込み・書き込み(read/write)処理
#

"""
 各種形式のファイルをリスト(多次元可変長配列)に格納
 入力ファイル
 　text2list: テキストファイルをlistに格納する
   csv2list:  csv(カンマ区切り)ファイルをlistに格納する
   tsv2list:  tsv(タブ区切り)ファイルをlistに格納する
   ssv2list:  tsv(空白区切り)ファイルをlistに格納する
 出力ファイル
   list2text: listをテキストファイルとして出力する
   list2csv:  listをCSVファイルとして出力する
   list2tsv:  listをTSVファイルとして出力する
   list2ssv:  listをSSVファイルとして出力する
"""

import csv                 # csvモジュール

# 入力ファイル用
def text2list(table, filename):
    with open(filename, "r", encoding='utf-8') as ifile: #入力ファイル
        dataobj = ifile.readlines()  # ifile全体を読み込む
    for line in dataobj :
        line = line.strip()  # 改行を削除
        table.append(line)    # listにlineを追加
    return


def csv2list(table, filename):
	list = []
	i = 0
	with open(filename, "r", encoding='utf-8') as ifile:#入力ファイル
		dataobj = csv.reader(ifile)  					# csv file全体を読み込み
		for line in dataobj :
			table.append(line)							# listにlineを追加
			i += 1
		return i


def tsv2list(table, filename):
    with open(filename, "r", encoding='utf-8') as ifile: #入力ファイル
         reader = csv.reader(ifile, delimiter='\t')  # tsv file全体を読み込み
         for line in reader :
             table.append(line)    # listにlineを追加
    return


def ssv2list(nh, filename):
	header = []
	table = []
	with open(filename, "r", encoding='utf-8') as ifile: #入力ファイル
		reader = csv.reader(ifile, delimiter=' ')  # ssv file全体を読み込み
		for line in reader :
			table.append(line)    # listにlineを追加
		for i in range(int(nh)):
			header.append(table[i])
			table.pop()
	return header, table


# 出力ファイル用
def list2text(filename, table):
    with open(filename, "w", encoding='utf-8') as ofile: #出力ファイル
         ofile.write('\n'.join(table))
    return 


def list2csvQuat(filename, table):
    with open(filename, "w", encoding='utf-8') as ofile: #出力ファイル
# デリミター、改行コード、囲み記号の指定
        writer = csv.writer(ofile, delimiter=',', lineterminator='\n', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(table)     # list（2次元配列）の場合
    return 


def list2csv(filename, table):
    with open(filename, "w", encoding='utf-8') as ofile: #出力ファイル
# デリミター、改行コード、囲み記号の指定
        writer = csv.writer(ofile, delimiter=',', lineterminator='\n')
        writer.writerows(table)     # list（2次元配列）の場合
    return 


def list2tsv(filename, table):
    with open(filename, "w", encoding='utf-8', newline='') as ofile: #出力ファイル
        line = csv.writer(ofile, delimiter='\t', lineterminator='\n' )
        line.writerows(table)     # list（2次元配列
    return 


def list2ssv(filename, header, table):
    with open(filename, "w", encoding='utf-8') as ofile: #出力ファイル
# デリミター、改行コード、囲み記号の指定
        writer = csv.writer(ofile, delimiter=' ', lineterminator='\n')
        writer.writerow(header)	# 見出し行
        writer.writerows(table)		# table(2次元配列）
    return 


