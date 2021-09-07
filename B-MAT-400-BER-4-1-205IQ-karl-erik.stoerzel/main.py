import sys
import math
from error import check_arguments


def plot_density():
    u = float(sys.argv[1])
    s = float(sys.argv[2])
    for i in range(201):
        res = (1 / (s * math.sqrt(2 * math.pi))) * (math.exp(-0.5 * math.pow((i - u) / s, 2)))
        print("%d %.5f" % (i, res))


def print_until():
    u = float(sys.argv[1])
    s = float(sys.argv[2])
    res = 0
    i = 0.0
    # for i in range(int(sys.argv[3])):
    while i < int(sys.argv[3]):
        res += (1 / (s * math.sqrt(2 * math.pi))) * (math.exp(-0.5 * math.pow((i - u) / s, 2)))
        i += 0.01
    print("%.1f%% of people have an IQ inferior to %s" % (res, sys.argv[3]))


def print_between():
    u = float(sys.argv[1])
    s = float(sys.argv[2])
    res = 0
    i = int(sys.argv[3])
    while i < int(sys.argv[4]):
        res += (1 / (s * math.sqrt(2 * math.pi))) * (math.exp(-0.5 * math.pow((i - u) / s, 2)))
        i += 0.01
    print("%.1f%% of people have an IQ between %s and %s" % (res, sys.argv[3], sys.argv[4]))


def main():
    check_arguments()
    if len(sys.argv) == 3:
        plot_density()
    if len(sys.argv) == 4:
        print_until()
    if len(sys.argv) == 5:
        print_between()
