#!/bin/bash
python3 --version
pip install -r requirements.txt
nucliadb --blob blob --main main --node node --log INFO