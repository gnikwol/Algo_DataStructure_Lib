# Algo_DataStructure_Lib
アルゴリズムとデータ構造のライブラリです。
ダイクストラ法やプリム法などの有名グラフアルゴリズムなどを収録しています。

## DancingLinks
２次元的な連結リストです。
２次元平面上の頂点に対するx軸方向とy軸方向の連結性を管理します。
DSU(UnionFind)があると連結性判定ができるようになります。

## imod
剰余環における逆元を計算します。すなわち、x^-1 mod (mod)の値を返します。
xとmodが互いに素でないときには正しい結果が得られません。（そもそも逆元が存在しないので）
操作の計算量O(log(max(x, mod)))

## IndexedStack
Stackと書いていますが、右側push、左側popと右側popをサポートするデータ構造です。
Stackを2つ使ってQueueを構築しています。ただし、"左側popと右側popを併用すると最悪計算量が要素数nに対してO(n)です。"
Stackとして使うかQueueとして使うか予め決めておきましょう。Indexedなのでindex指定できますができるのは値の取得のみでpopはできません。
操作あたりのならし計算量O(1)くらいだと思います。

## KMPsearch
所謂KMP法です。文字列textに文字列wordが部分文字列として入っているindexを全て出力します。驚くべきことに計算量は線形です。
また、おまけとしてperiodではword[0:i]の最小の周期長を計算できます。KMPの前計算が済んでいれば計算量O(1)です。

## LinkedList
連結リストです。要素数nの配列aを与えると連結リストを作ります。get~では要素の値を返します。eraseはもとの配列における任意のindexに相当する要素を消します。

## ReRooting(こうじちゅう)
全方位木DPとも言うのですが......ご存知でしょうか。
根付き木上のDPを行い、その後に根を移動させていくような操作をすることからRerootingと呼ばれています。
書いたのが少し前なので動作確認をしていたかどうかを忘れてしまいました。ので、少し怪しいコードです。

## SolveModlog
離散対数問題を解きます。所謂Babystep, Giantstepです。
O(sqrt(mod))程度の計算量でa^x ≡ b mod (mod)なるxを計算します。

## SparseTable
区間木ではないですが、似たようなことができます。
区間木の王、SegmentTreeと比べてできることは限られますが高速です。
冪等性のあるモノイドの区間演算をサポートします。要素数nとして、前計算にO(nlogn)、演算結果の区間クエリに対してO(1)で応答します。
updateクエリは受け付けないのでstaticなクエリに向いています。

## StarrySky（バグ）
見様見真似で作った区間木ですが、バグ取りができていません。

## StrongConnections
有向グラフの強連結成分分解を行います。
rootの指定をしてもしなくてもおそらく計算量は変わりません。

## SuffixArray
文字列のSuffixArrayを出力します。ソートが入っていて計算量はSA-ISに比べてやや遅いです。
文字列長|S|に対してO(|S|log|S|)でSAを構築します。

## Trie
トライ木です。連結の管理だけ行うのでクエリとか探索は好きに行ってください。

## TSPdp
頂点数nの有向グラフを受けてO(2^n n^2)で巡回セールスマン問題を解きます。
ナイーブなO(n!)の探索よりいくらか速いです。listの隣接行列を渡してください。
