#importações das bibliotecas necessárias
import os
import re
import webbrowser
import time
from colorama import Fore, init

#inicialização do colorama
init(autoreset=True)

#definição das constantes
REPO_URL = "https://github.com/morrownr/8821cu-20210916.git"
REPO_DIR = "8821cu-20210916"

#função para executar comandos no terminal
def run(cmd):
    print(Fore.CYAN + f"> {cmd}")
    return os.system(cmd)

#função para instalar dependências necessárias
def install_dependencies():
    run("sudo dnf upgrade -y")
    run(
        "sudo dnf install -y "
        "git dkms gcc make "
        "kernel-devel kernel-headers "
        "elfutils-libelf-devel"
    )

#função para limpar drivers antigos
def cleanup_old_driver():
    run("sudo dkms remove rtl8821CU/5.4.1 --all || true")
    run("sudo rm -rf /var/lib/dkms/rtl8821CU")

#
def install_driver():
    if not os.path.isdir(REPO_DIR):
        run(f"git clone {REPO_URL}")
    os.chdir(REPO_DIR)
    run("sudo ./install-driver.sh")

#função para carregar o módulo do driver
def load_module():
    run("sudo modprobe 8821cu")

#início do script principal
print(Fore.GREEN + "D-Link DWA-171 (RTL8821CU) Driver Installer - Fedora KDE")
time.sleep(2)

#verificação da instalação do git
print("Checking git installation...")
git_check = os.popen("git --version").read()

#se git não estiver instalado, instala-o
if not re.search("git version", git_check):
    print(Fore.YELLOW + "Git not found. Installing...")
    if run("sudo dnf install -y git") != 0:
        print(Fore.RED + "Failed to install git.")
        webbrowser.open("https://git-scm.com/downloads")
        exit()

#confirmação da instalação do git
print(Fore.GREEN + "Git OK\n")

#instalação das dependências
print("Installing dependencies...")
install_dependencies()

#limpeza de drivers antigos
print("Cleaning old DKMS drivers...")
cleanup_old_driver()

#instalação do driver atualizado
print("Installing updated driver...")
install_driver()

#carregamento do módulo do driver
print("Loading module...")
load_module()

#mensagem final de sucesso
print(Fore.GREEN + "\nDriver instalado com sucesso!")
print(Fore.YELLOW + "Se o Wi-Fi não aparecer após reiniciar, verifique o Secure Boot (MOK).")
