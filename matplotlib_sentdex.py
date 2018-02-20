import matplotlib.pyplot as plt

#basic plot
x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]

plt.plot(x,y, label = 'X')
plt.plot(x2,y2, label ='X2')
plt.xlabel('Plot Number')
plt.ylabel('Important Var')
plt.title('Interesting Graph\nWow')
plt.legend()
plt.show()



#bar chart
c =[2,4,6,8,10]
d =[6,7,4,5,6]
e =[1,3,5,7,9]
f =[5,2,8,4,9]

plt.bar(c,d, label = 'Bars1', color = 'b')
plt.bar(e,f, label = 'Bars2', color = 'k')

plt.title('Interesting Graph\nWow')
plt.legend()
plt.show()





#histogram
ages = [3,45,24,55,65,34,24,37,45,36,54,74,34,35,65,87,54,34,55,56]

mybins = [0,20,40,60,80,100]
plt.hist(ages, bins =mybins, histtype='bar', rwidth = 0.8 )
plt.show()
