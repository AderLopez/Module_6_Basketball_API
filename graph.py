#Libraries:
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def graphs ():
        
    #Use seaborn style
    sns.set_theme()

    #Create data
    values = np.cumsum(np.random.randn(1000,1))


    #Use the plot function
    plt.plot(values)

    #Show the graph
    plt.show()


    #Code to save figure as PNG
    #tsla = [1,2,3,4]
    plt.savefig('static/images/tsla.png')

    print("graph")
    return