FROM python:3.8
ADD db.py /app/ 
ADD main.py /app/ 
ADD requirements.txt /app/ 
WORKDIR /app/ 
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD [ "python3", "db.py" ]




