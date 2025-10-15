import sys

def main():
    number = sys.argv[2]
    if "j" not in number:
        number = number + " + j0"
    else:
        number = number.replace("-", " -").replace("j", " j")
        number = number.strip()
    print(number)
    

if __name__ == "__main__":
    main()