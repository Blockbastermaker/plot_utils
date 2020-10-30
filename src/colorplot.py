import numpy as np

def plot_colormap(_matrix, xticks=[], yticks=[], xlabel='XXX', ylabel='YYY',
                  cmap='Blues', figure_size=(5,5), text_size=16, output="",
                  show_fig=True, show_values=True):
    import matplotlib.pyplot as plt
    from matplotlib.pyplot import cm

    plt.figure(figsize=figure_size)
    plt.imshow(_matrix, cmap=cm.get_cmap(cmap))
    plt.xlabel(xlabel, size=text_size)
    plt.ylabel(ylabel, size=text_size)

    plt.colorbar()

    for i in range(_matrix.shape[0]):
        for j in range(_matrix.shape[1]):
            if _matrix[i, j] > np.mean(_matrix):
                c = "white"
            else:
                c = "k"
            text = plt.text(j, i, _matrix[i, j],
                            ha="center", va="center", color=c)

    if len(xticks):
        plt.xticks(np.arange(len(xticks))+0.5, xticks)

    if len(yticks):
        plt.yticks(np.arange(len(yticks))+0.5, yticks)

    if len(output):
        plt.savefig(output, dpi=500)

    if show_fig:
        plt.show()
