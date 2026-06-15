from datetime import datetime

def log(message, type="DEFAULT"):
  ERROR = '\033[31m'
  SUCCESS = '\033[32m'
  WARNING = '\033[33m'
  INFO = '\033[34m'
  RESET = '\033[0m'
  now = datetime.now().isoformat(timespec='seconds')

  color = ""
  match type:
    case "ERROR":
      color = ERROR
    case "SUCCESS":
      color = SUCCESS
    case "WARNING":
      color = WARNING
    case "INFO":
      color = INFO
    case "DEFAULT":
      color = RESET
  
  content = f'[{now}] {color}{type}{RESET} - {message}'
  print(content)
