FROM continuumio/miniconda:latest

WORKDIR /home/docker_conda_ifcproj

COPY environment.yml ./
COPY server.py ./
COPY process_ifc.py ./
COPY crud.py ./
COPY jan_func.py ./
COPY tmpIfcFile.ifc ./
COPY janIfcFile.ifc ./
COPY janJsonFile.json ./
COPY ifcjson ifcjson/
COPY templates templates/
COPY static static/

COPY boot.sh ./

RUN chmod +x boot.sh

RUN conda env create -f environment.yml

# RUN echo "source activate testenv" < ~/.bashrc
ENV PATH /opt/conda/envs/testenv2/bin:$PATH

EXPOSE 3200

ENTRYPOINT ["./boot.sh"]
