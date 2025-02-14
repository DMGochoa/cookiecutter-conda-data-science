import os
import sys

# Aquí se guarda la información que se ingresa de las variables de 
# inicio del cookiecutter
project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

if project_slug.startswith("x"):
    print(f"{ERROR_COLOR}ERROR: {project_slug=} is not a valid name for this template.")

    sys.exit(1) 

project_packages = "{{ cookiecutter.project_packages }}"

if project_packages == "ALL":
    print("There ara now 25 packages install.")
elif project_packages == "Minimal":
    print("There are now 14 packages install.")

print(f"{MESSAGE_COLOR}Let's do it! You're going to create somethin awesome!")
print(f"Creating project at { os.getcwd() }{RESET_ALL}")