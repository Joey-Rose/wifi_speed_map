FROM amazon/aws-lambda-python:3.8

# Install system dependencies
RUN yum install -y make sqlite-devel zlib-devel bash git gcc-c++ unzip

# install aws cli
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install

RUN cp /usr/local/bin/aws /opt/aws

# Copy function code to container
COPY lambda.py ./

# copy requirements.txt to container
COPY requirements.txt ./

# installing dependencies
RUN pip3 install -r requirements.txt

# Create a build directory; clone tippecanoe; and copy in all files
RUN mkdir -p /build
RUN git clone https://github.com/mapbox/tippecanoe.git /build/tippecanoe --depth 1
WORKDIR /build/tippecanoe

# Build tippecanoe
RUN make \
  && make install

# Copy binaries to `/opt`
RUN cp ./tippecanoe /opt/tippecanoe
RUN cp ./tile-join /opt/tile-join

# reset workdir
WORKDIR /opt

# setting the CMD to your handler file_name.function_name
CMD [ "lambda.handler" ]