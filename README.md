# Python Scripts

A collection of small Python scripts. Each script lives in the `python-scripting/` folder.

## Directory Backup (`python_scripting101.py`)

A command-line tool that copies a directory and everything inside it to a backup location, using only Python's standard library.

### Features

- Copies all files and subdirectories recursively
- Merges into the destination if it already exists
- Rejects invalid destinations (the source itself, or a folder inside the source)
- Resolves relative paths to absolute paths, so it works from any working directory
- No third-party dependencies

### Requirements

- Python 3.8 or newer

### Usage

```bash
python3 python-scripting/python_scripting101.py <source> <destination>
```

| Argument      | Description                                  |
|---------------|----------------------------------------------|
| `source`      | The directory to back up (must exist)        |
| `destination` | Where the backup will be created             |

To see the built-in help:

```bash
python3 python-scripting/python_scripting101.py --help
```

### Examples

Back up a documents folder to an external drive:

```bash
python3 python-scripting/python_scripting101.py ~/Documents /media/backup/Documents
```

Back up a project to a dated folder:

```bash
python3 python-scripting/python_scripting101.py ~/projects/myapp ~/backups/myapp-2026-10-26
```

On success, the script prints:

```
Backup completed: /home/user/Documents -> /media/backup/Documents
```

### Behavior notes

- **Existing destinations are merged.** If the destination folder already exists, files are copied into it. Files with the same name are overwritten, and files that exist only in the destination are left untouched.
- **Nothing is deleted.** The script never removes files from the source or the destination.
- **Invalid destinations are refused.** The destination cannot be the source directory or any folder inside it, which would cause the backup to copy into itself.
- **Missing sources produce an error.** If the source does not exist or is not a directory, the script exits with a clear message.

### Setup

```bash
git clone git@github.com:soltansam/python_scripts.git
cd python_scripts
python3 python-scripting/python_scripting101.py --help
```

## License

Add a license of your choice (for example MIT) if you want others to reuse this code.
