import time
import sys
import importlib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Import the module that has your main() function
import build   # assumes you have runner.py with a main() function


class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"File changed: {event.src_path}")

        # Reload module to get the latest code
        importlib.reload(build)

        # Run the main function
        try:
            build.main()
        except Exception as e:
            print(f"Error running main: {e}")


def watch(folder="src"):
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, folder, recursive=True)
    observer.start()

    print(f"Watching folder: {folder}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


if __name__ == "__main__":
    folder_to_watch = "src"
    if len(sys.argv) > 1:
        folder_to_watch = sys.argv[1]
    watch(folder_to_watch)
