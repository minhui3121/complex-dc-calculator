import sys

def main():
    number = sys.argv[2:len(sys.argv)-1] # Exclude push and pop
    number = "".join(number)
    if "j" not in number:
        number = number + " + j0"
    else:
        number = number.replace("-", " -").replace("+", " +").replace("j", " j")
        number = number.strip()
    print(number)
    

if __name__ == "__main__":
    main()