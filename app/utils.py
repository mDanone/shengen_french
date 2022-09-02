import time
import base64
from io import BytesIO

import requests

import config

WAIT_DELAY = 2

def get_base64(image):
    image = image.convert("RGB")
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    return "data:image/jpeg;base64," + img_str.decode()


def get_captcha(image):
    base_64image = get_base64(image)
    response = requests.post(
        config.RU_CAPTCHA_POST_URL,
        {
            "key": config.RU_CAPTCHA_KEY,
            "body": base_64image,
            "method": "base64",
            "json": 1
        }
    )
    
    return wait_for_result(response.json()["request"])


def wait_for_result(id):
    while True:
        result = requests.get(
            config.RU_CAPTCHA_GET_URL,
            params={
                "key": config.RU_CAPTCHA_KEY,
                "id": id,
                "action": "get",
                "json":1
            }
        )
        if result.json()["status"] == 1:
            return result.json()["request"].upper()
        print(result.json())
        time.sleep(WAIT_DELAY)