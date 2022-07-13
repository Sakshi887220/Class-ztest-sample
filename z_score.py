import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

#Change the School data here
df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()


##  code to find the mean of 100 data points 1000 times 
#function to get the mean of the given data samples
# pass the number of data points you want  as counter
def random_set_of_mean(counter):
    dataset = []
    
    return mean


# Function to get the mean of 100 data sets
mean_list = []
for i in range(0,1000):
   


## calculating mean and standard_deviation of the sampling distribution.
std_deviation = statistics.stdev(mean_list)




## findig the standard deviation starting and ending values

third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
# print("std1",first_std_deviation_start, first_std_deviation_end)
# print("std2",second_std_deviation_start, second_std_deviation_end)
# print("std3",third_std_deviation_start,third_std_deviation_end)




# # finding the mean of THE STUDENTS WHO GAVE EXTRA TIME TO MATH LAB and plotting on graph
df = pd.read_csv("sample_1.csv")


fig.show()




# #finding the mean of the STUDENTS WHO USED MATH PRACTISE APP and plotting it on the plot.
df = pd.read_csv("sample_2.csv")

fig.show()


# finding the mean of the STUDENTS WHO WERE ENFORCED WITH REGISTERS and plotting it on the plot.
df = pd.read_csv("sample_3.csv")

fig.show()


#finding the z score using the formula
