import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from database_XA import FCFs, mulliken_ids
from database_XC import all_modes_fcfs


def show_fcfs(ax: Axes, mode: FCFs) -> None:
    fcfs = mode.fcfs
    fcfs = [abs(fcf) if abs(fcf) > 1e-105 else np.nan for fcf in fcfs]
    xs = range(len(fcfs))
    label = (
        r"$\tilde{\nu}_{" # }
        f'{mode.mulliken_idx}'
        r"}=$" 
        fr"{mode.nu_cm:4.0f}"
        r"cm$^{-1}$" 
        r", $\Delta Q=$" 
        f"{mode.dQ*1e3:>+4.0f}"
    )
    ax.plot(xs, fcfs, label=label, marker='.')


def save_batch(batch: list[FCFs], symmetry: str) -> None:
    ratio=16/9
    width=4.5
    fig = plt.figure(
        layout='constrained',
        figsize=(ratio*width,width),
    )
    ax = fig.subplots()
    ax.set_ylabel(r'$|\langle 0_{C}| n_{X} \rangle |$')
    ax.set_xlabel(r'$n_X$')
    for mode in batch:
        show_fcfs(ax, mode)
    ax.set_yscale('log')
    ax.set_title(f"SrOPh X-C {symmetry[0]}$_{{{symmetry[1]}}}$")
    ax.set_yticks(ticks=[1, 1e-15, 1e-30, 1e-45, 1e-60, 1e-75])
    ax.set_xticks(ticks=[10 * i for i in range(7)])
    ax.set_xlim(left=-3, right=63)
    ax.set_ylim(top=1, bottom=1e-75)
    ax.legend(
        bbox_to_anchor=(1.05, 1),
        prop={'family': 'monospace'},
        loc='upper left',
        handletextpad=0.15,     # Space between legend marker and text
        columnspacing=0.8,     # Space between columns (if ncol > 1)
        handlelength=1.5,      # Length of legend markers
    )
    ax.grid()
    fig.savefig(fname=f'fcfs_all_XC_{symmetry}.svg')


def add_mulliken(mode: FCFs) -> FCFs:
    if mode.mulliken_idx != -1:
        raise RuntimeError("Fixing mulliken_idx when it's already set")

    current_freq = mode.nu_cm
    for mulliken_id in mulliken_ids:
        if abs(round(current_freq) - mulliken_id['freq']) < 0.49:
            mode.mulliken_idx = mulliken_id['idx']
            return mode
    else:
        raise RuntimeError(
            f"Didn't find the mulliken idx for mode of {mode.nu_cm=}"
        )


def main():
    fcfs_with_mulliken = [
        add_mulliken(mode) for mode in all_modes_fcfs
    ]
    fcfs_with_mulliken.sort(key=lambda f: f.mulliken_idx)

    # for fcfs in fcfs_with_mulliken:
    #     print(f'{fcfs.nu_cm=:5.0f} {fcfs.mulliken_idx=}')

    save_batch(fcfs_with_mulliken[:12], 'a1')
    save_batch(fcfs_with_mulliken[12:15], 'a2')
    save_batch(fcfs_with_mulliken[15:22], 'b1')
    save_batch(fcfs_with_mulliken[22:], 'b2')


if __name__ == "__main__":
    main()
