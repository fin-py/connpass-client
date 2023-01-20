import argparse
from pprint import pprint

from connpass_client.client import ConnpassClient


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--event_id")
    parser.add_argument("--keyword")
    parser.add_argument("--keyword_or")
    parser.add_argument("--ym")
    parser.add_argument("--ymd")
    parser.add_argument("--nickname")
    parser.add_argument("--owner_nickname")
    parser.add_argument("--series_id")
    parser.add_argument("--start")
    parser.add_argument("--order")
    parser.add_argument("--count")
    parser.add_argument("--format")
    args = parser.parse_args()
    client = ConnpassClient()
    pprint(
        client.get(
            event_id=args.event_id,
            keyword=args.keyword,
            keyword_or=args.keyword_or,
            ym=args.ym,
            ymd=args.ymd,
            nickname=args.nickname,
            owner_nickname=args.owner_nickname,
            series_id=args.series_id,
            start=args.start,
            order=args.order,
            count=args.count,
            format=args.format,
        )
    )
