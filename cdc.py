import sys
from collections import deque

# Supported commands
COMMANDS = {"push", "pop", "add", "sub", "mul", "div", "del"}

def parse_number(tokens):
    """
    Convert a list of tokens like ['5', '+', 'j4'] to a complex number.
    """
    number_str = "".join(tokens)
    if "j" in number_str:
        number_str = number_str.replace("j", "") + "j" # This line is needed to format string properly
    return complex(number_str)

def format_complex(cplx):
    """
    Format complex number in 'a + jb' or 'a - jb' form
    """
    if cplx.real == int(cplx.real):
        real = int(cplx.real)
    else:
        real = cplx.real
    if cplx.imag == int(cplx.imag):
        imag = int(cplx.imag)
    else:
        imag = cplx.imag
    sign = "+" if imag >= 0 else "-"
    return f"{real} {sign} j{abs(imag)}"

def main():
    stack = deque()
    args = sys.argv[1:]
    result = None
    i = 0

    while i < len(args):
        cmd = args[i]

        if cmd == "push":
            # Collect tokens after push until next command or end
            j = i + 1
            number_tokens = []
            while j < len(args) and args[j] not in COMMANDS:
                number_tokens.append(args[j])
                j += 1
            stack.append(parse_number(number_tokens))
            i = j - 1  # move index to last token of this number

        elif cmd == "pop":
            if stack:
                result = stack.pop()
            else:
                print("Error: stack underflow")
                return

        elif cmd == "add":
            if stack:
                total = sum(stack)
                stack.clear()
                stack.append(total)
            else:
                print("Error: stack underflow")
                return

        i += 1

    print(format_complex(result))

if __name__ == "__main__":
    main()