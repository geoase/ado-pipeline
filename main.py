import os
import glob

from cds_downloader import Downloader
from ado_downscaler import Downscaler
from ado_downscaler import calculate_pet

def main():
    input_path = "~/data/input"
    output_path = "~/data/output"

    downloader = Downloader.from_json("ado_era5.json")
    lst_processes = downloader.get_latest_daily_data(f"{output_path}/era5", date_latency="5D")

    filter_variable = downloader.cds_filter.get("variable")

    if not isinstance(filter_variable,list):
        filter_variable = filter_variable.split()

    dct_paths = {}
    for var_name in filter_variable:
        file_name = glob.glob(f"{output_path}/era5/{var_name}*")[0]
        dct_paths[var_name] = file_name
        downscaler = Downscaler.from_filepaths(
            os.path.join(input_path, "uerra", var_name + "*"),
            os.path.join(input_path, "era5", var_name + "*")
        )
        downscaler.downscale_era5(
            os.path.join(f"{output_path}/era5", file_name),
            os.path.join(f"{output_path}/qm")
        )

    dct_paths["orography_reanalysis"] = f"{input_path}/uerra/orography_reanalysis-uerra-europe-single-levels.nc"}
    calculate_pet(dct_paths)

if __name__ == "__main__":
    main()
