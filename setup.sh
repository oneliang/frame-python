#!/bin/bash
python3.7 setup.py sdist
echo "-----setup to dist finished-----"

pip3.7 install dist/frame-python-1.0.tar.gz
echo "-----install frame-python finished-----"
