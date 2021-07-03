#!/bin/sh
pip3 freeze > requirements.txt
sed -i '/pkg-resources/d' requirements.txt