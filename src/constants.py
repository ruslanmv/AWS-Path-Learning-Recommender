from os.path import abspath, dirname, join

MODEL_URL: str = "http://localhost:11434/api/generate"
MODEL_NAME: str = "aws-path-learning"

BASE_DIR: str = dirname(abspath(join(__file__, "..")))
PROMPTS_FOLDER: str = join(BASE_DIR, "prompts")
