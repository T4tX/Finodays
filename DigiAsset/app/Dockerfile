FROM python:3.8
ADD main.py /app/ 
ADD requirements.txt /app/ 
WORKDIR /app/
RUN pip3 install -r requirements.txt
CMD [ "python3", "uvicorn" , "main:app", "--reload"]