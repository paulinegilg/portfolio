#!/bin/sh

echo "Beep-beep... Starting build... 🤖"

if [ -d "./build" ]; then
  rm -r ./build
fi

mkdir ./build

cp -r ./assets ./build

python3 main.py "$1"

echo "Build is complete! 🎉"
