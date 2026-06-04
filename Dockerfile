FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN useradd -m appuser

USER appuser

EXPOSE 8501

CMD ["streamlit","run","app.py","--server.address=0.0.0.0"]