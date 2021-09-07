import math
import sys


def convert_to_int():
    tab = []
    for i in range (1, 10):
        tab.append(int(sys.argv[i]))
    sum = 0
    for arg in tab:
        sum += arg
        if arg < 0:
            raise ValueError("Number must be positive")
    if sum != 100:
        raise ValueError("Sum of numbers must be 100")
    return tab


def binomial(n, k, p):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k)) * math.pow(p, k) * math.pow(1 - p, n - k)


def get_coloum_names(Ox):
    columns = [[i] for i in range(9)]
    cur_col = 0
    while cur_col < len(columns):
        if sum([Ox[j] for j in columns[cur_col]]) >= 10:
            cur_col += 1
            continue
        if (cur_col + 1 == len(columns)) or (cur_col > 0 and sum([Ox[j] for j in columns[cur_col - 1]]) < sum(Ox[j] for j in columns[cur_col + 1])):
            columns[cur_col - 1] += columns[cur_col]
            del columns[cur_col]
            cur_col -= 1
        else:
            columns[cur_col] += columns[cur_col + 1]
            del columns[cur_col + 1]
    return columns


def get_chi(Ox, tx, columns):
    su = 0
    for column in columns:
        tmp = 0
        for nb in column:
            tmp += Ox[nb] - tx[nb]
        tmp2 = 0
        for nb in column:
            tmp2 += tx[nb]
        su += math.pow(tmp, 2) / tmp2
    return su


def calc_dispri(Ox):
    su = 0
    for i, s in enumerate(Ox):
        su += (i * s)
    return su / 10000


def get_tx(dispri):
    tx = []
    for i in range (0, 8):
        tx.append(100 * binomial(100, i, dispri))
    tx.append(100 - sum(tx))
    return tx


def formating(Ox, tx, columns, chi_squared, degrees):
    lines = [[' x'], ['Ox'], ['Tx']]
    for cl in columns:
        col_Ox = 0
        col_tx = 0
        for nb in cl:
            col_Ox += Ox[nb]
            col_tx += tx[nb]
        column = ['{0}'.format(cl[0]), str(col_Ox), '%.1f' % (col_tx)]
        if len(cl) > 1 or cl[0] == 8:
            if cl[-1] != 8:
                column[0] += ('-%d' % cl[-1])
            else:
                column[0] += '+'
        for i, row in enumerate(column):
            lines[i].append(row)
    lines[0].append('Total')
    lines[1].append('100')
    lines[2].append('100')
    for row in lines:
        li = []
        first = True
        for cell in row:
            if first:
                li.append('  {:6s}'.format(cell))
                first = False
                continue
            li.append(' {:6s}'.format(cell))
        print('|'.join(li).rstrip())
