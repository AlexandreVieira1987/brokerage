FROM python:3.8
RUN apt-get update
RUN apt-get install tesseract-ocr
RUN apt-get install tesseract-ocr-ben
RUN apt-get install poppler-utils
RUN pip3 install pdf2image
RUN pip3 install pytesseract


#ADD . /tesseract-python
#WORKDIR /tesseract-python
#RUN pip install -r requirements.txt

