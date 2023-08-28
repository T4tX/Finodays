FROM python:3.8
ADD db.py /database/
ADD requirements.txt /database/
WORKDIR /database/
RUN pip3 install -r requirements.txt
CMD [ "python3", "db.py" ]