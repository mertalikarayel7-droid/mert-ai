name: Build Android APK

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install System Dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev libssl-dev openssl libgdbm-dev libgdbm-compat-dev liblldb-dev liblzma-dev libreadline-dev libffi-dev uuid-dev git python3-dev zip unzip

    - name: Install Buildozer & Cython
      run: |
        pip install --upgrade pip
        pip install "cython<0.30.0" buildozer

    - name: Build APK with Buildozer
      run: |
        yes | buildozer -v android debug

    - name: Upload APK Artifact
      uses: actions/upload-artifact@v4
      with:
        name: mert-ai-apk
        path: bin/*.apk
