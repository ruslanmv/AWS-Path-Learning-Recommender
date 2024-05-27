from os import makedirs
from os.path import join
import pandas as pd
from assistant import ask_assistant
from functions import  load_prompt

def elaborate_field(row: pd.Series) -> pd.Series:
    if row["column_type"] == "string":
        print(
            f"Elaborating field {row['column_name']} of the file {row['filename']}... ",
            end="",
            flush=True,
        )
        tag: str = ask_assistant(row["column_name"])
        print("Tag: ", tag)
        if tag and tag != "None":
            row["tag"] = tag
    return row


def main() -> None:
    save_df(fields, join(OUTPUTS_FOLDER, "fields_generated.csv"))


# def main_old() -> None:

#     prompt: str = load_prompt(PROMPT_FILENAME)
#     ddls: list[tuple[str, str]] = extract_ddls(DDLS_FOLDER)

#     for file, ddl in ddls:
#         elaborate_ddl_old(file, prompt, ddl)


if __name__ == "__main__":
    makedirs(OUTPUTS_FOLDER, exist_ok=True)
    main()
