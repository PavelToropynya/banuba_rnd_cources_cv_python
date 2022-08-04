import os
import platform

platform = platform.system()

# TODO add all platforms support
# for macOS
if platform == "Darwin":
    os.system('python3 -m venv ../')
    os.system('virtualenv bnbenv')
    os.system('python -m venv bnbenv')
    os.system('source bnbenv/bin/activate')
