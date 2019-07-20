import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = os.path.join(BASE_DIR,'servers\\database\\dbtest.db')
LOGFILE = os.path.join(BASE_DIR,'app_demo1\\log\\test.log')
Interface_Time_Out = 500