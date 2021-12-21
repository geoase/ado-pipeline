import os
import glob

from cds_downloader import Downloader
from ado_downscaler import Downscaler

def main():
    input_path = "/data/input"
    output_path = "/data/output"

    downloader = Downloader.from_json("ado_era5.json")
    lst_processes = downloader.get_latest_daily_data("/tmp/era5", date_latency="5D")

    filter_variable = downloader.cds_filter.get("variable")

    if not isinstance(filter_variable,list):
        filter_variable = filter_variable.split()

    for var_name in filter_variable:
        file_name = glob.glob(f"/tmp/era5/{var_name}*")[0]
        print(file_name)
        print(var_name)
        downscaler = Downscaler.from_filepaths(
            os.path.join(input_path, "uerra", var_name + "*"),
            os.path.join(input_path, "era5", var_name + "*")
        )
        downscaler.downscale_era5(
            os.path.join("/tmp/era5", file_name),
            os.path.join("./")
        )


if __name__ == "__main__":
    main()
