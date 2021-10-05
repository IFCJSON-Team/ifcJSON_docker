FROM python:3.8

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

WORKDIR /app

ADD https://s3.amazonaws.com/ifcopenshell-builds/ifcopenshell-python-38-v0.6.0-721fe47-linux64.zip /tmp/ifcopenshell.zip
RUN unzip /tmp/ifcopenshell.zip -d .

# file converters
COPY lib/ifcJSON/file_converters/ifcjson ./ifcjson

# ifcJSON Schema
COPY lib/ifcJSON/Schema/IFC4.json ./

COPY app ./

EXPOSE 3200

ENTRYPOINT ["python","/app/app.py"]