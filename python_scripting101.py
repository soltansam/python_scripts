import argparse  # Parse the source and destination arguments from the command line.
import shutil  # Provide the directory-copying function.
from pathlib import Path  # Handle filesystem paths in a cross-platform way.


def main() -> None:  # Define the script's main entry point.
    parser = argparse.ArgumentParser(  # Create the command-line argument parser.
        description="Copy a directory and its contents to a backup location."  # Describe the script's purpose.
    )  # Finish creating the parser.
    parser.add_argument("source", type=Path, help="directory to back up")  # Accept the directory to copy.
    parser.add_argument("destination", type=Path, help="backup destination")  # Accept where to copy it.
    args = parser.parse_args()  # Read the values supplied when running the script.

    source = args.source.resolve()  # Convert the source to an absolute path.
    destination = args.destination.resolve()  # Convert the destination to an absolute path.

    if not source.is_dir():  # Check that the source exists and is a directory.
        parser.error(f"source directory does not exist: {source}")  # Stop with a clear error if it does not.
    if destination == source or source in destination.parents:  # Prevent copying into the source directory.
        parser.error("destination must not be the source directory or inside it")  # Explain the invalid destination.

    shutil.copytree(source, destination, dirs_exist_ok=True)  # Copy all files and subdirectories, merging if needed.
    print(f"Backup completed: {source} -> {destination}")  # Report the completed backup.


if __name__ == "__main__":  # Only run the backup when this file is executed directly.
    main()  # Start the command-line program.
