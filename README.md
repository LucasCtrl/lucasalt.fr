# lucasalt.fr

## Development
```sh
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install all dependencies
pip install -r requirements.txt

# Install watchdog to watch src folder
pip install watchdog

# Run the watcher to rebuild everytime a change is done
python -X dev watcher.py

# Start a live server on 127.0.0.1:8000 or 0.0.0.0:8000 - https://docs.python.org/3/library/http.server.html#command-line-interface
python -m http.server 8000 --directory dist/
```
