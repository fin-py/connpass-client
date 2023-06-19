from connpass_client import ConnpassClient


def test_results():
    data = ConnpassClient().get(event_id="266898")
    assert data["results_returned"] == 1
    assert data["results_available"] == 1
    assert data["results_start"] == 1


def test_data_keys():
    data = ConnpassClient().get(event_id="266898")
    res = set(data.keys())

    assert res == set(
        ["results_start", "results_returned", "results_available", "events"]
    )
