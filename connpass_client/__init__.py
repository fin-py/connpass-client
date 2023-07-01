from pprint import pprint

import typer
from typing_extensions import Annotated

from connpass_client.client import ConnpassClient
from connpass_client.io import Writer

app = typer.Typer()


@app.command()
def main(
    event_id: Annotated[
        str, typer.Option(help="イベント毎に割り当てられた番号で検索します。複数指定可能です")
    ] = None,
    keyword: Annotated[
        str, typer.Option(help="イベントのタイトル、キャッチ、概要、住所をAND条件部分一致で検索します。複数指定可能です")
    ] = None,
    keyword_or: Annotated[
        str, typer.Option(help="イベントのタイトル、キャッチ、概要、住所をOR条件部分一致で検索します。複数指定可能です")
    ] = None,
    ym: Annotated[str, typer.Option(help="指定した年月に開催されているイベントを検索します。複数指定可能です")] = None,
    ymd: Annotated[str, typer.Option(help="指定した年月日に開催されているイベントを検索します。複数指定可能です")] = None,
    nickname: Annotated[
        str, typer.Option(help="指定したニックネームのユーザが参加しているイベントを検索します。複数指定可能です")
    ] = None,
    owner_nickname: Annotated[
        str, typer.Option(help="指定したニックネームのユーザが管理しているイベントを検索します。複数指定可能です")
    ] = None,
    series_id: Annotated[
        str, typer.Option(help="グループ 毎に割り当てられた番号で、ひもづいたイベントを検索します。複数指定可能です")
    ] = None,
    start: Annotated[str, typer.Option(help="検索結果の何件目から出力するかを指定します")] = None,
    order: Annotated[str, typer.Option(help="検索結果の表示順を、更新日時順、開催日時順、新着順で指定します")] = None,
    count: Annotated[str, typer.Option(help="検索結果の最大出力データ数を指定します")] = None,
    format: Annotated[str, typer.Option(help="レスポンスの形式を指定します")] = None,
    json: Annotated[str, typer.Option(help="指定したファイルにJSON形式で保存します")] = None,
    csv: Annotated[str, typer.Option(help="指定したファイルにCSV形式で保存します")] = None,
) -> None:
    data: dict = ConnpassClient().get(
        event_id=event_id,
        keyword=keyword,
        keyword_or=keyword_or,
        ym=ym,
        ymd=ymd,
        nickname=nickname,
        owner_nickname=owner_nickname,
        series_id=series_id,
        start=start,
        order=order,
        count=count,
        format=format,
    )
    if all((json is None, csv is None)):
        pprint(data)
    if json:
        Writer(data).to_json(json)
    if csv:
        Writer(data).to_csv(csv)
