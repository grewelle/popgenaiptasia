import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set(style="white", color_codes=True)
from matplotlib import pyplot as plt
import pandas as pd


SMALL_SIZE = 16
MEDIUM_SIZE = 24
BIGGER_SIZE = 32

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

def main():

    #plotList = [['FL APO', 1.75, 'P'], ['FL APO', 1.62, 'P'], ['FL APO', 1.32, 'P'], ['FL APO', 1.42, 'P'], ['FL APO', 2.19, 'P'], ['FL APO', 1.43, 'P'], ['HI APO', 2.13, 'P'], ['HI APO', 2.06, 'P'], ['HI APO', 1.78, 'P'], ['HI APO', 1.49, 'P'], ['HI APO', 1.62, 'P'], ['HI APO', 1.69, 'P'], ['FL SYM A', 2.36, 'P'], ['FL SYM A', 2.58, 'P'], ['FL SYM A', 2.87, 'P'], ['FL SYM A', 1.92, 'P'], ['FL SYM A', 1.99, 'P'], ['FL SYM A', 1.97, 'P'], ['HI SYM B', 1.27, 'P'], ['HI SYM B', 1.39, 'P'], ['HI SYM B', 1.32, 'P'], ['HI SYM B', 1.76, 'P'], ['HI SYM B', 1.62, 'P'], ['HI SYM B', 1.31, 'P'], ['HI SYM A', 2.41, 'P'], ['HI SYM A', 1.62, 'P'], ['HI SYM A', 1.91, 'P'], ['HI SYM A', 1.28, 'P'], ['HI SYM A', 1.34, 'P'], ['HI SYM A', 1.61, 'P'], ['FL SYM B', 1.34, 'P'],  ['FL SYM B', 1.74, 'P'], ['FL SYM B', 1.42, 'P'], ['FL SYM B', 1.59, 'P'], ['FL SYM B', 1.37, 'P'], ['FL SYM B', 1.95, 'P'], ['FL APO', 1.80, 'G'], ['FL APO', 1.58, 'G'], ['FL APO', 1.87, 'G'], ['FL APO', 2.22, 'G'], ['FL APO', 2.02, 'G'], ['FL APO', 1.71, 'G'], ['HI APO', 0.98, 'G'], ['HI APO', 1.63, 'G'], ['HI APO', 1.62, 'G'], ['HI APO', 1.49, 'G'], ['HI APO', 1.67, 'G'], ['HI APO', 1.33, 'G'], ['FL SYM A', 3.29, 'G'], ['FL SYM A', 2.33, 'G'], ['FL SYM A', 2.07, 'G'], ['FL SYM A', 2.04, 'G'], ['FL SYM A', 1.23, 'G'], ['FL SYM A', 1.40, 'G'], ['HI SYM B', 1.13, 'G'], ['HI SYM B', 1.23, 'G'], ['HI SYM B', 1.11, 'G'], ['HI SYM B', 1.67, 'G'], ['HI SYM B', 1.58, 'G'], ['HI SYM B', 1.45, 'G'], ['HI SYM A', 1.6, 'G'], ['HI SYM A', 1.22, 'G'], ['HI SYM A', 1.23, 'G'], ['HI SYM A', 1.36, 'G'], ['HI SYM A', 1.73, 'G'], ['HI SYM A', 1.44, 'G'], ['FL SYM B', 1.32, 'G'],  ['FL SYM B', 1.22, 'G'], ['FL SYM B', 1.23, 'G'], ['FL SYM B', 1.36, 'G'], ['FL SYM B', 1.73, 'G'], ['FL SYM B', 1.44, 'G']]
    #plotList = [['FL APO', 1.12, 'P'], ['FL APO', 0.13, 'P'], ['FL APO', 3.17, 'P'], ['FL APO', 2.02, 'P'], ['FL APO', 1.51, 'P'], ['FL APO', 2.46, 'P'], ['HI APO', 5.56, 'P'], ['HI APO', 3.69, 'P'], ['HI APO', 5.31, 'P'], ['HI APO', 3.43, 'P'], ['HI APO', 4.05, 'P'], ['HI APO', 3.67, 'P'], ['FL SYM A', 2.39, 'P'], ['FL SYM A', 5.03, 'P'], ['FL SYM A', 2.16, 'P'], ['FL SYM A', 1.66, 'P'], ['FL SYM A', 2.92, 'P'], ['FL SYM A', 2.58, 'P'], ['HI SYM B', 4.32, 'P'], ['HI SYM B', 3.70, 'P'], ['HI SYM B', 1.55, 'P'], ['HI SYM B', 2.42, 'P'], ['HI SYM B', -2.10, 'P'], ['HI SYM B', -9.70, 'P'], ['HI SYM A', 9.21, 'P'], ['HI SYM A', 6.45, 'P'], ['HI SYM A', 7.49, 'P'], ['HI SYM A', 1.03, 'P'], ['HI SYM A', 0.534, 'P'], ['HI SYM A', 2.02, 'P'], ['FL SYM B', 5.52, 'P'],  ['FL SYM B', 5.08, 'P'], ['FL SYM B', 4.66, 'P'], ['FL SYM B', 1.14, 'P'], ['FL SYM B', -0.49, 'P'], ['FL SYM B', 1.26, 'P'], ['FL APO', -2.3, 'G'], ['FL APO', 0.308, 'G'], ['FL APO', 0.979, 'G'], ['FL APO', 1.51, 'G'], ['FL APO', 0.305, 'G'], ['FL APO', -0.046, 'G'], ['HI APO', 2.32, 'G'], ['HI APO', 3.16, 'G'], ['HI APO', 2.93, 'G'], ['HI APO', 3.0, 'G'], ['HI APO', 2.30, 'G'], ['HI APO', 3.91, 'G'], ['FL SYM A', 3.86, 'G'], ['FL SYM A', 4.02, 'G'], ['FL SYM A', 1.19, 'G'], ['FL SYM A', 1.35, 'G'], ['FL SYM A', -1.60, 'G'], ['FL SYM A', 1.53, 'G'], ['HI SYM B', 2.16, 'G'], ['HI SYM B', 2.82, 'G'], ['HI SYM B', 0.481, 'G'], ['HI SYM B', -0.59, 'G'], ['HI SYM B', -2.0, 'G'], ['HI SYM B', -0.09, 'G'], ['HI SYM A', 3.22, 'G'], ['HI SYM A', 1.13, 'G'], ['HI SYM A', 3.52, 'G'], ['HI SYM A', 0.292, 'G'], ['HI SYM A', 1.39, 'G'], ['HI SYM A', 1.63, 'G'], ['FL SYM B', 4.22, 'G'],  ['FL SYM B', 4.98, 'G'], ['FL SYM B', 4.00, 'G'], ['FL SYM B', 0.555, 'G'], ['FL SYM B', -0.18, 'G'], ['FL SYM B', -1.2, 'G']]
    #plotList = [['FL APO', 1.12, 'P'], ['FL APO', 0.13, 'P'], ['FL APO', 3.17, 'P'], ['FL APO', 2.02, 'P'], ['FL APO', 1.51, 'P'], ['FL APO', 2.46, 'P'], ['HI APO', 5.56, 'P'], ['HI APO', 3.69, 'P'], ['HI APO', 5.31, 'P'], ['HI APO', 3.43, 'P'], ['HI APO', 4.05, 'P'], ['HI APO', 3.67, 'P'], ['FL SYM A', 2.39, 'P'], ['FL SYM A', 5.03, 'P'], ['FL SYM A', 2.16, 'P'], ['FL SYM A', 1.66, 'P'], ['FL SYM A', 2.92, 'P'], ['FL SYM A', 2.58, 'P'], ['HI SYM B', 4.32, 'P'], ['HI SYM B', 3.70, 'P'], ['HI SYM B', 1.55, 'P'], ['HI SYM B', 2.42, 'P'], ['HI SYM B', -2.10, 'P'], ['HI SYM A', 9.21, 'P'], ['HI SYM A', 6.45, 'P'], ['HI SYM A', 7.49, 'P'], ['HI SYM A', 1.03, 'P'], ['HI SYM A', 0.534, 'P'], ['HI SYM A', 2.02, 'P'], ['FL SYM B', 5.52, 'P'],  ['FL SYM B', 5.08, 'P'], ['FL SYM B', 4.66, 'P'], ['FL SYM B', 1.14, 'P'], ['FL SYM B', -0.49, 'P'], ['FL SYM B', 1.26, 'P'], ['FL APO', -2.3, 'G'], ['FL APO', 0.308, 'G'], ['FL APO', 0.979, 'G'], ['FL APO', 1.51, 'G'], ['FL APO', 0.305, 'G'], ['FL APO', -0.046, 'G'], ['HI APO', 2.32, 'G'], ['HI APO', 3.16, 'G'], ['HI APO', 2.93, 'G'], ['HI APO', 3.0, 'G'], ['HI APO', 2.30, 'G'], ['HI APO', 3.91, 'G'], ['FL SYM A', 3.86, 'G'], ['FL SYM A', 4.02, 'G'], ['FL SYM A', 1.19, 'G'], ['FL SYM A', 1.35, 'G'], ['FL SYM A', -1.60, 'G'], ['FL SYM A', 1.53, 'G'], ['HI SYM B', 2.16, 'G'], ['HI SYM B', 2.82, 'G'], ['HI SYM B', 0.481, 'G'], ['HI SYM B', -0.59, 'G'], ['HI SYM B', -2.0, 'G'], ['HI SYM B', -0.09, 'G'], ['HI SYM A', 3.22, 'G'], ['HI SYM A', 1.13, 'G'], ['HI SYM A', 3.52, 'G'], ['HI SYM A', 0.292, 'G'], ['HI SYM A', 1.39, 'G'], ['HI SYM A', 1.63, 'G'], ['FL SYM B', 4.22, 'G'],  ['FL SYM B', 4.98, 'G'], ['FL SYM B', 4.00, 'G'], ['FL SYM B', 0.555, 'G'], ['FL SYM B', -0.18, 'G'], ['FL SYM B', -1.2, 'G']]
    plotList = [['FL APO', 7.68, 'P'], ['FL APO', 5.82, 'P'], ['FL APO', 7.54, 'P'], ['HI APO', 3.98, 'P'], ['HI APO', 3.09, 'P'],
                ['HI APO', 4.52, 'P'], ['FL SYM A', 5.56, 'P'],['FL SYM A', 4.92, 'P'], ['FL SYM A', 6.72, 'P'], ['HI SYM B', 4.91, 'P'], ['HI SYM B', 4.75, 'P'], ['HI SYM B', 4.50, 'P'],  ['HI SYM A', 5.79, 'P'], ['HI SYM A', 4.83, 'P'],
                ['HI SYM A', 5.23, 'P'], ['FL SYM B', 6.28, 'P'], ['FL SYM B', 6.13, 'P'], ['FL SYM B', 6.31, 'P'],  ['FL APO', 4.51, 'G'], ['FL APO', 4.70, 'G'],
                ['FL APO', 5.65, 'G'], ['HI APO', 2.69, 'G'], ['HI APO', 2.67, 'G'], ['HI APO', 1.96, 'G'], ['FL SYM A', 3.99, 'G'], ['FL SYM A', 3.04, 'G'],
                ['FL SYM A', 5.22, 'G'], ['HI SYM B', 3.99, 'G'], ['HI SYM B', 6.43, 'G'], ['HI SYM B', 4.23, 'G'], ['HI SYM A', 3.45, 'G'], ['HI SYM A', 3.46, 'G'],
                ['HI SYM A', 3.47, 'G'], ['FL SYM B', 9.92, 'G'], ['FL SYM B', 7.40, 'G'], ['FL SYM B', 5.84, 'G']]

    df = pd.DataFrame(plotList, columns=['Type', 'G6P', 'Treatment'])
    fig = plt.figure(figsize=(10, 18))
    ax = sns.boxplot(x="Type", y="G6P", data=df, hue="Treatment")
    plt.xlabel("Anemone Type")
    plt.ylabel("Total Glutathione")
    plt.show()
    fig.savefig("boxplot3.png")

main()