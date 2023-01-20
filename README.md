# connpass-client

connpass APIクライアント

## インストール

```bash
pip install git+https://github.com/fin-py/connpass-client.git
```

## つかいかた

```bash
python -m connpass_client --<パラメータ> <値>
```

`パラメータ` および `値` は [connpass API リファレンス](https://connpass.com/about/api/) を参照

> connpass API リファレンス: https://connpass.com/about/api/

### 実行例

```bash
python -m connpass_client --event_id 266898 
{'events': [{'accepted': 15,
             'address': '',
             'catch': 'CHAPTER 2 テスト関数を書く',
             'description': '<h1>概要</h1>\n'
                            '<ul>\n'
                            '<li><a '
                            'href="https://www.shoeisha.co.jp/book/detail/9784798177458" '
                            'rel="nofollow">テスト駆動Python 第2版</a> '
                            'を読むイベントです</li>\n'
                            '<li>今回は「CHAPTER 2 '
                            'テスト関数を書く」を読んだり、サンプルコードを実行したりした内容を共有します</li>\n'
                            '<li>「CHAPTER 1 '
                            'はじめてのpytest」の内容は把握している前提で進めます</li>\n'
                            '</ul>\n'
                            '<p>今回はスペシャルゲストとして、監修の <a '
                            'href="https://twitter.com/yattom" '
                            'rel="nofollow">安井 力</a> '
                            'さんにご参加いただけることになりました。冒頭に書籍の紹介をしていただきます。</p>\n'
                            '<h2>事前準備</h2>\n'
                            '<ul>\n'
                            '<li>「CHAPTER 1 '
                            'はじめてのpytest」を確認してサンプルコードが実行できるようにしてください</li>\n'
                            '<li>可能であれば「CHAPTER 2 '
                            'テスト関数を書く」の内容を確認し、練習問題を実施しておいてください</li>\n'
                            '</ul>\n'
                            '<h1>参加方法</h1>\n'
                            '<p><strong>オンラインで開催します</strong></p>\n'
                            '<ul>\n'
                            '<li><a href="https://brave.com/ja/talk/" '
                            'rel="nofollow">Brave '
                            'Talk</a>を使います、ブラウザから参加できます</li>\n'
                            '<li><strong>参加方法は「参加者への情報」を参照してください</strong></li>\n'
                            '<li><strong>マイクが使えるようにしてください</strong> '
                            '(カメラは不要です)</li>\n'
                            '</ul>\n'
                            '<h2>タイムテーブル</h2>\n'
                            '<ol>\n'
                            '<li>書籍の紹介 <a href="https://twitter.com/yattom" '
                            'rel="nofollow">@yattom</a></li>\n'
                            '<li>自己紹介</li>\n'
                            '<li>「CHAPTER 2 '
                            'テスト関数を書く」のメモ（自分なりに読んだポイントやきいてみたいこと）をまとめる</li>\n'
                            '<li>2の内容を情報共有</li>\n'
                            '</ol>',
             'ended_at': '2022-11-30T20:30:00+09:00',
             'event_id': 266898,
             'event_type': 'participation',
             'event_url': 'https://fin-py.connpass.com/event/266898/',
             'hash_tag': '',
             'lat': None,
             'limit': None,
             'lon': None,
             'owner_display_name': 'driller',
             'owner_id': 36417,
             'owner_nickname': 'driller',
             'place': 'オンライン(Brave Talk)',
             'series': {'id': 3056,
                        'title': 'fin-py',
                        'url': 'https://fin-py.connpass.com/'},
             'started_at': '2022-11-30T19:30:00+09:00',
             'title': 'テスト駆動Python 第2版 読書会#1',
             'updated_at': '2022-11-30T16:30:02+09:00',
             'waiting': 0}],
 'results_available': 1,
 'results_returned': 1,
 'results_start': 1}
```