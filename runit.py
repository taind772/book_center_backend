#!/usr/bin/python

import os
import shutil
import glob

TMP = ['./app/**/__pycache__/*', './app/*.db', './mysql/database/*', './app/**/migrations/*']


def clean():
  print('Cleaning temp file...')
  for path in TMP:
    for _ in glob.glob(path, recursive=True):
      if _.endswith("__init__.py"):
        continue
      if os.path.isfile(_):
        print(f'remove {_}')
        os.remove(_)
      else:
        print(f'remove {_}')
        shutil.rmtree(_)
  print('Finish clean tmp!')


def clean_docker():
  print('Cleaning docker file...')
  os.system("docker system prune -f")
  print('Finish cleaning docker!')


def build():
  # os.system("sudo systemctl start docker")
  print('Building compose...')
  stop()
  clean()
  clean_docker()
  debug = input('Debug? y=Yes, other=No: ')
  if debug == 'y':
    os.system("docker-compose up --build")
  else:
    os.system("docker-compose up -d --build ")
    exec_to_app()
  print('\nFinish task!')


def stop():
  print('Stopping docker containers...')
  os.system("docker stop $(docker ps -aq)")
  print('Finish stopping!')


def restart():
  print('Restarting docker containers...')
  os.system("docker restart $(docker ps -aq)")
  print('Finish restarting!')


def exec_to_app():
  os.system("docker exec -it backend_app_1 /scripts/wait-for-it.sh mysql:3306 -t 0 -- sh")


def exec_to_mysql():
  os.system("docker exec -it backend_mysql_1 mysql -uroot -padmin")


def clean_all():
  print('Cleaning everything...')
  stop()
  clean()
  os.system("docker system prune -af")
  print('Finish cleaning all!')


def shell():
  os.system("sh")


wish_dict = {
  0: shell,
  1: build,
  2: clean,
  3: clean_docker,
  4: stop,
  5: restart,
  6: exec_to_app,
  7: exec_to_mysql,
  8: clean_all,
  9: lambda: None
}


def wish()->bool:
  val = None
  try:
    val = int(input("Things this script can do:\
      \n0. Shell command\
      \n1. Build docker-compose (stop, clean docker and exec to app by default)\
      \n2. Clean temp data (Stop all docker containers by default)\
      \n3. Clean docker (containers, volumes but not pulled images)\
      \n4. Stop all docker containers\
      \n5. Restart all docker cotainers\
      \n6. Exec to app\
      \n7. Exec to database\
      \n8. Clean all\
      \n9. Exit\
      \nWhat do you want?: "))
  except:
    while val is None or val not in range(10):
      try:
        val = int(input("Invalid input, please choose again"))
      except:
        val = None
  wish_dict[val]()
  return val != 9


if __name__ == "__main__":
  while wish():
    print("_" * 60)
  print('Bye!')