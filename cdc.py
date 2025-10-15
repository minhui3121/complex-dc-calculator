import sys
from collections import deque

def main():
    stack = deque()
    args = sys.argv[1:]
    result = ""
    for i in range(len(args)):
        if args[i] == "push":
            number = args[i+1:len(args)-1]
            number = "".join(number)
            stack.append(number)
        elif args[i] == "pop":
            try:
                result = stack.pop()
            except IndexError:
                print("Error: stack underflow")
                return
    if "j" not in result:
        result = result + " + j0"
    else:
        result = result.replace("-", " -").replace("+", " +").replace("j", " j")
        result = result.strip()
    print(result)
    

if __name__ == "__main__":
    main()