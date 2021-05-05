import os

from cds_downloader import Downloader
from ado_downscaler import Downscaler

def main():
    input_path = "/input"
    output_path = "/output"

    downloader = Downloader.from_json("ado_era5.json")
    lst_files = downloader.get_latest_daily_data("/tmp/era5", date_latency="5D")

    filter_variable = downloader.cds_filter.get("variable")

    if not isinstance(filter_variable,list):
        filter_variable = filter_variable.split()

    for var_name in filter_variable:
        downscaler = Downscaler.from_filepaths(
            os.path.join(input_path, "UERRA", var_name),
            os.path.join(input_path, "ERA5", var_name)
        )
        # ado_ds = Downscaler.from_filepaths("/mnt/ADO/ZAMG/QM/era5_uerra/daily/2m_dewpoint_temperature/uerra/*","/mnt/ADO/ZAMG/QM/era5_uerra/daily/2m_dewpoint_temperature/era5/*")
        # ado_ds.downscale_era5("/mnt/ADO/ZAMG/ERA5/daily/2m_dewpoint_temperature_2021_4_22_reanalysis-era5-single-levels.grib","./")


if __name__ == "__main__":
    main()
