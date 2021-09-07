import sys


def check_arguments():
    if len(sys.argv) < 3 or len(sys.argv) > 5:
        sys.exit(84)
    try:
        for i in range(1, len(sys.argv)):
            if i > 2 and (int(sys.argv[i]) < 0 or int(sys.argv[i]) > 200):
                sys.exit(84)
            if len(sys.argv) == 5 and int(sys.argv[3]) > int(sys.argv[4]):
                sys.exit(84)
    except ValueError:
        sys.exit(84)
