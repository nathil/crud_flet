"""
    V 17.0
    Neta versão nós estamos programando a função de deletar. No IconButton do deletar
    definimos os valores dos parâmetros key e on_click. Para o parâmetro key passamos
    o cadastro a ser deletado. Para o parâmetro on_click passamos a função deletar
    que será chamada quando o botão for clicado.
    Na função deletar, o parâmetro recebe o controle do componente, permitindo recuperar
    o valor da key. A função deletar implica chamar a função remove da lista e passar como
    argumento o usuário a ser deletado.
    Em seguida, achamamos a função de atualizar a tabela para atualizar as linhas correntes
    da tabela. Como houve mudança na tela, finalizamos a função deletar chamando a função
    update da página.
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

