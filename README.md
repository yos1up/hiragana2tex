# hiragana2tex
convert hiragana string to tex string. (ひらがなだけでtex打ち)

ひらがなだけでtexを打てるようにするために作成したプログラムです。 python3 で動作します。パッケージは不要です。

* web上で試せるデモを用意しました： http://yos.gozaru.jp/hiragana2tex/

# できること
日本語（主にひらがな）で入力された文字列を、tex文字列に変換できます。例えば、以下のような文字列変換ができます。
```
<<< original >>>    いちたすにかけるさんひくよん
<<< tex string >>>  1+2\times 3-4

<<< original >>>    にのにのにじょうじょう
<<< tex string >>>  2^{2^{2}}

<<< original >>>    ななてんにぶんのにまんよんせんろくてんに
<<< tex string >>>  \frac{24006.2}{7.2}

<<< original >>>    いちたすにぶんのさんひくよん
<<< tex string >>>  1+\frac{3}{2}-4

<<< original >>>    いちたすに　ぶんの　さんひくよん
<<< tex string >>>  \frac{3-4}{1+2}

<<< original >>>    いちたすに　ぶんの　さん　　ひくよん
<<< tex string >>>  \frac{3}{1+2}-4

<<< original >>>    にのごぶんのいちじょう
<<< tex string >>>  2^{\frac{1}{5}}

<<< original >>>    えっくすにじょうひくわいにじょうは「えっくすたすわい」「えっくすひくわい」
<<< tex string >>>  x^{2}-y^{2}=(x+y)(x-y)

<<< original >>>    りむ　えっくすがむげん　えふ「えっくす」はぜろ
<<< tex string >>>  \lim _{x\rightarrow \infty }f(x)=0

<<< original >>>    しぐま　あいいこーるいち　えぬ　けーにじょういこーるろくぶんの　えぬ「えぬたすいち」「にえぬたすいち」
<<< tex string >>>  \sum _{i=1}^{n}k^{2}=\frac{n(n+1)(2n+1)}{6}

<<< original >>>    にえー ぶんの  まいなすびーぷらすまいなするーと びーにじょうひくよんえーしー
<<< tex string >>>  \frac{-b\pm \sqrt{b^{2}-4ac}}{2a}

<<< original >>>    えーの　ぴーひくいち　じょうごうどういちもどぴー
<<< tex string >>>  a^{p-1}\equiv 1\bmod p

<<< original >>>    じーしーでぃー　じゅうに、じゅうはち　はろく
<<< tex string >>>  \textrm{gcd} (12,18)=6
```

# 試してみる

* web上で試せるデモを用意しました： http://yos.gozaru.jp/hiragana2tex/

* 手元で試したい場合は、 `hiragana2tex.py` をダウンロードして `python hiragana2tex.py` を実行すれば、実際に文章を入力して、どのようにtex文字列に変換されるかを試すことができます。


# 使い方
`hiragana2tex.py` だけあれば動きます。 `hiragana2tex.py` 内の `hiragana2tex` 関数で、文字列の変換ができます。

~~~python
def hiragana2tex(s):
    '''
    ひらがな文字列をtex文字列に変換
    s <str> : ひらがな文字列
    returns <str> : tex文字列
    '''
~~~
* 「いちたすにぶんのさんたすよん」は 1 + (3/2) + 4 と解釈されますが、「いちたすに ぶんの さんたすよん」と空白をあけると、 (3+4)/(1+2) と解釈されます。このように、適切に空白をあけて入力することで、ある程度は空気を読んでくれます（上の変換例も参照）。空白の長さをもとに、空気を読みます。全角空白は、半角空白2個分と同じに扱われます。
* カッコは、丸括弧または鉤括弧で入力できます。（スマホで入力しやすい文字として鉤括弧を採用しています。）
* カンマは、読点で入力できます。ピリオドは、句点で入力できます。
* トークン辞書は、主に中学高校（〜大学教養課程）で学ぶ数学語を収録しています。読みについては、広く使われていると思われる数式の口語的な読みを中心に採用しています。複数の読み方が登録されているトークンも多数あります。が、偏りがあるかもしれません。辞書の中身は `hiragana2tex.py` の冒頭をご覧ください。
* 辞書で解釈できなかった文字たちは、 `\text{}` で包んで出力します。その際、仮名文字は全てローマ字に置き換えられます(Google chart API が全角文字の表示に非対応のため)。
* 解釈できない文字数が最小となるように、解釈されます。

# 簡易サーバー（google chart API を叩いて数式画像へ変換する機能付き）
`hiragana2tex.py` と `server.py` をダウンロードして、 `python server.py -p 8000` を実行すると、簡易サーバーを立てることができます（`-p` でポート番号を指定してください（デフォルトは `8000` です））。立てた状態で、ブラウザ等で `localhost:8000/?いちたすにはさん` にアクセスすると（ `8000` は指定したポート番号に変えてください）、画面に「1+2=3」という数式画像が表示されます。 `いちたすにはさん` の部分を、好きな文字列に置き換えてアクセスすると、数式画像が変わります。


# FAQ
* 大文字のアルファベットは出せますか？
    
    * 「エー」「ビー」などカタカナで入力すると大文字アルファベットになります。ギリシャ文字についても同様です。

* 「しぐま」で和記号が出てきてしまいます。σを入力するにはどうすればいいですか？
    
    * 「しぐ」または「すぃぐま」(!)で出せます。ただしこの仕様は変更される可能性がやや高いです。そもそも「しぐま」でσを出せるようにして和記号を「さむ」などにすれば良いのですが、実はこのプログラムを開発した動機となっているプロジェクトが「中高生」を主にターゲットにしたものなため、「しぐま」を和記号に割り当てている、という経緯があります。（なお、「さむ」でも和記号は出せます）

* 添字は出せますか？
    
    * "えーそえじえぬ"  "えーそえじ「えぬたすいち」"  "えーそえじ　えぬたすに" 　　などで出せるようになりました（"そえじ"は"したつき"でも可）。上付き文字も「うえつき」で出るようになりました。

* ベクトルと行列は出せますか？

    * 現状未対応ですが、出せるようにしたいと思っています。
