import json
from typing import Union
from urllib.request import urlopen


def make_request(url: str) -> Union[str, dict]:
    with urlopen(url) as response:
        body = response.read()
        try:
            output = json.loads(body)
        except json.decoder.JSONDecodeError:
            output = body
    return output
