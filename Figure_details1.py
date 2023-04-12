from matplotlib import pyplot as plt

class FigDetails():

    # Title............
    subtitles = ["Fig-1 title", "Fig-2 title", None]
    titles = {
        "Fig_1": ["Errors", None],
        "Fig_2": ["(1)", "(2)", "(3)", "(4)", None]
    }

    # labels..........
    xlabels = ["Time (s)", "Data Points"]
    ylabels = ["Error (mm)", "Error (m)"]



    # axis limits......
    xlims = [5, 6]
    ylims = [7, 8]

    # Legends.........
    legends_dict = {
        "Fig_1": ["Pitch", "Yaw"],
        "Fig_2": ["P", "Y"],
        "Fig_3": [],
        "Fig_4": [],
        "Fig_5": [],
        "Fig_6": [],
        "Fig_7": [],
        "Fig_8": [],
        "Fig_9": [],
        "Fig_10": [],
    }

# Font dict suptitle
font_dict_suptitle = {
    'family': 'Helvetica',
    'size': 20,
    'color': "black"
}

# Font dict title
font_dict_title = {
    'family': 'Helvetica',
    'size': 20,
    'color': "black"
}

# Font dict xlabel
font_dict_xlabel = {
    'family': 'Helvetica',
    'size': 20,
    'color': "black"
}
# Font dict ylabel
font_dict_ylabel = {
    'family': 'Helvetica',
    'size': 20,
    'color': "black"
}
# Font dict xtick
font_dict_xtick = {
    'family': 'Helvetica',
    'size': 20,
    'color': "black"
}  # Font ytick
font_dict_ytick = {
    'family': 'Helvetica',
    'size': 20,
    'color': "black"
}
# Font dict legend
font_dict_legend = {
    'family': 'Helvetica',
    'size': 20,
    'color': "black"
}

# Font dict default
font_dict_legend = {
    'family': 'Helvetica',
    'size': 10,
    'color': "black"
}


# Ploting....
def plot(y, x=None, title=None, subtitle=None, xlabel=None, ylabel=None, legends=None, xlim=None, ylim=None, leg_loc= "upper left", ls=None, lw=None, c=None, marker=None, mec=None, mfc=None, ms=None):
    # Note:   the 'DejaVu Sans' is the default font family, defalt font size for python is 10
    font_family = [None, "Helvetica", "Times New Roman", "Comic Sans MS", "Arial", "Calibri", "DejaVu Sans"]

    if x is None:
        plt.plot(y, label=legends, ls=ls, lw=lw, c=c, marker=marker, mec=mec, mfc=mfc, ms=ms)
    else:
        plt.plot(x, y, label=legends, ls=ls, lw=lw, c=c, marker=marker, mec=mec, mfc=mfc, ms=ms)
    plt.suptitle(subtitle, ha='center', fontsize=12, weight='extra bold', family=font_family[-1])
    plt.title(title, ha='center', fontsize=12, weight='normal', family=font_family[-1])
    plt.xlabel(xlabel, family=font_family[-1], fontsize=10, weight='normal')
    plt.ylabel(ylabel, family=font_family[-1], fontsize=10, weight='normal')
    plt.legend(loc=leg_loc, framealpha= 1, facecolor="White", edgecolor="black", fancybox=True, shadow=False, prop={'family':font_family[-1], 'stretch': 'normal', "weight":"normal", "size": 10})
    plt.grid(axis="both")

