from sklearn.linear_model import LinearRegression
import pandas as pd
readfiles   = [ "test.csv" ]

for readfile in readfiles:

    #私の環境ではUTF-8でないと読み込めないので
    df=pd.read_csv(readfile, encoding="utf-8")
    #df=pd.read_csv(readfile, encoding="SHIFT_JIS")
    print(readfile)
    print(df)

    Y=df[['Capacity']]
    X=df[['Temperature']]
    model = LinearRegression()
    model.fit(X,Y)
    print('Y=',model.coef_[0,0],'X+',model.intercept_[0])

    """
    #①　X,Y軸に指定する列に関して、上記のようなヘッダ名ではなく、列番号を指定する方法を教えてほしい。
    #A:ilocを使用する。下記のようになる。行の指定は:で全て取得する
    """
    print(df.iloc[:,[0]])
    print(df.iloc[:,[1]])

    Y=df.iloc[:,[0]]
    X=df.iloc[:,[1]]

    model = LinearRegression()
    model.fit(X,Y)
    print('Y=',model.coef_[0,0],'X+',model.intercept_[0])
    print('Y=',model.coef_[0],'X+',model.intercept_)

    """
    #②　X軸が2つ存在する重回帰分析の方法を教えてほしい。Y=aX1 + bX2 +C
    #A:目的変数以外を削除して、Xに代入、目的変数をYに代入。これでモデルを作る。あるいは複数の説明変数を入れる。

    #下記の終わりにの手前
    https://qiita.com/0NE_shoT_/items/08376b08783cd554b02e#%E7%B7%9A%E5%BD%A2%E5%9B%9E%E5%B8%B0%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E6%80%A7%E8%83%BD%E8%A9%95%E4%BE%A1

    https://qiita.com/karaage0703/items/f38d18afc1569fcc0418#%E9%87%8D%E5%9B%9E%E5%B8%B0%E5%88%86%E6%9E%90

    """


    #③　X,Y軸にヘッダ名を指定する場合、なぜ[が2つ必要になるのか？
    #A:1個だとSeriesオブジェクトになってしまう。2つないとDataFrameオブジェクトにならないから。

    """
    #④　coef_、intercept_について、coef[0,0]、intercept[0]と配列の次元が異なってしまう理由はなぜ？
    #A:coefは回帰係数であり、interceptは切片であるから。
    回帰分析する時、説明変数Xの値をリストで入れる。重回帰分析に対応させるためにリストで入れなければならない。故にそれに対応して回帰係数もリストで返ってくる。
    一方で切片は単なる値にすぎない。目的変数を出すため、回帰係数と説明変数の掛け算をした後に加算するだけ。故にリストではない数値で返ってくる。


    今回のコードの場合、目的変数も同様にリストで代入している。そのため、余分に次元が生成されてしまう。
    """

    X=df[['Temperature']]
    Y=df['Capacity']
    model = LinearRegression()
    model.fit(X,Y)

    print("=============")
    print('Y=',model.coef_[0],'X+',model.intercept_)
    print("=============")

    #⑤　pandasのread_csvでファイルを読み込む場合、読み込んだファイルはどこのメモリに保存されているのか？　例えば、for文で沢山のファイルを読み込んだ場合、(素人なのでよくわかっていないが)、プログラムの計算速度が遅くなることはあるのか？遅くなってしまう場合、対策案は存在するのか？
    """
    read_csvで読み取ったデータはDataFrameオブジェクトとして変数に格納される。ただ、ループする際に変数内のデータが上書きされていくため、メモリにデータが保存されすぎて遅くなることはない。
    計算速度が遅くなる原因は、計算処理にある。pandasを使用しての計算処理は極力避けて、numpyで行うように仕立てる。
    """



"""
Q2　PWmin =< 10a + 15b + 20c +40d =<PWmin*1.2を満たす整数a,b,c,dの組合せを算出する方法に関して
⑥　以下コードを作成したが、もっと短いコードで算出させる方法は存在するか？もしくは、専用ライブラリ、標準関数等は存在するか？

これはわからない。あるとしたらリストの内包表記ぐらいか？
"""

"""
import math
import itertools
import numpy as np
Powerpattern = np.empty((0,4),int)
#PWminは任意の整数

ar=list(range(math.ceil(PWmin*1.2/10)))
br=list(range(math.ceil(PWmin*1.2/15)))
cr=list(range(math.ceil(PWmin*1.2/20)))
dr=list(range(math.ceil(PWmin*1.2/40)))

for a,b,c,d in itertools.product(ar,br,cr,dr):
    Tpower = 10*a+15*b+20*c+40*d

    if Tpower>=PWmin and Tpower<=PWmin*1.2:
        Powerpattern=np.append(Powerpattern,np.array([[a,b,c,d]]),axis=0)
        continue
"""


#⑦　a,b,c,dの整数組合せを格納させる空配列np.emptyに関して、ネット検索内容の見様見真似で引用したため、使い方がよくわからない。emptyの使い方を教えてほしい。上記コードでは登場しないが、np.zerosも同じ要領で使用するのか？
"""
emptyとzerosの違いは初期値として0を入れるか入れないかの違い。

このコードの場合、冒頭で1行は4個のデータを入れるよう初期化している。4個以上のデータ入力を許さないためにそうしている。
1回のループごとに常に4個の値をappendしているため、あえて0で初期化させる必要はない。

もし、特定の要素に対して直接値を入れるなどの場合は0で初期化したほうがよい。
"""

#⑧　appendの使用要領を教えてほしい。axis=0を指定すると列追加が可能になるが、ここでいうaxisはどういう意味か？
"""
A:axis=0は列に沿った処理、axis=1は行に沿ったの処理。appendする時、行に沿って追加するか列に沿って追加するかを指定しないといけない。
#https://qiita.com/Phoeboooo/items/b464b7df3c64a33caf94
"""

#⑨　numpyとpandasの使い分けのコツは存在するのか？numpy、pandasができることについて、ざっくり教えてほしい。
"""
基本的にnumpyのほうが早いので、計算はnumpy。CSVでの取得やデータの加工等の手続きはpandasに任せたほうが良い。
pandasは列数が多い場合、計算速度が一気に落ちる。一方でnumpyであればその心配はない。

ちなみにsklearnではnumpyを使用して計算している。
DataFrameで直接値を入れるとエラーになるので、列を指定して計算を行う(DataFrameで列を指定することで、numpyオブジェクトになる。)

参照:https://deepage.net/features/pandas-numpy.html#pandas%E3%81%A8numpy%E3%81%AE%E4%BA%92%E6%8F%9B%E6%80%A7
参照:https://qiita.com/andrew_cook/items/c62170ca07a6c522e8e3
"""


