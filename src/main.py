import sys
import Lox

# Exit codes
EX_USAGE = 64
# global variables
global had_error
had_error: bool = False


def main():
    lox = Lox.Lox()
    if len(sys.argv) > 2:
        print("Usage: python main.py <input_file>")
        sys.exit(EX_USAGE)
    elif len(sys.argv) == 2:
        lox.run_file(sys.argv[1])
    else:
        lox.run_prompt()


if __name__ == "__main__":
    main()
