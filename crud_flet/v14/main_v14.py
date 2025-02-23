"""
    V 14.0
    Nesta versão houve mudança visual! Nós adicionamos o componente AppBar nas daus telas (views).
    Reajustamos os componentes da tela de cadastro. No TextField do nome, passamos o argumento
    True para o parâmetro autofocus. Isso faz com que o cursor fique ativo neste campo toda vez
    que a tela é exibida. No TextField do telefone nós passamos a função cadastrar como
    argumento do parâmetro on_submit. Isso faz com que a função cadastrar seja chamada ao
    pressionar a tecla ENTER.
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

