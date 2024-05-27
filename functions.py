from os import listdir, makedirs
from os.path import isfile, join
from time import time
import pandas as pd
from constants import  PROMPTS_FOLDER
def load_prompt(filename: str) -> str:
    with open(join(PROMPTS_FOLDER, filename), "r") as f:
        return f.read()

def format_time(s: float) -> str:
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return f"{int(h)}h {int(m)}m {int(s)}s"

