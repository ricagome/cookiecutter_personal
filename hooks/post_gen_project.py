print("Bye bye")
import os
import subprocess

# Definir colores
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

# Iniciar ambiente virtual
subprocess.call(['python', '-m', 'venv', 'venv'])

# Path to a Python interpreter that runs any Python script
# under the virtualenv /path/to/virtualenv/
python_venv =   os.getcwd()+"\\venv\\Scripts\\python.exe"

subprocess.call([python_venv,'-m', 'pip', '--upgrade', 'pip'])
subprocess.call([python_venv,'-m', 'pip', 'install', '-r', 'requirements.txt'])


# Configurar el ambiente para recibir notebooks.

if '{{ cookiecutter.project_packages }}' == 'Notebook':
  subprocess.call([python_venv,'-m', 'ipykernel', 'install', '--user', '--name', 'venv'])


print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")