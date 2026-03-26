FROM astral/uv:python3.13-trixie

WORKDIR /app
RUN apt-get update \
    && apt-get install -y \
        curl \
    && apt-get clean
COPY . .
RUN uv sync

EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT [ "uv", "run", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0" ]
