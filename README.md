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
```
