import sys


def print_help():
    if len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        print("USAGE\n"
              "\t./202unsold a b\n"
              "\nDESCRIPTION\n"
              "\ta\tconstant computed from past results\n"
              "\tb\tconstant computed from past results")
        sys.exit(0)
    elif len(sys.argv) != 3:
        sys.exit(84)


def check_number(number):
    try:
        number = int(number)
        if number != float(number):
            sys.exit(84)
        if number <= 50:
            sys.exit(84)
    except ValueError:
        sys.exit(84)


def check_input():
    print_help()
    check_number(sys.argv[1])
    check_number(sys.argv[2])
