#!/usr/bin/python

import os
import shutil
import glob

TMP = ['./app/**/__pycache__', './app/**/migrations', './app/innerDB', './mysql/database']

def clean():
  for path in TMP:
    for _ in glob.glob(path, recursive=True):
      os.remove(_) if os.path.isfile(_) else shutil.rmtree(_)

def run():
  # Clean docker data - dont uncomment this line if u dont know what it for
  os.system("docker system prune -f")
  os.system("docker-compose up --build")

if __name__ == "__main__":
  clean()
  run()