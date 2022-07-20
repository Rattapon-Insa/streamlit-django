FROM python:3.9

WORKDIR /streamlit_app

COPY requirements.txt /streamlit_app/requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install streamlit

EXPOSE 8000

COPY . .

CMD ["python", "manage.py", "runserver"]



