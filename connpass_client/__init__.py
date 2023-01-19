def main() -> None:
    import argparse
    import dataclasses
    import os
    from pprint import pprint

    from connpass_client.client import ConnpassClient

    parser = argparse.ArgumentParser()
    parser.add_argument("key")
    parser.add_argument("value")
    args = parser.parse_args()
    client = ConnpassClient()
    pprint(client.get(args.key, args.value))