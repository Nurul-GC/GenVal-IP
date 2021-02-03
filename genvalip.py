# ******************************************************************************
#  Direitos Autorais (c) 2019-2021 Nurul GC                                    *
#                                                                              *
#  Jovem Programador                                                           *
#  Estudante de Engenharia de Telecomunicações                                 *
#  Tecnologia de Informação e de Medicina.                                     *
#  Foco Fé Força Paciência                                                     *
#  Allah no Comando.                                                           *
# ******************************************************************************

import colorama as cor_terminal
from pprint import pformat
from random import randint
from socket import gethostbyaddr
from time import sleep, time

# iniciando a instancia que vai colorir as letras do terminal
cor_terminal.init(autoreset=True)
n_ip = 0
n_erros = 0
lista_ip = []
lista_erros = []


def geraIP():
    """gerando os IPs"""
    ip = f"{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}"
    return ip


def validaIP(ip_addr: str):
    """validando os IPs"""
    global n_erros
    try:
        # usando a função gethostbyaddr() para achar o DNS do IP
        ipValido = gethostbyaddr(ip_addr)
        if ipValido:
            return True
    except Exception:
        n_erros += 1
        lista_erros.append(n_erros)
        return False


def geraListaIP():
    """organizando a lista dos IPs"""
    global n_ip
    while n_ip <= 3:
        ipGerado = geraIP()
        if validaIP(ipGerado):
            n_ip += 1
            lista_ip.append(ipGerado)
        elif ipGerado in lista_ip:
            n_ip -= 1
        else:
            n_ip -= 1
    return sorted(lista_ip)


if __name__ == '__main__':
    print(f"""{cor_terminal.Fore.YELLOW}
    **************************************
    *             GenVal-IP              *
    **************************************
    [1] - IMPRIMIR A LISTA DE IPs
    [2] - CRIAR FICHEIRO .txt COM A LISTA DE IPs
    [s] - SAIR
    """)
    try:
        while True:
            a = input(f"{cor_terminal.Fore.CYAN}Sua opção:\n> ").lower()
            if a == '1':
                tempo_inicio = time()
                print(f"{cor_terminal.Fore.CYAN}[i] - GERANDO OS IPs, POR FAVOR AGUARDE..\n")
                print(pformat(geraListaIP()))
                tempo_final = time()
                tempo_duracao = tempo_final-tempo_inicio
                print(f"{cor_terminal.Fore.GREEN}[i] - CONCLUIDO!\n\t{cor_terminal.Fore.RED}OCORRERAM {len(lista_erros)} ERROS\n\t{cor_terminal.Fore.CYAN}DURANTE {tempo_duracao}s..")
                exit(0)
            elif a == '2':
                print(f"{cor_terminal.Fore.CYAN}[i] - GERANDO OS IPs, POR FAVOR AGUARDE..\n")
                with open("listaIPs/ipsValidos.txt", 'w+') as ipsValidos:
                    ipsValidos.writelines(geraListaIP())
                print(f"{cor_terminal.Fore.GREEN}[i] - Lista gerada com sucesso!\n\tVerifique o ficheiro './listaIPs/ipsValidos.txt' ..")
                exit(0)
            elif a == 'q' or 's':
                print(f"{cor_terminal.Fore.YELLOW}[i] - TERMINANDO..")
                sleep(2)
                exit(0)
            else:
                print(f"{cor_terminal.Fore.RED}[x] - DIGITE APENAS [1, 2 ou s]..\n")
    except Exception:
        exit(0)
