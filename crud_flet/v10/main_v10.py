"""
    V 10.0
    Nesta versão o objetivo é implementar a navegação de telas. Para isso precisamos passar
    como argumento uma função responsável pelo controle de rotas da nossa página. Essa função
    deve ser passada para o parâmetro on_route_change da página. A função passada foi a
    controle_de_rota. Quando se trabalha com várias páginas, o que se tem na verdade são várias
    views. No escopo da função controle_de_rota o que nós fazemos são três coisas:
    1- limpamos a lista de views
    2- inserimos a view desejada na lista
    3- atualizamos a página
    A função controle_de_rota que foi passada para o parâmetro on_route_change da página sempre
    será chamada quando a função go da página for acionada. O parâmetro route_event armazena o
    argumento passado para a função go.
    Cada tela foi construída utilizando o componente View. Ao utilizar este componente, passamos
    dois argumentos. Uma string representando o nome da view e uma lista de componentes da tela.
    As duas telas construídas estão nas funções view1 e view2. Para conseguir navegar entre as
    telas, nós criamos um dicionário telas no escopo da função main. A chave corresponde ao
    índice da tela e o valor o retorno das funções view1 e view2 que criamos. Observe que nós
    criamos duas variáveis globais para poder utilizá-las em todas as funções do nosso arquivo.
    Ainda no escopo da função main, ao chamar a função go e passar como argumento o valor 1,
    estamos informando que a nossa tela da função view1 é que será exibida inicialmente.
    Em cada umas das telas nós temos o componente ElevatedButton com o on_click definido. Para
    cada on_click nós criamos uma função anônima e fizemos a chamada da função go no seu escopo.
    LEMBRE, A CHAMADA DA FUNÇÃO GO ACIONA A NOSSA FUNÇÃO controle_de_rota!

"""
import flet as ft

def main(p: ft.Page):  
    global page , telas
    page = p    
    telas = {
        '1': view1(),
        '2': view2()
    }
    page.title = "Sistema de cadastro"           
    page.on_route_change = controle_de_rota  
    page.theme_mode  = "light"
    page.go('1')


def controle_de_rota(route_event):    
    page.views.clear()    
    page.views.append(telas[route_event.route])          
    page.update()


def view1():     
    return ft.View(   
                "tela1",             
                [                           
                    ft.Text('Tela 1', size=20),
                    ft.ElevatedButton('ir para a tela 2', on_click= lambda e: page.go("2"))

                ],                                    
            )

def view2():     
    return ft.View(
                "tela2",
                [                           
                    ft.Text('Tela 2', size=20),
                    ft.ElevatedButton('ir para a tela 1', on_click= lambda e: page.go("1"))                    
                ],                                    
            )



ft.app(target=main)

