from re import T
from .error import check_input
from .file import load_csv
from .output import print_countries, fit1, fit2, correlation, CalculatedData
import plotly.express as px
import pandas as pd
import sys
def main():
    total = False
    data = load_csv()
    graphical = check_input(data)
    print_countries(data)
    for i in sys.argv:
        if i == "-t":
            total = True
    fit1(data, total)
    fit2(data)
    correlation(data)
    if graphical or total:
        df = pd.DataFrame(CalculatedData, columns=["Country", "Year", "Population in Million"])
        fig = px.line(df, x="Year", y="Population in Million", color="Country", line_group="Country", hover_name="Country")
        fig.show()


