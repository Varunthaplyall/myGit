
import argparse, collections, difflib, enum, hashlib, operator, os, stat
import struct, sys, time, urllib.request, zlib


class ObjectType(enum.Enum):
    commit = 1
    tree = 2
    blob = 3


def read_file(path):
    """Read contents of file at given path as bytes."""
    with open(path, 'rb') as f:
        return f.read()


def write_file(path, data):
    """Write data bytes to file at given path."""
    with open(path, 'wb') as f:
        f.write(data)

def init(repo):
    """Create directory for repo and initialize .git directory."""
    try:
        # Check if the repo folder already exists
        if os.path.exists(repo):
            print(f"Error: Directory '{repo}' already exists.")
            return

        os.mkdir(repo)
        os.mkdir(os.path.join(repo, '.git'))

        for name in ['objects', 'refs', 'refs/heads']:
            os.mkdir(os.path.join(repo, '.git', name))

        write_file(os.path.join(repo, '.git', 'HEAD'), b'ref: refs/heads/master')

        print(f'Initialized empty repository: {repo}')

    except PermissionError:
        print("Error: You don't have permission to create files here.")
    except FileNotFoundError:
        print("Error: Invalid path or missing parent directory.")
    except OSError as e:
        print(f"OS error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
