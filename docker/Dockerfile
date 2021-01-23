FROM continuumio/miniconda:latest

COPY docker/environment.yml .

RUN conda env create -f environment.yml

RUN echo "source activate env" > ~/.bashrc

ENV PATH /opt/conda/envs/env/bin:$PATH

WORKDIR /app

COPY lib/ifcJSON/file_converters/ifcjson ./ifcjson
COPY app ./

EXPOSE 3200

ENTRYPOINT ["python","/app/app.py"]

# CMD ["flask", "run", "-h", "0.0.0.0", "-p", "3200"]