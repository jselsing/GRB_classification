import pandas as pd
from astropy.utils.data import download_file
import shutil

def main():

    # Open BAT catalog
    batcat = pd.read_csv("../data/batcat.csv")

    # Loop through enties to get lc
    for index, row in batcat.iterrows():

        # Skip rows with the trigger ID
        try:
            # Construct URL
            grbname = row["GRBname"]
            trigger = int(row["Trig_ID"])
            lc_url = "https://swift.gsfc.nasa.gov/results/batgrbcat/%s/data_product/00%s000-results/lc/64ms_lc_ascii.dat"%(grbname, trigger)

            # Download lc and move to data dir
            tmp_path = download_file(lc_url)
            batlc_path = "../data/BAT_lightcurves/%s_lc.dat"%(grbname)
            shutil.move(tmp_path, batlc_path)
        except:
            pass



if __name__ == '__main__':
    main()







