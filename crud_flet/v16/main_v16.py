"""
    V 16.0
    Neta versão nós inserimos uma nova coluna na tabela para permitir excluir e editar
    os usuários cadastrados. Na função preencher_linha_tabela, nós inserimos mais
    uma DataCell que por sua vez recebe uma Row. Utilizamos a Row pois estamos inserindo
    dois ícones nessa célula. Os ícones inseridos são os IconButton.
    
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

