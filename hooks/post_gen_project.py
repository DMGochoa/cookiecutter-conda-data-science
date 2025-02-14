import os
import subprocess

project_slug = "{{ cookiecutter.project_slug }}"

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])
subprocess.call(['conda', 'env', 'create', '--file', 'environment.yml'])

print(f"{MESSAGE_COLOR}It's ready the git repository{RESET_ALL}")
