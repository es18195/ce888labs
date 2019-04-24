import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# There are far
# better ways of doing this

if __name__ == "__main__":
    vehicles = pd.read_csv('./vehicles.csv')
    
    sns_plot = sns.lmplot(vehicles.columns[0], vehicles.columns[1], data=vehicles,fit_reg=False)
    print((vehicles))
    
    sns_plot.axes[0,0].set_ylim(0,)
    sns_plot.axes[0,0].set_xlim(0,)
    
    sns_plot.savefig("vehicle_scaterplot.png",bbox_inches='tight')
    sns_plot.savefig("vehicle_scaterplot.pdf",bbox_inches='tight')

    
    data = vehicles.values.T[0]
    plt.clf()
    sns_plot2 = sns.distplot(data, bins=20, kde=False, rug=True).get_figure()
    
    axes = plt.gca()
    axes.set_xlabel('Current fleet') 
    axes.set_ylabel('Amount')

    sns_plot2.savefig("vehicle_histogram_current.png",bbox_inches='tight')
    sns_plot2.savefig("vehicle_histogram_current.pdf",bbox_inches='tight')
    
    data2 = vehicles.values.T[1,0:79]
    plt.clf()
    sns_plot2 = sns.distplot(data2, bins=20, kde=False, rug=True).get_figure()
    
    axes = plt.gca()
    axes.set_xlabel('newt fleet') 
    axes.set_ylabel('Amount')

    sns_plot2.savefig("vehicle_histogram_new.png",bbox_inches='tight')
    sns_plot2.savefig("vehicle_histogram_new.pdf",bbox_inches='tight')

### part 2
    
    mean_old = np.mean(data)
    mean_new = np.mean(data2)
    [meanold,lower_old,upper_old]=boostrap(data, data.shape[0], 10000)
    [meannew,lower_new,upper_new]=boostrap(data2, data.shape[0], 10000)
    print("old, lower: ",str(lower_old) ," upper: ",str(upper_old))
    print("new, lower: ",str(lower_new) ," upper: ",str(upper_new))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    