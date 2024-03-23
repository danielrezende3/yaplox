import sys
from typing import List
import my_token
import my_scanner


def main():
    if len(sys.argv) > 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)
    elif len(sys.argv) == 2:
        run_file(sys.argv[1])
    else:
        run_prompt()


def run_prompt():
    while True:
        input_str = input("> ")
        if input_str == "exit()":
            break
        run(input_str)


def run_file(run_file):
    read_bytes: bytes
    with open(run_file, "rb") as file:
        read_bytes = file.read()
        run(str(read_bytes, "utf-8"))


def run(source: str):
    scanner = my_scanner.Scanner(source)
    tokens: List[my_token.Token] = scanner.scan_tokens()

    for token in tokens:
        print(token)


def error(line: int, message: str):
    report(line, "", message)


def report(line: int, where: str, message: str):
    print(f"[line {line}] Error{where}: {message}")


if __name__ == "__main__":
    main()
