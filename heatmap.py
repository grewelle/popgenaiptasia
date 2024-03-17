
import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set(style="white", color_codes=True)
from matplotlib import pyplot as plt



SMALL_SIZE = 16
MEDIUM_SIZE = 24
BIGGER_SIZE = 32

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

def main():

    #heatMatrix = [[0,0,0,.1,1],[.00037,0,.0012,.13,.00037]]
    #heatMatrix = [[0,0,0,.21,0],[.00075,0.0024,0,.26,.00075],[0.64, 0.19, 0.59, 0.14, 0.027], [0.46, 0.95, 0.078, 0.22, 0.38]]
    #heatMatrix = [[0,0,0,0,0,0],[0.9,0,0,0,0,0],[0.0023,0.00062,0,0,0,0],[0,0,0.02,0,0,0],[0,0,0,0.00064,0,0],[0,0,0,0,0.24,0]]
    heatMatrix = [[0.0028,0.23,1,1,1,1],[0.017,1,1,1,1,1],[1,1,1,1,1,1],[0,0.001,0.19,1,1,1],[0,0,0,0,1,1],[0,0,0,0,0.02,1]]
    fig = plt.figure(figsize=(10, 18))
    ax = sns.heatmap(heatMatrix, annot=True, vmin=0, vmax=1)
    plt.xlabel("Anemone Type")
    plt.ylabel("Treatment")
    plt.show()
    fig.savefig("heatMatrix_4.png")

main()