import sys

def check_input(data):
    graphical = False
    if (len(sys.argv) < 2):
        exit(84)
    for i in range(1, len(sys.argv)):
        found = False
        if sys.argv[i] == "-g":
            graphical = True
            continue
        if sys.argv[i] == "-t":
            continue
        for row in data:
            if row[1] == sys.argv[i]:
                found = True
        if not found:
            exit(84)
    return graphical
