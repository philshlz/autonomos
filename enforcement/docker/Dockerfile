# minimal agent container. the adapter (claude-code / openrouter / ollama)
# is layered in at build via ADAPTER build-arg. the handbook and ledger
# are identical regardless of which adapter wins.
FROM python:3.12-slim

ARG ADAPTER=openrouter
WORKDIR /agent

COPY . /agent
RUN pip install --no-cache-dir -r requirements.txt 2>/dev/null || true

# the agent boots from the handbook, writes to the mounted ledger,
# and reaches the network only through the proxy
ENTRYPOINT ["python", "boot.py"]
