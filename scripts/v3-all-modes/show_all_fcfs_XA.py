import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from database_XA import all_modes_fcfs, FCFs


def show_fcfs(ax: Axes, mode: FCFs) -> None:
    fcfs = mode.fcfs
    fcfs = [abs(fcf) if abs(fcf) > 1e-75 else np.nan for fcf in fcfs]
    xs = range(len(fcfs))
    label = (
        r"$\tilde{\nu}"
        r"=" 
        fr"{mode.nu_cm:.0f}$"
        r"cm$^{-1}$" 
        r", $\Delta Q=" 
        fr"{mode.dQ:+.3f}$"
    )
    ax.plot(xs, fcfs, label=label, marker='.')


def save_batch(batch: int):
    ratio=16/9
    width=4.5
    fig = plt.figure(
        layout='constrained',
        figsize=(ratio*width,width),
    )
    ax = fig.subplots()
    ax.set_ylabel(r'$|\langle 0_{A}| n_{X} \rangle |$')
    ax.set_xlabel(r'$n_X$')
    for mode in all_modes_fcfs[10*batch:min(10*(batch+1), len(all_modes_fcfs))]:
        show_fcfs(ax, mode)
    ax.set_yscale('log')
    ax.set_title("SrOPh X-A")
    ax.set_yticks(ticks=[1, 1e-15, 1e-30, 1e-45, 1e-60, 1e-75])
    ax.set_xticks(ticks=[10 * i for i in range(7)])
    ax.set_xlim(left=-3, right=63)
    ax.set_ylim(top=1, bottom=1e-75)
    ax.legend(
        bbox_to_anchor=(1.05, 1),
        loc='upper left',
        handletextpad=0.15,     # Space between legend marker and text
        columnspacing=0.8,     # Space between columns (if ncol > 1)
        handlelength=1.5,      # Length of legend markers
    )
    ax.grid()
    fig.savefig(fname=f'fcfs_all_XA_{batch}.svg')


def main():
    for batch in range(4):
        save_batch(batch)


if __name__ == "__main__":
    main()
