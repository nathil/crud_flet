"""
    V 19.0
    Nesta versão estamos programando o botão atualiazr da tela atualizar. Ao clicar nesse
    botão, recuperamos os valores correntes de nome e telefone. Também é recueprado o índice
    do usuário que será editado. Este índice é o índice em que ele está na lista banco_de_dados.
    Em seguida, um novo dicionário é passado para o índice especificado na lista.
    Por fim, as linhas da tabela são atualizadas e a paginação para a tela 2 é realizada.    
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

