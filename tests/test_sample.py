from typer.testing import CliRunner

import connpass_client
from connpass_client import ConnpassClient


def test_results():
    data = ConnpassClient().get(event_id="266898")
    assert data["results_returned"] == 1
    assert data["results_available"] == 1
    assert data["results_start"] == 1


def test_main_stdout():
    expected_result = """Usage: main [OPTIONS]

Options:
  --event-id INTEGER              イベント毎に割り当てられた番号で検索します。複数指定可能です
  --keyword TEXT                  イベントのタイトル、キャッチ、概要、住所をAND条件部分一致で検索します。複数指定可能です
  --keyword-or TEXT               イベントのタイトル、キャッチ、概要、住所をOR条件部分一致で検索します。複数指定可能です
  --ym INTEGER                    指定した年月に開催されているイベントを検索します。複数指定可能です
  --ymd INTEGER                   指定した年月日に開催されているイベントを検索します。複数指定可能です
  --nickname TEXT                 指定したニックネームのユーザが参加しているイベントを検索します。複数指定可能です
  --owner-nickname TEXT           指定したニックネームのユーザが管理しているイベントを検索します。複数指定可能です
  --series-id INTEGER             グループ 毎に割り当てられた番号で、ひもづいたイベントを検索します。複数指定可能です
  --start INTEGER                 検索結果の何件目から出力するかを指定します
  --order INTEGER                 検索結果の表示順を、更新日時順、開催日時順、新着順で指定します
  --count INTEGER                 検索結果の最大出力データ数を指定します
  --format TEXT                   レスポンスの形式を指定します
  --json TEXT                     指定したファイルにJSON形式で保存します
  --csv TEXT                      指定したファイルにCSV形式で保存します
  --version / --no-version        バージョンを表示します  [default: no-version]
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit."""
    runner = CliRunner()
    result = runner.invoke(connpass_client.app, ["--help"])
    with open("a.txt", "w") as f:
        f.write(result.stdout)
    assert expected_result == result.stdout.rstrip()
