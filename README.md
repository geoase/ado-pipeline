# ado-pipeline

Build image with tag:

```
docker build -t ado_qm_pet .
```

Run container with bind mounts and .env file (`-it` may be omitted):

```
docker run -v /mnt/ADO/ZAMG/UERRA/derived/daily:/data/input/uerra -v /mnt/ADO/ZAMG/ERA5/archive/derived:/data/input/era5 --env-file .env -it ado_pet bash
docker run -d \
  -it \
  --name ado_qm_pet_test \
  --mount type=bind,source=<INPUT DIRECTORY>,target=/home/appuser/data/input,readonly \
  --mount type=bind,source=<OUTPUT DIRECTORY>,target=/home/appuser/data/output \
  --env-file .env\
  ado_qm_pet:latest
```

Copy the .env.sample file to .env and adapt the CDS API information following the 
instructions in the [api-how-to](https://cds.climate.copernicus.eu/api-how-to).

The daily archive data of "era5" and "uerra" must already be present in subdirectories within
`<INPUT DIRECTORY>`. Be sure that the permissions are set accordingly, so that the data can be written 
from the container.
