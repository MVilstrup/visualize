# I have not had the time to test this method, 
# so do not use it in its current state

def remove_borders(axes, left=False, bottom=False, right=False, top=False):
    """
    A function to remove chartchunks from matplotlib plots
    such as axes, spines, ticks and labels

    Params:
            @axes : An iterable
            axes should contain plt.gca() or plt.subplot() objects, e.g. [plt.gca()]

            Four bools to indicate what parts of the plot to hide

            @left : bool    (Default: False)
            
            @bottom : bool  (Default: False)

            @right : bool   (Default: False)

            @top : bool     (Default: False)
    """

    for ax in axes:
        ax.spines["left"].set_visible(not left)
        ax.spines["bottom"].set_visible(not bottom)
        ax.spines["right"].set_visible(not right)
        ax.spines["top"].set_visible(not top)

        if left:
            ax.tick_params(left="off", labelleft="off")
        if bottom:
            ax.tick_params(bottom="off", labelbottom="off")
        if right:
            ax.tick_params(right="off")
        if top:
            ax.tick_params(top="off")
