"""
    V 6.0
    Nesta versão estamos imprimindo os valores digitados nos campos nome e telefone quando o
    usuário clica no botão cadastrar. Para que isso seja possível, primeiro devemos definir
    a referência dos componentes TextField para poder recuperar os valores neles digitados.
    Definimos as referências criando uma restrutura dicionário. A chave de cada elemento do
    dicionário corresponde ao nome da referência e o valor corresponde ao componente Ref
    especificando o generics do componente referênciado. No nosso caso, os dois componentes
    referenciados são do tipo TextField.
    Uma vez que o dicionário é criado, utilizamos os seus elementos como argumento dos
    componentes TextField da nossa árvore de componentes. Fazemos isso definindo o argumento
    passando para o parâmetro ref do TextField. Para o TextField do nome, definimos
    ref=componentes['tf_nome'] e para o TextField do telefone, definomos 
    ref=componentes['tf_telefone']. Ao fazer isso, podemos recuperar o valor digitado pelo
    usuário a partir da referência. Estamos fazendo isso na função cadastrar!
    na função, estamos imprimindo o valor corrente dos componentes referenciados.

"""
import flet as ft

componentes = {
        'tf_nome': ft.Ref[ft.TextField](),
        'tf_telefone': ft.Ref[ft.TextField](),        
        #add todos os compontens da tela aqui
    }

def main(page: ft.Page):            
    page.title = "Sistema de cadastro"  
    page.theme_mode  = "light"        
    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(content=ft.Text('Nome:', size=20), width= 150),                      
                        ft.TextField(label='Nome', ref=componentes['tf_nome'])
                    ]                    
                ),#Row
                ft.Row(
                    [
                        ft.Container(content=ft.Text('Telefone:', size=20), width=150),
                        ft.TextField(label='Telefone', ref=componentes['tf_telefone'])
                    ]
                ),#Row
                
                ft.ElevatedButton('Cadastrar', icon='save', on_click=cadastrar)                                                      
            ]
        )#Column
    )
            
def cadastrar(e):        
    print(componentes['tf_nome'].current.value)
    print(componentes['tf_telefone'].current.value)

ft.app(target=main)
