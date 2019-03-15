import matplotlib; matplotlib.use('TkAgg')
import matplotlib.pyplot as pl
import seaborn as sns; sns.set_style('ticks')

import pandas as pd
from scipy.signal import medfilt


def main():

    bands = ["15-25 keV", "25-50 keV", "50-100 keV", "100-350 keV", "15-350 keV"]



    # Open BAT catalog
    batcat = pd.read_csv("../data/batcat.csv")

    # Loop through enties to get lc
    # melt
    for index, row in batcat.iterrows():
        try:
            grbname = row["GRBname"]
            t90 = row["T90"]
            if t90 < 2:
                lc = pd.read_hdf("../data/bat_lc.h5", key=grbname)
                flux = medfilt(lc[bands[0]], 1)
                pl.plot(lc.t, flux, linestyle="steps-mid")

        except:
            pass

    kn_cand = ["GRB051221A", "GRB101219A", "GRB100625A", "GRB120804A", "GRB130603B"]
    # bands = ["15-25 keV", "25-50 keV", "50-100 keV", "100-350 keV", "15-350 keV"]

    for ii, kk in enumerate(kn_cand):

        lc = pd.read_hdf("../data/bat_lc.h5", key=kk)
        pl.plot(lc.t, 1+medfilt(lc[bands[0]], 1), linestyle="steps-mid", label=kk)



    pl.xlim(-3, 5)
    pl.legend()
    pl.tight_layout()
    pl.savefig("../figures/BAT_lc.pdf")
    # pl.show()


if __name__ == '__main__':
    main()







