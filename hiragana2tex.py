# coding: utf-8
# author: @yos1up
_infty_ = 2147483640

# トークンの辞書。主にtokenizeメソッドで使われる。（コロンの右側に書いてある）valueたちを「トークン」と呼ぶ。
dictionary_misc = {
        'えー':'a',   
        'びー':'b',
        'しー':'c',
        'でぃー':'d',
        'いー':'e',
        'えふ':'f',
        'じー':'g',
        'えいち':'h',
        'あい':'i',
        'じぇー':'j',
        'けー':'k',
        'える':'l',
        'えむ':'m',
        'えぬ':'n',
        'おー':'o',
        'ぴー':'p',
        'きゅー':'q',
        'あーる':'r',
        'えす':'s',
        'てぃー':'t',
        'ゆー':'u',
        'ぶい':'v',
        'だぶりゅー':'w',
        'だぶる':'w',
        'えっくす':'x',
        'えっきす':'x',
        'えくす': 'x',
        'わい':'y',
        'ぜっと':'z',
        'エー':'A',
        'ビー':'B',
        'シー':'C',
        'ディー':'D',
        'イー':'E',
        'エフ':'F',
        'ジー':'G',
        'エイチ':'H',
        'アイ':'I',
        'ジェー':'J',
        'ケー':'K',
        'エル':'L',
        'エム':'M',
        'エヌ':'N',
        'オー':'O',
        'ピー':'P',
        'キュー':'Q',
        'アール':'R',
        'エス':'S',
        'ティー':'T',
        'ユー':'U',
        'ブイ':'V',
        'ダブリュー':'W',
        'ダブル':'W',
        'エックス':'X',
        'エッキス': 'X',
        'エクス': 'X',
        'ワイ':'Y',
        'ゼット':'Z',
        'あるふぁ': '\\alpha ',
        'べーた': '\\beta ',
        'がんま': '\\gamma ',
        'でるた': '\\delta ',
        'いぷしろん': '\\varepsilon ',
        'いーた': '\\eta ',
        'えーた': '\\eta ',
        'ぜーた': '\\zeta ',
        'ぷさい': '\\psi ',
        'ふぁい': '\\phi ',
        'ぐざい': '\\xi ',
        'くしー': '\\xi ',
        'くし': '\\xi ',
        'くさい': '\\xi ',
        'しーた': '\\theta ',
        'てーた': '\\vartheta ',
        'ろー': '\\rho ',
        'みゅー': '\\mu ',
        'にゅー': '\\nu ',
        'ぱい': '\\pi ',
        'おめが': '\\omega ',
        'たう': '\\tau ',
        'いおた': '\\iota ',
        'かっぱ': '\\kappa ',
        'らむだ': '\\lambda ',
        'すぃぐま': '\\sigma ', # これどうにかすべきだよなあ。\\sumと被ってる。
        'しぐ': '\\sigma ', # とりあえずこうしてみる
        'うぷしろん': '\\upsilon ',
        'かい': '\\chi ',
        'アルファ': '\\Alpha ',
        'ベータ': '\\Beta ',
        'ガンマ': '\\Gamma ',
        'デルタ': '\\Delta ',
        'イプシロン': '\\Epsilon ',
        'イータ': '\\Eta ',
        'エータ': '\\Eta ',
        'ゼータ': '\\Zeta ',
        'プサイ': '\\Psi ',
        'ファイ': '\\Phi ',
        'グザイ': '\\Xi ',
        'クシー': '\\Xi ',
        'クサイ': '\\Xi ',
        'シータ': '\\Theta ',
        'ロー': '\\Rho ',
        'ミュー': '\\Mu ',
        'ニュー': '\\Nu ',
        'パイ': '\\Pi ',
        'オメガ': '\\Omega ',
        'タウ': '\\Tau ',
        'イオタ': '\\Iota ',
        'カッパ': '\\Kappa ',
        'ラムダ': '\\Lambda ',
        'シグマ': '\\Sigma ', # これどうにかすべきだよなあ。\\sumと被ってる。
        'ウプシロン': '\\Upsilon ',
        'カイ': '\\Chi ',        
        'ぜろ':'0',
        'れい':'0', # 「まる」は関数の合成記号に割り当てています
        'いち':'1',
        'いっ':'1', # いってんいち
        'に':'2',
        'にー':'2',
        'にい':'2',
        'ふた':'2',
        'さん':'3',
        'よん':'4',
        'ご':'5',
        'ごー':'5', # ごおー (5o) とかがあって「ごお」を加えていない
        'ごお':'5',
        'ろく':'6',
        'ー': '', # そもそもこれで語尾の伸ばし棒を吸収できるので、他のいくつかのエントリーは消しても大丈夫なはず。ただ、一応残してある。(TODO: このエントリは妥当か？)
        'ろっ':'6',
        'なな':'7',
        'はち':'8',
        'はっ':'8',
        'きゅう':'9',
        'じゅう':'10',
        'じゅっ':'10',
        'じっ':'10',
        'ひゃく':'100',
        'びゃく': '100',
        'ぴゃく': '100',
        'せん':'1000',
        'ぜん': '1000', 
        'まん':'10000',
        'おく':'100000000',
        'ちょう':'1000000000000',
        'けい':'10000000000000000',
        'がい':'100000000000000000000',
        'じょ':'1000000000000000000000000', # 次の「じょう」がかぶる。
        'むりょうたいすう': '10000000000000000000000000000000000000000000000000000000000000000',
        'ぐーごる': '10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
        'てふ': '\\TeX ',
        'てっく': '\\TeX ',
        'てっくす': '\\TeX ',
        'じゃば': '\\textrm{JAVA + YOU, DOWNLOAD TODAY!}', # あなたとJAVA, 今すぐダウンロー　ド
        'てん':'.',
        'じょう':'^',
        'じょうこん':'^/',
        'じじょう':['2','^'],
        'ぴい':'_P_', # 順列
        'しい':'_C_', # 組み合わせ
        'ばー':'\\overline ',
        'の':'', # さんのよんじょう（いずれは、^のヒントに使うようにするかも。）
        'と':'', # きゅうとよんぶんのさん
        'か':'', # きゅうかよんぶんのさん（昔の呼び方）
        'ことの':'',
        'たす':'+',
        'ぷらす':'+',
        'ぷらまい':'\\pm ',
        'ぷらすまいなす':'\\pm ',
        'まいなすぷらす':'\\mp ',
        'まいぷら':'\\mp ',
        'ぷらぷら':'++',
        'ひく':'-',
        'まいなす':'-',
        'かける':'\\times ',
        'わる':'\\carf ', # 現状は分数となる
        'ぶんの':'\\frac ',
        'いこーる':'=',
        'は':'=',
        'のっといこーる':'\\neq ',
        'だいなりいこーる':'\\geq ',
        'しょうなりいこーる':'\\leq ',
        'だいなり':'>',
        'しょうなり':'<',
        'にありいこーる':'\\approx ',
        'にありこーる':'\\approx ',
        'ごうどう':'\\equiv ',
        'そうじ': '\\sim ',
        'どうけい': '\\cong ',
        'から':'', # いずれは、sumのヒントに使うようにするかも。
        '「':'(',
        '」':')',
        '（':'(',
        '）':')',
        '、':',',
        '。':'.',  
        '・':'\\cdot ',
        'すいちょく':'\\perp ',
        'ちょっかく':'\\perp ',
        'へいこう': '//', 
        'かく':'\\angle ',
        'ど':'^{\\circ}',
        'すたー':'^{\\star}',
        'ぷらいむ':'\'',
        'だっしゅ':'\'',
        'あすたりすく':'\\ast ',
        'どうち':'\\iff ',
        'ならば': '\\Rightarrow ',
        'かつ': '\\wedge ', # \\land は google chart APIが未対応だった
        'または': '\\vee ', # \\lor は google chart APIが未対応だった
        'ひれい':'\\propto ',
        'びっくり':'!',
        'かいじょう':'!', # 中高生は ^{\\chi} は使わないだろう。
        'あれふ':'\\aleph ',
        'むげん':'\\infty ',
        'むげんだい':'\\infty ',
        'はーと':'\\heartsuit ',
        'だいや':'\\diamondsuit ',
        'だいあ':'\\diamondsuit ',
        'すぺーど':'\\spadesuit ',
        'くらぶ':'\\clubsuit ',
        'くろーばー':'\\clubsuit ',
        'くろーば':'\\clubsuit ',
        'しゃーぷ':'\\sharp ',
        'なちゅらる':'\\natural ',
        'ふらっと':'\\flat ',
        'ふぉあおーる':'\\forall ',
        'すべて':'\\forall ',
        'にんい':'\\forall ',
        'いぐじすつ':'\\exists ',
        'ある':'\\exists ',
        'いんばーす':'^{-1}',
        'てんち':'^{T}',         
        'おーばー':'/', # これは単なる記号として
        'どっと':'\\cdot ',
        'いん':'\\in ',
        'こんていんず':'\\ni ',
        'さぶせっと':'\\subset ',
        'さぷせっと':'\\supset ',
        'すーぷせっと':'\\supset ',
        'すーぱーせっと':'\\supset ',
        'きゃっぷ':'\\cap ',
        'きょうつうぶぶん':'\\cap ',
        'かっぷ':'\\cup ',  
        'わしゅうごう':'\\cup ',
        'さしゅうごう':'\\setminus ',
        'せっとまいなす':'\\setminus ',
        'くうしゅうごう':'\\emptyset ',
        'ほしゅうごう':'^{c}',
        'さんかっけい':'\\triangle ',
        'さんかくけい':'\\triangle ',
        'やじるし':'\\rightarrow ',   
        'が':'\\rightarrow ', # limの矢印って　えぬがむげんだいって言いません？ 
        'を':'\\rightarrow ', # limの矢印って　えぬをむげんだいって言いません？ 
        'なぶら':'\\nabla ',   
        'もど':'\\bmod ',               
        'もっど':'\\bmod ',
        'もじゅろ': '\\bmod ',
        'みっど': '\\mid ',
        'みど': '\\mid ', # 縦棒。割り切る記号
        'しぜんすう': '\\mathbb{N}',
        'せいすう': '\\mathbb{Z}',
        'ゆうりすう': '\\mathbb{Q}',
        'じっすう': '\\mathbb{R}',
        'ふくそすう': '\\mathbb{C}',
        'しげんすう': '\\mathbb{H}',
        'くおたにおん': '\\mathbb{H}',
        'はちげんすう': '\\mathbb{O}',
        'おくたにおん': '\\mathbb{O}',
        'じゅうろくげんすう': '\\mathbb{S}',
        'そすう': '\\mathbb{P}', # これ使われてるの見たことない
        'ごうせい': '\\circ ',
        'まる': '\\circ ',
        'せくしょん': '\\S ',
        ' ':' ',
        'さいん':'\\sin ',
        'こさいん':'\\cos ',
        'こす':'\\cos ',
        'たんじぇんと':'\\tan ',
        'たん':'\\tan ',
        'あーくこさいん': '\\arccos ',
        'あーくさいん': '\\arcsin ',
        'あーくたんじぇんと': '\\arctan ',
        'はいぱぼりっくこさいん': '\\cosh ',
        'はいぱぼりっくさいん': '\\sinh ',
        'はいぱぼりっくたんじぇんと': '\\tanh ',
        'せかんと': '\\sec ',
        'こせかんと': '\\csc ',
        'こたんじぇんと': '\\cot ',
        'よげんていり': '{AC^2 = AB^2 + BC^2 - 2AB\\cdot BC\\cos B}',
        'せいげんていり': '{\\frac{AB}{\\sin C} = \\frac{BC}{\\sin A} = \\frac{CA}{\\sin B}}',
        'おいらーのこうしき': '{e^{i\\pi} = -1}',
        'どもあぶるのていり': '{e^{i\\theta} = \\cos\\theta + i\\sin\\theta}',
        'かほうていり': '{\\sin(x+y) = \\sin x \\cos y + \\cos x \\sin y, \\cos(x+y) = \\cos x \\cos y - \\sin x \\sin y}',
        'ぴたごらすのていり': '{AB^2 + BC^2 = AC^2}',
        'さんへいほうのていり': '{AB^2 + BC^2 = AC^2}',
        'ちゅうせんていり': '{AB^2 + AC^2 = 2(AM^2 + BM^2)}',
        'とれみーのていり': '{AB\\cdot CD + BC\\cdot DA = AC\\cdot BD}',
        'いいよこいよ': '{114514}',
        'なんでやはんしんかんけいないやろ': '{334}',
        'なんでや！はんしんかんけいないやろ': '{334}', # 末尾の！は階乗になる。
        'じんるいうちゅうすべてのこたえ':'{42}',
        'じんるい、うちゅう、すべてのこたえ':'{42}'
}
dictionary_func = { # 関数　自動で括弧がついたり特殊処理が行われたりする。
        # TODO: 三角関数はここに加えず単に記号とした方が良い？
        # TODO: 「るーと」はここよりも「じょう」「じょうこん」「ぶんの」あたりと同じ括りの方が良いかも？
        # むしろそいつらをここに持ってきた方が良いかも
        'るーと':'\\sqrt ',
        'びぶんでぃー1':'\\diffd1 ', # これらはdetect_diffによって発生します
        'びぶんでぃー2':'\\diffd2 ',         
        'ろぐ':'\\log ',
        'ろがりずむ':'\\log ', 
        'ぜったいち':'\\abs ',
        'あぶす':'\\abs ',
        'のるむ':'\\norm ',
        'がうす':'\\gauss ', # ガウス関数
        'ふろあ':'\\floor ',
        'しーる':'\\ceil ',
        'り':'\\Re ',
        'いむ':'\\Im ', # これらの読み方は一般的か？
        'あーぐ':'\\arg ',
        'いくすぷ': '\\exp ',
        'えくすぷ': '\\exp ',
        'でっと': '\\det ',
        'とれーす': '\\textrm{tr} ',
        'とら': '\\textrm{tr} ',
        'とれ': '\\textrm{tr} ', # なんて読むんだろう？
        'らんく': '\\textrm{rank} ',
        'ほむ': '\\hom ',
        'かーねる': '\\textrm{Ker} ',
        'いめーじ': '\\textrm{Im} ',
        'おーと': '\\textrm{Aut} ',
        'えんど': '\\textrm{End} ',
        'とー': '\\textrm{Tor} ',
        'とーじょん': '\\textrm{Tor} ',
        'えくすと': '\\textrm{Ext} ',
        'いくすと': '\\textrm{Ext} ',
        'おーど': '\\textrm{ord} ',
        'おーだ': '\\textrm{ord} ',
        'おーだー': '\\textrm{ord} ', # ord_p 下付きにできるのと読み分ける？
        'でぃぐ': '\\textrm{deg} ',
        'でぐ': '\\textrm{deg} ',
        'でぃぐりー': '\\textrm{deg} ',
        'でぐりー': '\\textrm{deg} ',
        'でぃむ': '\\textrm{dim} ',
        'でぃめんじょん': '\\textrm{dim} ',
        'でぃぶ': '\\textrm{div} ',
        'ろっと': '\\textrm{rot} ',
        'ろーと': '\\textrm{rot} ',
        'ぐらっど': '\\textrm{grad} ',
        'ぐらど': '\\textrm{grad} ',
        'ぐらーど': '\\textrm{grad} ',
        'かーる': '\\textrm{curl} ',
        'れる': '\\textrm{ReLU} ',
        'れるー': '\\textrm{ReLU} ',
        'えるー': '\\textrm{ELU} ',
        'いーえるゆー': '\\textrm{ELU} ',
        'そふとまっくす': '\\textrm{softmax} ',
        'えるふ': '\\textrm{erf} ', # 言わないか。
        'あいあいでぃー': '\\textrm{i.i.d.} ',
        'じーしーでぃー': '\\textrm{gcd} ', # この辺は誤爆する人いないかな・・・？
        'えるしーえむ': '\\textrm{LCM} '
}
dictionary_sym_sub = { # _ で真下に式が書かれる記号たち（関数としては処理しない）
        'まっくす':'\\max ',
        'みにまむ': '\\min ',
        'みん': '\\min ',
        'すーぷ': '\\sup ',
        'いんふ': '\\inf ',
        'りみっと': '\\lim ',
        'りむ': '\\lim ',
        'りむすーぷ': '\\limsup ',
        'りむいんふ': '\\liminf ',
        'あーぐまっくす': '{\\mathrm arg~max}\\limits ',
        'あーぐみにまむ': '{\\mathrm arg~min}\\limits ',
        'あーぐみん': '{\\mathrm arg~min}\\limits ',
}
dictionary_sym_sub_sup = { # _ で真下に、^ で真上に式が書かれる記号たち（関数としては処理しない）
        'しぐま':'\\sum ',
        'さむ':'\\sum ',
        'わきごう':'\\sum ',
        'さめーしょん':'\\sum ',
        'ぷろだくと':'\\prod ',
        'ぷろど':'\\prod ',
        'ぷろっど': '\\prod ',
        'せききごう':'\\prod ',
        'せきぶん':'\\int ',
        'いんてぐらる':'\\int ',            
        'いんと':'\\int '
}
# TODO: 優先度のたかそうなものを列挙：単位系、添え字の記述法を考える（とりあえずはカッコ・・・）、

dictionary = {}
for d in [dictionary_misc, dictionary_func, dictionary_sym_sub, dictionary_sym_sub_sup]:    
    dictionary.update(d)
tokens_func = {v for v in dictionary_func.values()}
tokens = {v if isinstance(v, str) else '' for v in dictionary.values()} # listはunhashableなので避けている
tokens_sym_sub_sup = {v for v in dictionary_sym_sub_sup.values()}
tokens_sym_sub = {v for v in dictionary_sym_sub.values()}
dictionary_maxlength = max([len(s) for s in dictionary.keys()])


roman = ['a','a','i','i','u','u','e','e','o','o',
        'ka','ga','ki','gi','ku','gu','ke','ge','ko','go',
        'sa','za','shi','ji','su','zu','se','ze','so','zo',
        'ta','da','chi','di','tsu','tsu','zu','te','de','to','do',
        'na','ni','nu','ne','no','ha','ba','pa','hi','bi','pi',
        'fu','bu','pu','he','be','pe','ho','bo','po',
        'ma','mi','mu','me','mo','ya','ya','yu','yu','yo','yo',
        'ra','ri','ru','re','ro','wa','wa','wi','we','wo','n','vu','ka','ke']
def kana2roman(s):
    '''
    s: 文字列
    returns: カナだけローマ字読みに差し替えられた文字列
    ※ これはgoogle chart APIが日本語に対応していないので便宜的に作成したものです。
    「きゅうりょう」を kyuuryou などとする機能はありません。kiyuuriyou となるだけです。
    '''
    ret = ''
    for c in s:
        idx = -1
        if (0<=ord(c)-ord('ぁ')<len(roman)):
            idx = ord(c) - ord('ぁ')
        elif (0<=ord(c)-ord('ァ')<len(roman)):
            idx = ord(c) - ord('ァ')
        ret += (roman[idx] if idx>=0 else c)
    return ret

def tokenize(sentence):
    '''
    トークンに切り出す
    sentence <str> : （主にひらがなで構成された）文字列
    returns: <list of str> : トークンのリスト。（それぞれのトークンは文字列）
    '''
    sentence = ''.join([c if (c!='　') else '  ' for c in list(sentence)]) # 全角空白を半角空白2個に変換
    # 解釈不能文字数が最小となるような切り分け方を、動的計画法で求める
    dp = [_infty_] * (len(sentence)+1)
    memo = [1] * (len(sentence)+1)
    dp[0] = 0
    for i in range(1,len(sentence)+1):
        if (dp[i] > dp[i-1] + 1):
            dp[i] = dp[i-1] + 1 # 最後の1文字を解釈しない
            memo[i] = 1
        for j in range(1,dictionary_maxlength+1)[::-1]: # 最後のj文字を（可能ならば）解釈する（jは大きい方が良い）
            if (i<j): continue
            if (sentence[i-j:i] in dictionary):
                if (dp[i] > dp[i-j]):
                    dp[i] = dp[i-j]
                    memo[i] = j
    # 結果をもとに、トークンの列を作成（memoを頼りに遡る）
    tokenized_sentence = []
    offs = len(sentence)
    while offs > 0:
        try:
            item = dictionary[sentence[offs-memo[offs]:offs]]
        except KeyError:
            item = '\\text{'+''.join([c if c!='\\' else '\\backslash' for c in kana2roman(sentence[offs-1])])+'}'
        if isinstance(item, str):
            tokenized_sentence.append(item)
        elif isinstance(item, list):
            tokenized_sentence += item[::-1]
        else:
            raise ValueError
        offs -= memo[offs]
    # 反転
    tokenized_sentence = tokenized_sentence[::-1]
    # 最後に、連続する半角空白をconcatする。
    ret = []
    buf = ''
    for i in range(len(tokenized_sentence)):
        if (tokenized_sentence[i]==' '):
            buf += ' '
        else:
            if (buf != ''):
                ret.append(buf)
                buf = ''
            ret.append(tokenized_sentence[i])
    # 実は最後の半角空白たちが無視されるが、処理に関係ないのでスルーする。
    return ret

def peal(s):
    '''
    両端に同数ずつ付いた括弧があればそれらを剥がす
    s: 文字列、returns: 結果の文字列
    '''
    ret = ''
    for i in range(len(s)):
        if (s[i]!='(' or s[-(i+1)]!=')'):
            return s[i:len(s)-i]
    return ret

def wrap(s, op):
    '''
    文字列を括弧で包み込む。ただしopによって、包み込む条件が異なる。下記参照。
    s: 文字列、returns: 結果の文字列、op: オプション（というか演算子 operand）

    TODO: もう少し真面目に、括弧で包み込むべき条件を考えた方が良い？
    '''
    if (op=='^'): # べきの基数をかっこで包み込むべきかを返す
        # 空白以外の文字が1文字以下、または、単一のトークンである、でなければ()で囲う
        return s if sum([c!=' ' for c in s])<=1 or s in tokens else ('(' + s + ')')
    else: # かけざんの両項を括弧で包み込むべきかを返す
        # 単項式でないなら()で包み込む
        return s if isprincipal(s) else ('(' + s + ')')

def isspaces(s):
    '''
    文字列が半角スペースだけからなるかを調べ、そうならば、文字列の長さを、そうでないならば 0　を返す。
    s: 文字列、returns: 整数
    '''
    for w in s:
        if (w != ' '): return 0
    return len(s)

def strength(op):
    '''
    演算子の結合の強さを返す。演算子でない場合は -inf を返す。
    op: トークン（文字列）、returns: intまたはfloat

    メインの処理を行うメソッドconvertでは、演算子が強い場所から順に処理されていく。
    '''
    if (op in ['\\overline ']):
        return 8
    if (op in ['\\diffd1 ', '\\diffd2 ']):
        return 7
    if (op in ['_P_', '_C_']):
        return 6
    if (op in list(tokens_sym_sub_sup)+list(tokens_sym_sub)):
        return 5
    if (op in ['^', '^/'] + list(tokens_func)):
        return 4
    if (op in ['\\times ', '\\cdot ', '\\frac ', '\\carf ']):
        return 3
    if (op in ['+', '-']):
        return 2
    if (op in ['=', '<', '>', '\\leq ', '\\geq ', '\\neq ', '\\equiv ', '\\approx ']):
        return 1
    return -_infty_

def isop(op):
    '''
    演算子かどうかを返す。
    op: トークン（文字列）、returns: bool
    '''
    return strength(op)!=-_infty_

def find_nopnop(ts, idx, d):
    '''
    トークンリスト ts の idx番目から d 方向に「非演算子が連続で並ぶところ」を探す 
    (offs, offs+d) がともに非演算子となるような最初の offs を返す。
    ただし、インデックス max(offs, offs+d) がマイナス記号の場合だけは許容する。
    （演算子だがチャンクの先頭に来うるので。この関数は、チャンクの切れ目としてふさわしい場所を探すのに使われる。）
    ts <list of str>: トークンリスト
    idx <int>: 探し始めのインデックス 
    d <1 or -1>: 探す方向
    returns <int>: 上の条件を満たす最初のoffs. 見つからなかった場合は、d<0 ならば 0, d>0 ならば len(ts)-1 が返る。
    '''
    assert(d==1 or d==-1)
    offs = idx
    while 1<=offs<len(ts)-1:
        if isop(ts[offs]) and (ts[offs]!='-' or d>0):
            offs += d
            continue
        if isop(ts[offs+d]) and (ts[offs+d]!='-' or d<0):
            offs += d
            continue
        break
    return offs

def isprincipal(s):
    '''
    トークンsが単項式かどうかを返す
    掛け算や、一部の関数(sinなど)の引数に入れるときに括弧をつける必要があるかの判定に使う
    s: 文字列、returns: bool
    '''
    # 英数字しかなかったら単項式 TODO: これは十分条件ではあるが恐らく必要条件ではない。必要十分にできるか？
    return not(sum([not('A'<=c<='Z' or 'a'<=c<='z' or '0'<=c<='9' or c==' ') for c in s]))

def remove_emptystr(ts):
    '''
    トークンリスト ts から空文字列を取り除く
    ts: <list of str>
    returns: <list of str>
    '''
    ret = []
    for i in ts:
        if (i!=''): ret.append(i)
    return ret

def find_larger_space(ts, idx, d):
    '''
    トークンリスト ts の idx番目から d 方向に「s[idx]以上の space level（i.e. isspaces の返り値）のトークン」を探し、
    存在するならば、その最初のインデックスを返す。（もちろん、s[idx]そのものは検索対象外）

    ts <list of str>: トークンリスト
    idx <int>: 探し始めのインデックス 
    d <1 or -1>: 探す方向
    returns <int>: 上の条件を満たす最初のoffs. 見つからなかった場合は、d<0 ならば -1, d>0 ならば len(ts) が返る。
    '''
    assert(d==-1 or d==1)
    if not 0<=idx<len(ts): return idx
    n = isspaces(ts[idx])
    offs = idx+d
    while 0<=offs<len(ts):
        if (n <= isspaces(ts[offs])): break
        offs += d
    return offs


def safe_index(l, target):
    '''
    リスト l において target が現れる最初のインデックスを返す。存在しない場合は -1 を返す。
    l <list> : リスト
    target : 見つけたいもの
    returns <int> : target があるインデックスのうち最も若いもの。ない場合は、-1。
    '''
    try:
        return l.index(target)
    except ValueError:
        return -1

def detect_diff(ts):
    '''
    微分のdとおぼしきものをみつけ、印をつけておく。
      ['d','d']という並びがあれば、最初のdをトークン dictionary['びぶんでぃー1'] に置換する。
      ['d','(アルファベット1文字)','d']という並びがあれば、最初のdを トークン dictionary['びぶんでぃー2'] に置換する。
    そして、いずれも、2つ目のdは削除する。
    '''
    ret = []
    i = 0
    while i < len(ts):
        if (ts[i] == 'd'):
            if (i+1<len(ts) and ts[i+1]=='d'):
                ret.append(dictionary['びぶんでぃー1'])
                i += 2
            elif (i+2<len(ts) and ts[i+2]=='d' and len(ts[i+1])==1 and ('A'<=ts[i+1][0]<='Z' or 'a'<=ts[i+1][0]<='z')):
                ret.append(dictionary['びぶんでぃー2'])
                ret.append(ts[i+1])
                i += 3
        else:
            ret.append(ts[i])
            i += 1
    return ret

def convert(tokenized_sentence):
    '''
    トークンリストをtex文字列に変換するメソッド
    tokenized_sentence <list of str> : トークンのリスト。
    returns <str> : tex 文字列

    具体的な処理は下記を参照
    '''
    ts = tokenized_sentence
    while 1: # 括弧を全て解決する。
        if (len(ts)>=100000):
            print('! WARNING: too many tokens. stop converting.')
            return ''.join(ts) # fail safe
        idx = safe_index(ts, '(')
        if (idx>=0):
            cnt = 1
            for idx2 in range(idx+1, len(ts)+1):
                if (idx2==len(ts)): break
                if (ts[idx2]=='('): cnt += 1
                elif (ts[idx2]==')'): cnt -= 1
                if (cnt==0): break
        else:
            break
        ts = ts[:idx] + ['('+convert(ts[idx+1:idx2])+')'] + ts[idx2+1:] # 括弧の中身を再帰的にconvertする。
    # この時点で、かっこは全て解決済み


    # TODO: find_nopnopを色々なところに入れていく（より空気を読むようになる。）
    while 1: # 強い演算子の周囲から順に、トークンを結合していく。
        if (len(ts)>=100000):
            print('! WARNING: too many tokens. stop converting.')
            return ''.join(ts) # fail safe
        if (len(ts)<=1): return ''.join([t if not isspaces(t) else '' for t in ts]) # 長さ0または1の場合。
        sl = [strength(w) for w in ts]
        maxstr = max(sl)
        if (maxstr==-_infty_): return ''.join([t if not isspaces(t) else '' for t in ts]) # もう演算子がない場合。

        idx = sl.index(maxstr) # 一番強い演算子 ts[idx] の周囲のトークンをこの後まとめる
        op = ts[idx]
        # TODO: トークンのグループ分けを要見直し。左右に幾つのチャンクを取るか、でまとめるのが良さそう。
        if (op in tokens_sym_sub_sup): # 真下に _で、真上に^で式を書くタイプの記号 (sum, product)
            idx2 = find_larger_space(ts, idx+1, 1)
            idx3 = find_larger_space(ts, idx2, 1)
            ts = ts[:idx] + [op+'_{'+peal(convert(ts[idx+1:idx2]))+'}^{'+peal(convert(ts[idx2:idx3]))+'}'] + ts[idx3:]
        elif (op in tokens_sym_sub): # 真下に _ で式を書くタイプの記号 (lim, )
            idx2 = find_larger_space(ts, idx+1, 1)
            ts = ts[:idx] + [op+'_{'+peal(convert(ts[idx+1:idx2]))+'}'] + ts[idx2:]
        elif (op in tokens_func): # 関数　自動で括弧がついたり特殊処理が行われたり
            # ts[idx+1]がn-spaceの時、その次の(n以上)-spaceを見つけて、そのインデックスを返す。n-spaceでない場合は、idx+2を返す。
            idx2 = find_larger_space(ts, idx+1, 1) # idx2が次の(n以上)-space
            if (op=='\\sqrt '):
                ts = ts[:idx] + ['\\sqrt{'+peal(convert(ts[idx+1:idx2]))+'}'] + ts[idx2:]
            elif (op == '\\abs '):
                ts = ts[:idx] + ['| '+peal(convert(ts[idx+1:idx2]))+'| '] + ts[idx2:]            
            elif (op == '\\norm '):
                ts = ts[:idx] + ['|| '+peal(convert(ts[idx+1:idx2]))+'|| '] + ts[idx2:]   # '\\|'認識されない？         
            elif (op == '\\gauss '):
                ts = ts[:idx] + ['[ '+peal(convert(ts[idx+1:idx2]))+'] '] + ts[idx2:]        
            elif (op == '\\floor '):
                ts = ts[:idx] + ['\\lfloor '+peal(convert(ts[idx+1:idx2]))+'\\rfloor '] + ts[idx2:]        
            elif (op == '\\ceil '):
                ts = ts[:idx] + ['\\lceil '+peal(convert(ts[idx+1:idx2]))+'\\rceil '] + ts[idx2:]
            elif (op == '\\diffd1 '): # d/dほげ
                ts = ts[:idx] + ['\\frac{d}{d'+peal(convert(ts[idx+1:idx2]))+'}'] + ts[idx2:]
            elif (op == '\\diffd2 '): # dぴよ/dほげ
                idx3 = find_larger_space(ts, idx2, 1)
                ts = ts[:idx] + ['\\frac{d'+peal(convert(ts[idx+1:idx2]))+'}{d'+peal(convert(ts[idx2:idx3]))+'}'] + ts[idx3:]
            else:
                ts = ts[:idx] + [op+'('+peal(convert(ts[idx+1:idx2]))+')'] + ts[idx2:]          
        elif (op in ['\\frac ', '\\carf ', '_P_', '_C_']): # 前後に1チャンクずつとるタイプ
            idx2 = find_larger_space(ts, idx+1, 1)
            idx3 = find_larger_space(ts, idx-1, -1)
            if (op=='\\frac '): # 分数（「ぶんの」）
                ts = ts[:max(0,idx3+1)] + ['\\frac{'+peal(convert(ts[idx+1:idx2]))+'}{'+(peal(convert(ts[idx3+1:idx])))+'}'] + ts[idx2:]
            elif (op=='\\carf '): # 分数（「わる」）
                ts = ts[:max(0,idx3+1)] + ['\\frac{'+peal(convert(ts[idx3+1:idx]))+'}{'+(peal(convert(ts[idx+1:idx2])))+'}'] + ts[idx2:]
            elif (op=='_P_'):
                ts = ts[:max(0,idx3+1)] + ['{}_{'+peal(convert(ts[idx3+1:idx]))+'}\\textrm{P}_{'+(peal(convert(ts[idx+1:idx2])))+'}'] + ts[idx2:]
            elif (op=='_C_'):
                ts = ts[:max(0,idx3+1)] + ['{}_{'+peal(convert(ts[idx3+1:idx]))+'}\\textrm{C}_{'+(peal(convert(ts[idx+1:idx2])))+'}'] + ts[idx2:]
        elif (op in ['\\overline ']): # 後ろに1チャンクとるタイプ
            idx2 = find_larger_space(ts, idx-1, -1) + 1
            ts = ts[:max(0,idx2)] + ['\\overline{'+peal(convert(ts[idx2:idx]))+'}'] + ts[idx+1:]
        elif (op in ['^', '^/']): # べき乗、べき乗根 （後ろに2チャンクとるタイプ）
            '''
            # 演算子でないものが2個連続で並んでいるところを左に検索。そこで切る。
            idx2 = find_nopnop(ts, idx-1, -1) # (idx2-1, idx2) が該当。見つからなかったらidx2==0
            idx3 = find_larger_space(ts, idx2-1, -1)
            '''
            idx2 = find_larger_space(ts, idx-1, -1) + 1            
            idx2 = find_nopnop(ts, idx2, -1)
            idx3 = find_larger_space(ts, idx2-1, -1) #TODO：リファクタリング。idx2, idx3がチャンクの先頭になるように書き換えたい        
            if (op=='^'):
                ts = ts[:max(0,idx3+1)] + [wrap(peal(convert(ts[idx3+1:idx2])),'^')+'^{'+peal(convert(ts[idx2:idx]))+'}'] + ts[idx+1:]
            else:
                ts = ts[:max(0,idx3+1)] + ['\\sqrt['+convert(ts[idx2:idx])+']{'+peal(convert(ts[idx3+1:idx2]))+'}'] + ts[idx+1:]                
            # ts = ts[:max(0,idx2-1)] + [(ts[idx2-1] if idx2>0 else '')+'^{'+peal(convert(ts[idx2:idx]))+'}'] + ts[idx+1:]
            # ts = ts[:max(0,idx-2)] + [(ts[idx-2] if idx>1 else '')+'^{'+(peal(ts[idx-1]) if idx>0 else '')+'}'] + ts[idx+1:]
        elif(op in ['\\times ','\\cdot ']): # 掛け算
            idx2 = find_larger_space(ts, idx+1, 1)
            idx3 = find_larger_space(ts, idx-1, -1)
            ts = ts[:max(0,idx3+1)] + [wrap(peal(convert(ts[idx3+1:idx])),op)+op+wrap(peal(convert(ts[idx+1:idx2])),op)] + ts[idx2:]            
        else:  # 一般的な二項演算子 これ、もうほとんど何もやってない。
            ts = ts[:max(0,idx-1)] + [(ts[idx-1] if idx>0 and not isspaces(ts[idx-1]) else '')+ts[idx]+(ts[idx+1] if idx+1<len(ts) and not isspaces(ts[idx+1]) else '')] + ts[idx+2:]
    return ts

def concat_number(tokenized_sentence):
    '''
    トークンリストの中にある「数値」たちを一つのトークンにする
    例えば ['2','100','3','.','7','+','9','100','10000'] を['203.7','+','9000000']　にする

    このメソッドの前後で、数値トークンの意味が明確に変わってしまいます。
    なので、このメソッドは一度だけ適用するものであり、繰り返し適用するものではありません。

    TODO: そもそも最初の辞書の段階で数値トークンに「しるし」をつけておけばいいのでは？ '\\d0', '\\d1', '\\b10000' などのように。

    tokenized_sentence <list of str>: 処理したいトークンリスト
    returns <list of str>: 上記処理結果
    '''
    def isnumstr(s): # 数値トークンかどうか判定
        return (len(s)>0 and not(sum([not('0'<=c<='9') for c in s]))) or (s=='.')
    def isdigit(s): # 数値トークンが、ケタ('0'-'9')かどうか判定
        return len(s)==1 and s[0]!='.'
    ret = []
    num = 0
    num2 = 0
    dig = None
    numflg = False
    ptflg = False
    ptstr = ''     
    for i in range(len(tokenized_sentence)+1):
        # print(i, ret, num, num2, dig, numflg)
        if (i<len(tokenized_sentence) and isnumstr(tokenized_sentence[i]) and (tokenized_sentence[i]!='.' or numflg)): # '.'始まりは認めない
            if (not numflg): numflg = True
            if (ptflg): # 小数パートに入っている場合
                ptstr += tokenized_sentence[i]
            else: # まだ整数パートにいる場合
                if tokenized_sentence[i]=='.':
                    ptflg = True
                    ptstr = '.'
                elif (isdigit(tokenized_sentence[i])): # ケタ
                    if (dig!=None): # けたが2連続続いた時は、値の列が切れた時として扱う
                        # numflg = False
                        ptflg = False
                        num += num2 + dig                
                        ret.append(str(num)+ptstr)
                        ptstr = ''
                        num, num2, dig = 0, 0, None
                    dig = int(tokenized_sentence[i])
                else: # 基数
                    if (len(tokenized_sentence[i]) <= 4): # 10--1000
                        num2 += (1 if dig==None else dig) * int(tokenized_sentence[i])
                        dig = None
                    else: # 10000--
                        num2 += (0 if dig==None else dig)
                        num += num2 * int(tokenized_sentence[i])
                        num2, dig = 0, None
        else:
            if (numflg): # 数値トークンの列が切れた時
                numflg = False
                ptflg = False
                num += num2 + (0 if dig==None else dig)               
                ret.append(str(num)+ptstr)
                ptstr = ''
                num, num2, dig = 0, 0, None 
            if (i<len(tokenized_sentence)): ret.append(tokenized_sentence[i])
    return ret

def hiragana2tex(s):
    '''
    ひらがな文字列をtex文字列に変換
    s <str> : ひらがな文字列（実は「エー」で 'A'(大文字！) が出せたりとかはあるので、ひらがなだけに限ったわけではない）
    returns <str> : tex 文字列
    '''
    return convert(detect_diff(remove_emptystr(concat_number(tokenize(s)))))





# 使用例 usage
if (__name__=='__main__'):
    ex = [
    'いちたすにかけるさんひくよん',
    'にのにのにじょうじょう',
    'ななてんにぶんのにまんよんせんろくてんに',
    'いちたすにぶんのさんひくよん',
    'いちたすに　ぶんの　さんひくよん',
    'いちたすに　ぶんの　さん　　ひくよん',
    'にのごぶんのいちじょう',
    'えっくすにじょうひくわいにじょうは「えっくすたすわい」「えっくすひくわい」',
    'りむ　えっくすがむげん　えふ「えっくす」はぜろ',
    'しぐま　あいいこーるいち　えぬ　けーにじょういこーるろくぶんの　けー「けーたすいち」「にけーたすいち」',
    'にえー ぶんの  まいなすびーぷらすまいなするーと びーにじょうひくよんえーしー',
    'えーの　ぴーひくいち　じょうごうどういちもどぴー',
    'じーしーでぃー　じゅうに、じゅうはち　はろく'
    ]

    for s in ex:
        print('<<< original >>>   ',s) # 原文
        print('<<< tokenized >>>  ', tokenize(s)) # トークンにバラした段階（参考）
        print('<<< tex string >>> ', hiragana2tex(s)) # tex 文字列への変換結果
        print()

    while 1:
        s = input('>> Enter hiragana string: ')
        print('<<< tokenized >>>  ', tokenize(s)) # トークンにバラした段階（参考）
        print('<<< tex string >>> ', hiragana2tex(s)) # tex 文字列への変換結果
        print()


 # TODO: 空白だけのトークンは結合直前に空文字列に置き換える
 # TODO: 経路探索を真面目にやる　（解釈不能文字数を最小化）
 # TODO: 三角関数の扱いを「記号」に変えてみる
 # TODO: じじょう
 # TODO: しい、ぴい　に対応
 # TODO: いくつかの定理
 # TODO: バー
 # TODO: 微分でぃーでぃーえっくす

# TODO: find_nopnopを適切にして、パラメータ部分に「マイナス記号」だけが乗ったりしないようにする。
# find_good_chunk(ts,idx,d) が良いか。
# good chunkとは・・・冒頭がプラスマイナス以外の演算子でない、末尾が演算子でない

