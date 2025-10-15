import sys
from collections import deque

token = ["push", "pop", "add", "sub", "mul", "div", "del"]

def main():
    stack = deque()
    args = sys.argv[1:]
    result = ""
    for i in range(len(args)):
        if args[i] == "push":
            j = 1
            while args[i + j] not in token:
                j += 1
            number = args[i+1:i+j]
            number = "".join(number)
            stack.append(number)
        elif args[i] == "pop":
            try:
                result = stack.pop()
            except IndexError:
                print("Error: stack underflow")
                return
        elif args[i] == "add":
            total = sum(int(x) for x in stack)
            stack.clear
            stack.append(str(total))
    if "j" not in result:
        result = result + " + j0"
    else:
        result = result.replace("-", " -").replace("+", " +").replace("j", " j")
        result = result.strip()
    print(result)
    

if __name__ == "__main__":
    main()