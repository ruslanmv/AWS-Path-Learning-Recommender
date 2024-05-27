from functools import lru_cache
from requests import Response, post
from constants import MODEL_NAME, MODEL_URL
def build_body(prompt: str) -> dict:
    return {"model": MODEL_NAME, "prompt": prompt, "stream": False}
# Please, provide the AWS Role, AWS Path,and why suggest this based on the current employee role below. Role:
@lru_cache
def ask_assistant(field_name: str) -> str:
    prompt: str = """{input}"""
    response: Response = post(MODEL_URL, json=build_body(prompt.format(input=field_name)))
    response_txt: str = response.json()["response"]
    return response_txt
