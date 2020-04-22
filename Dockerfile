FROM python:3

WORKDIR /opt/bot

COPY . .

# install all dependancies
RUN pip install -r requirements.txt

CMD ["python", "main.py"]