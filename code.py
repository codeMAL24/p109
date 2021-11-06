import pandas as pd
import statistics as s
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
hlist = df["Height"].tolist()

mean,median,mode = s.mean(hlist),s.median(hlist),s.mode(hlist)
print("this is the mean --->{}, \nthis is the median --->{},\nthis is the mode ---> {}  ".format(mean,median,mode))
std = s.stdev(hlist)


first_std_start,first_std_end =  mean - std, mean + std

sec_std_start,sec_std_end =  mean - (2*std), mean + (2*std)

third_std_start,third_std_end =  mean - (3*std), mean + (3*std)

fig = ff.create_distplot([hlist],["result"],show_hist = False)

fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "MEAN"))
fig.add_trace(go.Scatter(x = [first_std_start,first_std_start],y = [0,0.17],mode = "lines + markers",name = "STD1 strt"))
fig.add_trace(go.Scatter(x = [first_std_end,first_std_end],y = [0,0.17],mode = "lines + markers",name = "STD1 end"))
fig.add_trace(go.Scatter(x = [sec_std_start,sec_std_start],y = [0,0.17],mode = "lines + markers",name = "STD2 strt"))
fig.add_trace(go.Scatter(x = [sec_std_end,sec_std_end],y = [0,0.17],mode = "lines + markers",name = "STD2 end"))
fig.add_trace(go.Scatter(x = [third_std_start,third_std_start],y = [0,0.17],mode = "lines + markers",name = "STD3 strt"))
fig.add_trace(go.Scatter(x = [third_std_end,third_std_end],y = [0,0.17],mode = "lines + markers",name = "STD3 end"))
fig.show()

data_within_1_std = [result for result in hlist if result > first_std_start and result < first_std_end]
data_within_2_std = [result for result in hlist if result > sec_std_start and result < sec_std_end]
data_within_3_std = [result for result in hlist if result > third_std_start and result < third_std_end]

print("{}% of data lies within first std".format(len(data_within_1_std)*100.0/len(hlist)))
print("{}% of data lies within second std".format(len(data_within_2_std)*100.0/len(hlist)))
print("{}% of data lies within third std".format(len(data_within_3_std)*100.0/len(hlist)))

#ahhhhhhhh my hands