FROM python:3
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python3","anapi.py"]
