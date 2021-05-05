FROM continuumio/miniconda3

COPY ["environment.yml", "/tmp/"]
RUN conda env create -f /tmp/environment.yml

# Create a user to run our app
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

COPY ["ado_era5.json","main.py", "./"]

# Pull the environment name out of the environment.yml
RUN echo "source activate $(head -1 /tmp/environment.yml | cut -d' ' -f2)" > ~/.bashrc
ENV PATH /opt/conda/envs/$(head -1 /tmp/environment.yml | cut -d' ' -f2)/bin:$PATH

#ENTRYPOINT ["python","main.py"]
