#Libraries:
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def graphs (name, values):
        
    #Use seaborn style
    sns.set_theme()

    #Create data
    #values = np.cumsum(np.random.randn(1000,1))

    plt.clf()
    #Use the plot function
    plt.hist(values, bins=30, edgecolor='black', alpha=0.7)
    plt.title('Frequency Table (Histogram)')
    #To use names for the labels
    plt.xlabel('Values')
    plt.ylabel('Frequency') 
    #To rotate the axis
    plt.xticks(rotation=45)

    #plt.plot(values)

    #Show the graph
    plt.show()


    #Code to save figure as PNG
    #tsla = [1,2,3,4]
    path = 'static/images/'+name+'.png'
    print(path)
    plt.savefig(path)

    print("graph")
    return