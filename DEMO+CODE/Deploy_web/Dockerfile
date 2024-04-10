FROM python:3.12-slim
COPY . /main
WORKDIR /main
RUN pip install -r requirements.txt
EXPOSE 80
RUN mkdir ~/.streamlit
RUN cp config.toml ~/.streamlit/config.toml
WORKDIR /main
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"] 