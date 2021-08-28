import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics
import pandas as pd

df = pd.read_csv("class109\StudentsPerformance.csv")
reading=df["reading score"].tolist()

mean = sum(reading)/len(reading)
median = statistics.median(reading)
mode = statistics.mode(reading)
standardDeviation=statistics.stdev(reading)

print("Mean is :", mean)
print("Median is :",median)
print("Mode is ", mode)
print("Standard Deviation is :", standardDeviation)

fig = ff.create_distplot([reading],["Result"],show_hist=False)
fig.show()

first_std_deviation_start, first_std_deviation_end = mean-standardDeviation, mean+standardDeviation
second_std_deviation_start, second_std_deviation_end = mean-(2*standardDeviation), mean+(2*standardDeviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*standardDeviation), mean+(3*standardDeviation)

list_of_data_within_1_std_deviation = [result for result in reading if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in reading if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in reading if result > third_std_deviation_start and result < third_std_deviation_end]

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(reading)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(reading)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(reading)))