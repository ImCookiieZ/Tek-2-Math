def formula(a, b, x, y):
    return ((a - x) * (b - y)) / ((5 * a - 150) * (5 * b - 150))


def show_tab_line_sum(i, tab):
    result = 0.0
    for k in range(i * 5, i * 5 + 5):
        result += tab[k]
    return result


def show_tab_column_sum(j, tab):
    result = 0.0
    k = 0
    while k < 5:
        result += tab[j]
        k += 1
        j += 5
    return result


def show_joint_law(tab):
    tab_i = 0
    print("\tX=10\tX=20\tX=30\tX=40\tX=50\tY law")
    for i in range(5):
        print("Y=%d" % ((i + 1) * 10), end="")
        for j in range(5):
            print("\t%.3f" % tab[tab_i + j], end="")
        print("\t%.3f" % show_tab_line_sum(i, tab))
        tab_i += 5
    print("X law", end="")
    for i in range(5):
        print("\t%.3f" % show_tab_column_sum(i, tab), end="")
    print("\t1.000")


def show_law(a, b):
    print("z\t20\t30\t40\t50\t60\t70\t80\t90\t100\np(Z=z)", end="")
    for i in range(9):
        sum = 0.0
        for y in range(5):
            for x in range(5):
                result = (formula(a, b, (x + 1) * 10, (y + 1) * 10))
                if x + y == i:
                    sum += result
        print("\t%0.3f" % sum, end="")
    print()


def show_variances(tab):
    expectX = 0.0
    expectY = 0.0
    varX = 0.0
    varY = 0.0
    sumX = []
    sumY = []
    for i in range(5):
        sumX.append(show_tab_column_sum(i, tab))
        sumY.append(show_tab_line_sum(i, tab))
    for i in range(5):
        expectX += sumX[i] * ((i + 1) * 10)
        expectY += sumY[i] * ((i + 1) * 10)
    for i in range(5):
        varX += pow(((i + 1) * 10 - expectX), 2) * sumX[i]
        varY += pow(((i + 1) * 10 - expectY), 2) * sumY[i]
    print("expected value of X:\t%.1f" % expectX)
    print("variance of X:\t\t%0.1f" % varX)
    print("expected value of Y:\t%.1f" % expectY)
    print("variance of Y:\t\t%0.1f" % varY)
    print("expected value of Z:\t%.1f" % (expectX + expectY))
    print("variance of Z:\t\t%0.1f" % (varX + varY))


def print_tab(a, b, tab):
    print("--------------------------------------------------------------------------------")
    show_joint_law(tab)
    print("--------------------------------------------------------------------------------")
    show_law(a, b)
    print("--------------------------------------------------------------------------------")
    show_variances(tab)
    print("--------------------------------------------------------------------------------")
