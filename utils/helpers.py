import base64

from werkzeug.exceptions import BadRequest


def decode_stl(encoded_data, path):
    try:
        with open(path, "wb") as file:
            file.write(base64.b64decode(encoded_data.encode("utf-8")))
    except Exception:
        raise BadRequest("Invalid file")
