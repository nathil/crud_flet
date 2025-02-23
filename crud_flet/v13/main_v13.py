"""
    V 13.0
    Nesta versão o objetivo foi mover a interface de cadastro e a tabela para os arquivos
    apropriados. Os componentes do cadstro foram movidos para a View do arquivo tela_cadastro.py
    Para esse arquivo também foi movida a função cadastrar e o dicionário componentes.
    Na função cadastrar o banco de dados é chamado a partir da importação de controle.
    Isso signigica que o banco de dados da aplicação foi remanejado para o arquivo controle,
    é uma variável global e foi inicializado no escopo da função init.
    Para o arquivo tela_tabela.py nós movemos os componentes da tabela e as funções de
    preenchimento da tabela. Neste arquivo nós também movemos o dicionário componentes.
    A última modificação que foi feita foi na função navegacao do arquivo controle. No escopo
    dessa função nós inserimos uma condição para atualizar as linhas corrente tabela toda vez
    que a aba da tela da tabela for clicada.
"""
import flet as ft
import controle as con

def main(page: ft.Page):   
    con.init(page)         
    page.title = "Sistema de cadastro"           
    page.on_route_change = con.controle_de_rota  
    page.theme_mode  = "light"
    page.go('1')


ft.app(target=main)

