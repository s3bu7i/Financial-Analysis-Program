
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

value = input("Enter the value :")
startdate = input("Enter start date :")
enddate = input("Enter end date :")

stock = [value]
b = str(yf.download(stock , start = startdate , end=enddate))

f = open("Finance.txt", "a")
f.write(b)
f.close()


