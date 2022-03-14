'''

Matplotlib code 

'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


'''
Line Graph

'''


year = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
temp_index= [0.72,0.61,0.65,0.68,0.75,0.90,1.02,0.93,0.85,0.99,1.02]

plt.plot(year,temp_index)

plt.xlabel("Year")
plt.ylabel("Temprature")
plt.title("Global Warming",{'fontsize' : 14, 'horizontalalignment':'center' })
plt.show()


#  New Graph
month = ['Jan','Feb','March','April','May','June','July','Aug','Sep','Oct','Nov','Dec']
costomer1 = [12,13,9,8,7,8,8,7,6,5,8,10]
costomer2 = [14,16,11,7,6,6,7,6,5,8,9,12]
plt.plot(month,costomer1,color='red',label = "costomer1",marker='o')
plt.plot(month,costomer2,color ='blue',label = "costomer2",marker='^')
plt.xlabel("Months")
plt.ylabel("Energy Consumtion")
plt.title("Building the Consumtion")
plt.legend()
plt.show()

# Subgraph
#plt.figure()
plt.subplot(1,2,1)
plt.plot(month,costomer1,color='red',label = "costomer1",marker='o')
plt.xlabel("Costomer1")
plt.ylabel("Energy Consumtion")
plt.title("Building Energy Consumtion of Costomer1")
plt.legend()


plt.subplot(1,2,2)
plt.plot(month,costomer2,color ='blue',label = "costomer2",marker='^')
plt.xlabel("Costomer2")
plt.title("Building Energy Consumtion of Coustomer 2")
plt.legend()
plt.show()


'''

Scatter Graph
'''

month = ['Jan','Feb','March','April','May','June','July','Aug','Sep','Oct','Nov','Dec']
costomer1 = [12,13,9,8,7,8,8,7,6,5,8,10]
costomer2 = [14,16,11,7,6,6,7,6,5,8,9,12]
plt.scatter(month,costomer1,color='red',label = "costomer1")
plt.scatter(month,costomer2,color ='blue',label = "costomer2")
plt.xlabel("Months")
plt.ylabel("Energy Consumtion")
plt.title("Building the Consumtion")
plt.legend()
plt.grid()
plt.show()




'''
Histogram 
'''
plt.hist(costomer1,bins= 10,color= 'red')
plt.ylabel("Energy Consumtion")
plt.title("Histogram")
plt.show()


'''
Bar charts //Diffrecne b/w hsitogram and bar charts

Histrogram is distibution of data in probability form but bar chart is actual number
'''

plt.bar(month, costomer1,width= 0.8, color ='blue')
plt.show()

# try to build the two costomer bar graph
plt.bar(month, costomer1,width= 0.8, color ='blue',label ="Costomer1")
plt.bar(month, costomer2,width= 0.8, color ='red',label ="Costomer2")
plt.xlabel("Months")
plt.ylabel("Energy Consumtion")
plt.title("Building the Consumtion")
plt.legend()
plt.show()


# bar cahrt of two customer not solve my probem so we need a prallel so see the
# reslults

bar_width = 0.4
month_b = np.arange(12)
plt.bar(month_b,costomer1,bar_width,color = 'red',label= "Costomer1")
plt.bar(month_b+bar_width,costomer2,bar_width,color = 'blue',label= "Costomer2")
# assosiate that number to months
plt.xticks(month_b + (bar_width)/12,('Jan','Feb','March','April','May','June','July','Aug','Sep','Oct','Nov','Dec'))
plt.xlabel("Months")
plt.ylabel("Energy Consumtion")
plt.title("Building the Consumtion")
plt.legend()
plt.show()

'''
Box plot
'''
# single box plot
plt.boxplot(costomer1,notch =True,vert=True)


# parralel box plots
plt.boxplot([costomer1,costomer2],patch_artist = True,
             boxprops =dict(facecolor ='red',color='red'),
             whiskerprops = dict(color = 'green'),
             capprops = dict(color = 'blue'),
             medianprops=dict(color='yellow'))
plt.show()


