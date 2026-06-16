from datetime import datetime

class Logger:
  def __init__(self, mode="DEFAULT"):
    self.mode = mode
    
    self.ERROR = '\033[31m'
    self.SUCCESS = '\033[32m'
    self.WARNING = '\033[33m'
    self.INFO = '\033[34m'
    self.DEBUG = '\033[35m'
    self.RESET = '\033[0m'
    self.now = datetime.now().isoformat(timespec='seconds')

  def set(self, message):
    print(f'[{self.now}] {self.INFO}INFO{self.RESET} - {message}')
  
  def error(self, message):
    print(f'[{self.now}] {self.ERROR}ERROR{self.RESET} - {message}')
  
  def success(self, message):
    print(f'[{self.now}] {self.SUCCESS}SUCCESS{self.RESET} - {message}')

  def warning(self, message):
    if self.mode == "WARNING" or self.mode == "DEBUG":
      print(f'[{self.now}] {self.WARNING}WARNING{self.RESET} - {message}')

  def debug(self, message):
    if self.mode == "DEBUG":
      print(f'[{self.now}] {self.DEBUG}DEBUG{self.RESET} - {message}')

log = None

def init_logger(mode):
  global log
  log = Logger(mode=mode)
