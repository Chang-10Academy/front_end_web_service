FROM python:3.8
ADD . /front_end_web_service
WORKDIR /front_end_web_service
RUN pip install -r requirements.txt
CMD python app.py