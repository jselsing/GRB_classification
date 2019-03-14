import matplotlib; matplotlib.use('TkAgg')
import matplotlib.pyplot as pl
import seaborn as sns; sns.set_style('ticks')

import pandas as pd
import numpy as np

def main():

    # Open BAT catalog
    batcat = pd.read_csv("../data/batcat.csv")

    # Loop through enties to get lc
    for index, row in batcat.iterrows():



        # Skip rows without the trigger ID
        try:
            # Read in lc to dataframe
            grbname = row["GRBname"]
            batlc_path = "../data/BAT_lightcurves/%s_lc.dat"%(grbname)
            lc_frame = pd.read_table(batlc_path, names=["t", "15-25 keV", "2", "25-50 keV", "4", "50-100 keV", "6", "100-350 keV", "8", "15-350 keV", "10"], sep=" ")

            lc = lc_frame[["t", "15-25 keV", "25-50 keV", "50-100 keV", "100-350 keV", "15-350 keV"]]
            lc = lc[(lc.t > -10) & (lc.t < 50)]
            lc.to_hdf("../data/bat_lc.h5", key=grbname)

        except:
            pass



if __name__ == '__main__':
    main()

