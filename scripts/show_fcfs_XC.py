import matplotlib.pyplot as plt
from matplotlib.axes import Axes


fcfs_nu12_a1_Mulliken_239_cm = [
    abs(float(fcf)) for fcf in 
   """9.7499e-01   2.2045e-01   2.7970e-02   1.7515e-03  -5.7635e-05
   -2.2362e-05  -1.5089e-06   8.9556e-08   2.2056e-08   7.7121e-10  -1.6570e-10
   -1.9057e-11   4.3047e-13   2.2023e-13   8.9306e-15  -1.7242e-15  -1.8873e-16
   7.3048e-18   2.3250e-18   4.5565e-20  -2.1614e-20  -1.5358e-21   1.4884e-22
   2.2870e-23  -4.8228e-25  -2.5830e-25  -6.4627e-27   2.3940e-27   1.6928e-28
   -1.7720e-29  -2.4880e-30   8.2939e-32   2.9161e-32   2.8578e-34  -2.9213e-34
   -1.4138e-35   2.5073e-36   2.4038e-37  -1.7295e-38  -3.1305e-39   6.8321e-41
   3.5047e-41   5.1031e-43  -3.4797e-43  -1.7185e-44   3.0522e-45   2.8115e-46
   -2.2597e-47  -3.6737e-48   1.1738e-49   4.2137e-50   1.0746e-52  -4.3705e-52
   -1.4697e-53   4.1176e-54   2.7924e-55  -3.4631e-56  -3.9583e-57   2.4482e-58
   4.8628e-59  -1.1428e-60""".split()
]


fcfs_nu6_a1_Mulliken_1349_cm = [
    abs(float(fcf)) for fcf in 
   """9.9933e-01  -3.6377e-02   3.2323e-03  -1.6443e-04   1.2088e-05
   -6.7465e-07   4.5879e-08  -2.6607e-09   1.7368e-10  -1.0258e-11   6.5345e-13
   -3.8950e-14   2.4421e-15  -1.4625e-16   9.0688e-18  -5.4430e-19   3.3484e-20
   -2.0113e-21   1.2299e-22  -7.3879e-24   4.4961e-25  -2.6997e-26   1.6368e-27
   -9.8214e-29   5.9360e-30  -3.5588e-31   2.1453e-32  -1.2850e-33   7.7289e-35
   -4.6250e-36   2.7764e-37  -1.6598e-38   9.9469e-40  -5.9409e-41   3.5549e-42
   -2.1213e-43   1.2676e-44  -7.5571e-46   4.5103e-47  -2.6867e-48   1.6017e-49
   -9.5328e-51   5.6772e-52  -3.3763e-53   2.0088e-54  -1.1938e-55   7.0963e-57
   -4.2140e-58   2.5030e-59  -1.4853e-60   8.8155e-62  -5.2278e-63   3.1005e-64
   -1.8375e-65   1.0891e-66  -6.4505e-68   3.8206e-69  -2.2616e-70   1.3387e-71
   -7.9202e-73   4.6855e-74""".split()
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
        fcfs=fcfs_nu12_a1_Mulliken_239_cm,
        label=r"$\nu _{12}$($a_1$), $\tilde{\nu} = 239$cm$^{-1}$, $\Delta Q=0.119$"
    )
    show_fcfs(
        ax=ax,
        fcfs=fcfs_nu6_a1_Mulliken_1349_cm,
        label=r"$\nu _{6}$($a_1$), $\tilde{\nu} = 1349$cm$^{-1}$, $\Delta Q=0.008$"
    )
    ax.set_ylabel(r'$|\langle 0_{C}| n_{X} \rangle |$')
    ax.set_xlabel(r'$n_X$')
    ax.set_title("SrOPh X-C")
    ax.legend()
    ax.grid()
    fig.savefig(fname='fcfs_xc.svg')

if __name__ == "__main__":
    main()
