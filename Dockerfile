FROM python:3.12-slim-bullseye

# Add user docker to the container
RUN useradd -ms /bin/bash docker

# Install dependencies for a python app using requirements.txt
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    curl \
    build-essential

# Create the /app directory in /home/docker with owner docker \
RUN mkdir -p /home/docker/app && chown -R docker:docker /home/docker/app

# Set the working directory to the created app directory
WORKDIR /home/docker/app

# Copy requirements.txt to the container
COPY --chown=docker:docker ./requirements.txt /home/docker/app/requirements.txt

# Install dependencies using existing requirements.txt in /home/docker/app/requirements.txt
RUN pip3 install --no-cache-dir -r /home/docker/app/requirements.txt

# Copy the rest of the src files with docker user as owner
COPY --chown=docker:docker src/ /home/docker/app/src/
COPY --chown=docker:docker .env /home/docker/app/.env

# Switch to docker user
USER docker

# Create a healthcheck for the container
HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f http://localhost:80/health || exit 1

# Expose port 80
EXPOSE 80

# Create entrypoint for src/main.py via python
ENTRYPOINT ["python3", "src/main.py"]

