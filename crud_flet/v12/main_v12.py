"""
    V 12.0
    Nesta versão nós refatoramos a versão 11 para isolar as telas em diferentes arquivos pytthon.
    Observe que cada View está em um arquivo separado que nós chamamos de tela_cadastro.py e
    tela_tabela.py.
    Nós também criamos o arquivo controle que tem como responsabilidade orquestrar essas telas.
    Sendo assim criamos uma função init e movemos as variáveis globais para o escopo dessa
    função. A funções controle_de_rota e barra_navegacao também foram movidas para o arquivo
    controle. Na função main do arquivo principal devemos chamar a função init de controle.
    Você também vai perceber a necessidade de importar controle no arquivo principal e nos
    arquivos das telas. Essa importação é necessária justamente para conseguir utilizar as
    funções que foram movidas para lá.
    No arquivo controle também foi necessário importar as telas para poder montar o dicionário
    de telas, já que cada função view está em um arquivo separado agora.

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

