
- name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install "cython<0.30.0" buildozer

      - name: Build with Buildozer
        run: |
          yes | buildozer -v android debug
