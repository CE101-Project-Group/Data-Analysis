import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def Histogram(): 
    x = np.array([
    [1, 2, 2],
    [1, 1, 2],
    [2, 4, 3],
    ])

    data = tuple(x.mean(axis=0))

    index = np.arange(3)
    bar_width = 0.5

    plt.bar(index, data, bar_width)
    plt.xticks(index, ('Garage', 'Bedrooms', 'Storeys'))

    plt.show()

def BoxPlot():
    all_data = [125000,50000,100000,75000]
 
    fig = plt.figure(figsize=(8,6))
     
    plt.boxplot(all_data,
                notch=False, # box instead of notch shape
                sym='rs',    # red squares for outliers
                vert=True)   # vertical box aligmnent
     
    plt.xticks([y+1 for y in range(1)], ['house price'])
    plt.xlabel('price range')
    t = plt.title('Box plot')
    plt.show() 

def BarChart():
    """
    A program that charts the
    relationship between house price
    and the size of the house
    created by Connor W
    date created 28/11/18
    modified 29/11/18
    """
    # data to be plotted
    house_price = ("1000","1250","1500","1750")
    y_pos = np.arange(len(house_price))
    house_size = [75000,100000,125000,50000]

    fig, ax1 = plt.subplots()

    # plots data and information for axes
    plt.bar(y_pos, house_size, align='center', alpha=0.5, color='r')
    plt.xticks(y_pos, house_price)
    plt.ylabel('House Size')
    plt.xlabel("House Price")
    plt.title('House Price Against House Size')

    fig.tight_layout()
    plt.show()

# calls the functions
Histogram()
BoxPlot()
BarChart()
