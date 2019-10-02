FROM python:3-stretch

WORKDIR /usr/src/app

COPY dict.tar.gz .
RUN mkdir -p /root/.jamdict/data/
RUN tar -C /root/.jamdict/data/ -zxvf dict.tar.gz --strip 1
RUN rm dict.tar.gz

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

# $ docker build . -t jp:latest
# $ docker run --rm -i -t -v $(pwd):/usr/src/app/ jp:latest /bin/bash
# $ python app.py