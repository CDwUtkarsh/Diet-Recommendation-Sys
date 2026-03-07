FROM python:3.10

WORKDIR /app

COPY Streamlit_Frontend /app

RUN pip install --upgrade pip
RUN pip install -r pages/requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "Hello.py"]