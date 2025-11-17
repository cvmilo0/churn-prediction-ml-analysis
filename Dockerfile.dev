FROM python:3.11-slim

RUN apt-get update && apt-get install --no-install-recommends -y \
        curl \ 
        build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

#Install uv for package management
ADD https://astral.sh/uv/install.sh /install.sh
RUN chmod -R 755 /install.sh && /install.sh && rm /install.sh
# Set up the UV environment path correctly
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app

COPY . .

RUN uv sync

ENV PATH="/app/.venv/bin:{$PATH}"

# Expose the specified port for FastAPI
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]