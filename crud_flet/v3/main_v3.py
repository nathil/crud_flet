"""
    V 3.0
    Nesta versão estamos adicionando uma segunda linha com os componentes Text e TextField.
    Para adicionar várias linhas, utilizamos o componente Column. O componente Column recebe
    como argumento uma lista de componentes. A quantidade de elementos nessa lista é igual a
    quantidade de linhas na coluna. Observe que estamos passando dois componentes Row como 
    elemento de Column.
    Outra modificação dessa versão, foi a definição do tema para light. Fizemos isso atribuindo
    o valor light para a variável theme_mode da página.
    Por fim, a medida que a árvore de componentes vai crescendo, é uma boa prática de programação
    comentar onde o componente termina. Fizemos isso para os compoenntes Row e Column.
"""
import flet as ft

def main(page: ft.Page):            
    page.title = "Sistema de cadastro"  
    page.theme_mode  = "light"        
    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Text('Nome:', size=20),                   
                        ft.TextField(label='Nome')
                    ]                    
                ),#Row
                ft.Row(
                    [
                        ft.Text('Telefone:', size=20),
                        ft.TextField(label='Telefone')
                    ]
                )#Row
            ]
        )#Column
    )
            


ft.app(target=main)
