from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from Figure_details1 import plot, FigDetails as fdc

# objects
titles, subtitles, xlabels, ylabels, xlims, ylims, legends = [fdc.titles, fdc.subtitles, fdc.xlabels, fdc.ylabels,
                                                              fdc.xlims, fdc.ylims, fdc.legends_dict]


def main():
    err_data_roll = [i for i in range(1, 201, 1)]
    err_data_pitch = [i for i in range(1, 601, 3)]
    err_data_yaw = [i for i in range(1, 401, 2)]
    plot(err_data_pitch, subtitle=subtitles[-1], title=titles["Fig_1"][-1], xlabel=xlabels[0], ylabel=ylabels[0], legends=legends["Fig_1"][0],
         xlim=None, ylim=None, leg_loc="upper left", ls=None, lw=None, c=None, marker=".")
    plot(err_data_yaw, subtitle=subtitles[-1], title=titles["Fig_1"][-1], xlabel=xlabels[0], ylabel=ylabels[0], legends=legends["Fig_1"][1],
         xlim=None, ylim=None, leg_loc="upper left", ls=None, lw=2, c=None)
    # plt.legend(labels=legends["Fig_1"])
    plt.grid(axis="both", linewidth=1, linestyle="dashed")
    plt.show()

# SUBPLOTS
    # Subplot_1...........
    plt.subplot(2,2,1)
    plot(err_data_pitch, subtitle=subtitles[1], title=titles["Fig_2"][0], xlabel=xlabels[0], ylabel=ylabels[0], legends=legends["Fig_1"][0],
         xlim=None, ylim=None, leg_loc="upper left", ls=None, lw=3, c=None)
    plot(err_data_yaw, subtitle=subtitles[1], title=titles["Fig_2"][0], xlabel=xlabels[0], ylabel=ylabels[0], legends=legends["Fig_1"][1],
         xlim=None, ylim=None, leg_loc="upper left", ls=None, lw=4, c=None)
    plt.grid(axis="both", linewidth=1, linestyle="dashed")
    # Subplot_2...........
    plt.subplot(2,2,2)
    plot(err_data_pitch, subtitle=subtitles[1], title=titles["Fig_2"][1], xlabel=xlabels[0], ylabel=ylabels[0], legends=legends["Fig_1"][0],
         xlim=None, ylim=None, leg_loc="upper left", ls=None, lw=5, c=None)
    plot(err_data_yaw, subtitle=subtitles[1], title=titles["Fig_2"][1], xlabel=xlabels[0], ylabel=ylabels[0], legends=legends["Fig_1"][1],
         xlim=None, ylim=None, leg_loc="upper left", ls=None, lw=10, c=None)
    plt.grid(axis="both", linewidth=1, linestyle="dashed")
    # Subplot_3...........
    plt.subplot(2,2,3)
    plot(err_data_pitch, subtitle=subtitles[1], title=titles["Fig_2"][2], xlabel=xlabels[0], ylabel=ylabels[0], legends=legends["Fig_1"][0],
         xlim=None, ylim=None, leg_loc="upper left", ls="dashed", lw=15, c=None)
    plot(err_data_yaw, subtitle=subtitles[1], title=titles["Fig_2"][2], xlabel=xlabels[0], ylabel=ylabels[0], legends=legends["Fig_1"][1],
         xlim=None, ylim=None, leg_loc="upper left", ls="solid", lw=20, c="green")
    plt.grid(axis="both", linewidth=1, linestyle="dashed")
    # Subplot_4...........
    plt.subplot(2,2,4)
    plot(err_data_pitch, subtitle=subtitles[1], title=titles["Fig_2"][3], xlabel=xlabels[0], ylabel=ylabels[0], legends=legends["Fig_1"][0],
         xlim=None, ylim=None, leg_loc="upper left", ls="dashdot", lw=25, c="blue")
    plot(err_data_yaw, subtitle=subtitles[1], title=titles["Fig_2"][3], xlabel=xlabels[0], ylabel=ylabels[0], legends=legends["Fig_1"][1],
         xlim=None, ylim=None, leg_loc="upper left", ls="dashed", lw=30, c="black")
    plt.grid(axis="both", linewidth=1, linestyle="dashed")
    plt.show()


if __name__ == "__main__":
    main()
