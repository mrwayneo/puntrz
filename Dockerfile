FROM python:3.8-slim
RUN useradd --create-home --shell /bin/bash wayneo
WORKDIR /home/wayneo
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
USER wayneo
CMD ["bash"]