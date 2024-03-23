import sys
from typing import List

# Exit codes
EX_DATAERR = 65


class Lox:

    had_error: bool = False

    def run_prompt(self):
        while True:
            input_str = input("> ")
            if input_str == "exit()":
                break
            self.run(input_str)

    def run_file(self, run_file: str):
        read_bytes: bytes
        with open(run_file, "rb") as file:
            read_bytes = file.read()
            self.run(str(read_bytes, "utf-8"))
        if self.had_error:
            sys.exit(EX_DATAERR)

    def run(self, source: str):
        # scanner = my_scanner.Scanner(source)
        # tokens: List[my_token.Token] = scanner.scan_tokens()

        # for token in tokens:
        #     print(token)
        pass

    def error(self, line: int, message: str):
        self.report(line, "", message)

    def report(self, line: int, where: str, message: str):
        print(f"[line {line}] Error{where}: {message}")
        self.had_error = True
