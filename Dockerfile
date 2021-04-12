FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y vim

RUN apt-get install -y python3.8 python3-pip python3.8-dev 
RUN apt-get install -y git
RUN python3.8 -m pip install flask
WORKDIR /home
RUN mkdir output
RUN git clone https://github.com/eduard-cojocea/Laborator_MDS.git

CMD python3.8 /home/Laborator_MDS/example_flask_2.py