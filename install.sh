#!/bin/bash
python3 -m venv .venv

if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    source .venv/Scripts/activate
else
    source .venv/bin/activate
fi

pip install --upgrade pip
pip install -r utils/requirements.txt
