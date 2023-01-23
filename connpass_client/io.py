import csv
import json
import pathlib


class Writer:
    fieldnames: list = [
        "event_id",
        "title",
        "catch",
        "description",
        "event_url",
        "started_at",
        "ended_at",
        "limit",
        "hash_tag",
        "event_type",
        "accepted",
        "waiting",
        "updated_at",
        "owner_id",
        "owner_nickname",
        "owner_display_name",
        "place",
        "address",
        "lat",
        "lon",
        "series",
    ]

    def __init__(self, data: dict):
        self.data: dict = data
        self.results_returned: int = data["results_returned"]
        self.results_available: int = data["results_available"]
        self.results_start: int = data["results_start"]
        self.events: list = data["events"]

    def to_json(self, filepath: str) -> None:
        with pathlib.Path(filepath).open(mode="w") as f:
            json.dump(self.data, f)

    def to_csv(self, filepath: str) -> None:
        if len(self.events) == 0:
            print("No events.")
            return

        with pathlib.Path(filepath).open(mode="w") as f:
            writer: csv.DictWriter = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(self.events)
