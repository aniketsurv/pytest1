### name: Build Docker Image
  run: |
    docker build -t my-python-app .

### name: Run Tests in Docker
  run: |
    docker run --rm my-python-app
