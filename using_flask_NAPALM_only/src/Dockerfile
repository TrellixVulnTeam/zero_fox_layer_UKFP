FROM ubuntu:latest

# USER root



RUN mkdir zero_fox_layer

WORKDIR /zero_fox_layer

COPY . .
COPY ./libs .

RUN apt update && apt upgrade -y && \
    apt install python3-pip -y && \
    pip install -r requirements.txt

# RUN apt upgrade -y

# RUN apt install python3 -y

# RUN apt install pip3

# RUN pip install -r requirements.txt

# RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python3" ]    

CMD [ "zero_fox_layer.py" ] 


