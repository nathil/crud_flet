"""
    V 9.0
    Nesta versão estamos inserindo as linhas da tabela dinamicamente. Para isso, criamos a função
    atualizar_tabela que faz um mapeamento da lista banco_de_dados para uma lista em que cada
    elemento é um componente DataRow. O componente DataRow precisa receber como argumento uma
    lista que é atribuida ao parâmetro cells. Os elementos dessa lista precisam ser do tipo
    DataCell e a quantidade de elementos DataCell tem que ser igual à quantidade de colunas
    da tabela. Para montar a lista de elementos DataCell, foi criada uma função chamada
    preencher_linha_tabela que é a função responsável pela transformação realizada no mapeamento.
    O preenchimento da tabela está ocorrendo no momento em que um cadastro é realizado. No escopo
    da função cadastrar, as linhas correntes da tabela estão sendo atualizadas recebendo o retorno
    da função atualizar_tabela. No escopo da função cadastrar também estamos fazendo a atualização
    dos dois campos de texto, limpando os seus valores correntes, a partir da atribuição de uma
    string vazia.
    Para que a tela seja atualizada após essas modificações, é necesário chamar a função update
    da página. Para isso, foi necessário criar uma variável global pagina no escopo da função
    main. Essa variável global recebe o valor do atributo da função main que é justamente a página.
    Tendo a variável global é possível utilizá-la em qualquer função do nosso arquivo. 


"""
import flet as ft

componentes = {
        'tf_nome': ft.Ref[ft.TextField](),
        'tf_telefone': ft.Ref[ft.TextField](), 
        'tabela': ft.Ref[ft.DataTable](),       
        #add todos os compontens da tela aqui
    }

banco_de_dados = []

def main(page: ft.Page): 
    global pagina
    pagina = page          
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
                
                ft.ElevatedButton('Cadastrar', icon='save', on_click=cadastrar),
                ft.DataTable(
                            width=float('inf'),
                            ref=componentes['tabela'],                                                    
                            columns=[
                                ft.DataColumn(ft.Text("Nome")),
                                ft.DataColumn(ft.Text("Telefone")),                                                                                                
                            ],
                            #rows=[] são ser carregadas dinamicamente
                         ),                                                     
            ]
        )#Column
    )
            
def cadastrar(e):    
    usuario = {
        'nome' : componentes['tf_nome'].current.value,
        'telefone' : componentes['tf_telefone'].current.value
    }    
    
    banco_de_dados.append(usuario)
    componentes['tf_nome'].current.value = ""
    componentes['tf_telefone'].current.value = ""
    componentes["tabela"].current.rows = atualizar_tabela()
    pagina.update()

    
def atualizar_tabela():
    return [
            ft.DataRow(cells=preencher_linha_tabela(cadastro))
            for cadastro in banco_de_dados
        ]


def preencher_linha_tabela(cadastro):
    return [
                ft.DataCell(ft.Text(cadastro['nome'])),
                ft.DataCell(ft.Text(cadastro['telefone']))                                                           
        ]

ft.app(target=main)
