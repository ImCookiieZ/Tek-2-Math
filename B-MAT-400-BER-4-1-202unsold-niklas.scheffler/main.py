#!/usr/bin/env python3
import sys

from input import check_input
from output import print_tab, formula


def calc_tab(a, b):
    tab = []
    for y in range(5):
        for x in range(5):
            tab.append(formula(a, b, (x + 1) * 10, (y + 1) * 10))
    return tab


def main():
    check_input()
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    tab = calc_tab(a, b)
    print_tab(a, b, tab)
    sys.exit(0)
