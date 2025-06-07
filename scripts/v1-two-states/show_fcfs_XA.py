import matplotlib.pyplot as plt
from matplotlib.axes import Axes


fcfs_nu33_b2_Mulliken_65_cm = [
    abs(float(fcf)) for fcf in 
   """9.9984e-01   3.2167e-16  -1.7926e-02  -9.9892e-18   3.9363e-04
   2.8318e-19  -9.1111e-06  -7.7554e-21   2.1610e-07   2.0857e-22  -5.1981e-09
   -5.5465e-24   1.2619e-10   1.4638e-25  -3.0832e-12  -3.8417e-27   7.5693e-14
   1.0041e-28  -1.8652e-15  -2.6156e-30   4.6095e-17   6.7958e-32  -1.1419e-18
   -1.7618e-33   2.8343e-20   4.5594e-35  -7.0471e-22  -1.1781e-36   1.7546e-23
   3.0399e-38  -4.3742e-25  -7.8353e-40   1.0916e-26   2.0175e-41  -2.7269e-28
   -5.1901e-43   6.8174e-30   1.3341e-44  -1.7057e-31  -3.4270e-46   4.2704e-33
   8.7972e-48  -1.0698e-34  -2.2570e-49   2.6816e-36   5.7874e-51  -6.7250e-38
   -1.4833e-52   1.6873e-39   3.7999e-54  -4.2352e-41  -9.7307e-56   1.0635e-42
   2.4909e-57  -2.6715e-44  -6.3740e-59   6.7128e-46   1.6305e-60  -1.6873e-47
   -4.1697e-62   4.2425e-49""".split()
]


fcfs_nu32_a1_Mulliken_449_cm = [
    abs(float(fcf)) for fcf in 
   """1.0000e+00  -4.5994e-16  -6.7669e-04   5.3907e-19   5.6082e-07
   -5.7677e-22  -4.8993e-10   5.9618e-25   4.3857e-13  -6.0515e-28  -3.9817e-16
   6.0738e-31   3.6482e-19  -6.0498e-34  -3.3642e-22   5.9928e-37   3.1173e-25
   -5.9115e-40  -2.8991e-28   5.8122e-43   2.7041e-31  -5.6995e-46  -2.5283e-34
   5.5769e-49   2.3686e-37  -5.4470e-52  -2.2227e-40   5.3120e-55   2.0887e-43
   -5.1735e-58  -1.9653e-46   5.0327e-61   1.8511e-49  -4.8909e-64  -1.7452e-52
   4.7488e-67   1.6468e-55  -4.6072e-70  -1.5551e-58   4.4667e-73   1.4695e-61
   -4.3276e-76  -1.3894e-64   4.1904e-79   1.3144e-67  -4.0555e-82  -1.2441e-70
   3.9230e-85   1.1782e-73  -3.7931e-88  -1.1161e-76   3.6661e-91   1.0578e-79
   -3.5419e-94  -1.0029e-82   3.4208e-97   9.5113e-86 -3.3027e-100  -9.0233e-89
   3.1878e-103   8.5629e-92""".split()
]


def show_fcfs(ax: Axes, fcfs: list[float], label: str) -> None:
    xs = range(len(fcfs))
    ax.semilogy(xs, fcfs, label=label)


def main():
    ratio=16/9
    width=3
    fig = plt.figure(
        layout='constrained',
        figsize=(ratio*width,width),
    )
    ax = fig.subplots()
    show_fcfs(
        ax=ax,
        fcfs=fcfs_nu33_b2_Mulliken_65_cm,
        label=r"$\nu _{33}$($a_1$), $\tilde{\nu} = 65$cm$^{-1}$, $\Delta Q=0.0$"
    )
    show_fcfs(
        ax=ax,
        fcfs=fcfs_nu32_a1_Mulliken_449_cm,
        label=r"$\nu _{32}$($a_1$), $\tilde{\nu} = 449$cm$^{-1}$, $\Delta Q=0.0$"
    )
    ax.set_ylabel(r'$|\langle 0_{A}| n_{X} \rangle |$')
    ax.set_xlabel(r'$n_X$')
    ax.set_title("SrOPh X-A")
    ax.set_ylim(top=1, bottom=1e-100)
    ax.legend()
    ax.grid()
    fig.savefig(fname='fcfs_xa.svg')

if __name__ == "__main__":
    main()
