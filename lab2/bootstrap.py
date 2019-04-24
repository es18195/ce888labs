import matplotlib
matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import numpy as np
import random


def boostrap(sample, sample_size, iterations):
    bootstrap_matrix= np.zeros([iterations,sample_size])

    for i in range(iterations):
        for s in range(sample_size):
            bootstrap_matrix[i,s]=random.choice(sample)
        
    iteration_mean = np.mean(bootstrap_matrix, axis=1)
    data_mean = np.mean(iteration_mean)
    lower=np.percentile(iteration_mean,2.5)
    upper=np.percentile(iteration_mean,97.5)
    return data_mean, lower, upper


if __name__ == "__main__":
	df = pd.read_csv('./salaries.csv')

	data = df.values.T[1]
	boots = []
	for i in range(100, 100000, 1000):
		boot = boostrap(data, data.shape[0], i)
		boots.append([i, boot[0], "mean"])
		boots.append([i, boot[1], "lower"])
		boots.append([i, boot[2], "upper"])

	df_boot = pd.DataFrame(boots, columns=['Boostrap Iterations', 'Mean', "Value"])
	sns_plot = sns.lmplot(df_boot.columns[0], df_boot.columns[1], data=df_boot, fit_reg=False, hue="Value")

	sns_plot.axes[0, 0].set_ylim(0,)
	sns_plot.axes[0, 0].set_xlim(0, 100000)

	sns_plot.savefig("bootstrap_confidence.png", bbox_inches='tight')
	sns_plot.savefig("bootstrap_confidence.pdf", bbox_inches='tight')


	#print ("Mean: %f")%(np.mean(data))
	#print ("Var: %f")%(np.var(data))
	


	