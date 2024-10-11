# tela inicial:
    # titulo
    # botao para iniciar o chat
        # quando clicar no botao abrir um pop up
            # um titulo "bem vindo ao pacezap"
            # uma caixa de texto para escrever o nome no chat
            # um botao para entrar no site  
                # mudar o titulo
                # sumir com o pop up
                # carregar o chat  
                # carregar o espaco de digitar a msg
                # botao para enviar as msgs
                    # quando clicar no botao alem de enviar limpa a msg

# irei utilizar o flet
# passo 1: importar o flet
import flet as ft

# passo 2: cria um funcao principal pra rodar o aplicativo
def main (pagina):

    # adicionar um titulo
    titleInit = ft.Text("PaceZap") 

    # websocket - tunel de comunicacao entre usuarios
    def send_message_tunnel(message):
        text = ft.Text(message)
        chat.controls.append(text)
        pagina.update()

    pagina.pubsub.subscribe(send_message_tunnel)
    
    # criando a funcao de enviar a msg
    def send_message(event):
        user_name = box_name
        text_box_message = box_show_message.value
        message = f"{user_name}: {text_box_message}"
        pagina.pubsub.send_all(message) 
        box_show_message.value = ""
        pagina.update()

    # campo enviar msg
    box_show_message = ft.TextField(label="Write your message")
    button_send = ft.ElevatedButton(label="Send message", on_click= send_message)
    row_send = ft.Row([box_show_message,button_send])

    # criando a visualizacao do chat em coluna
    chat = ft.Column()

    # entra no chat
    def join_chat(event):
        # sumir com o pop up
        popup.open = False

        # mudar o titulo
        pagina.remove(titleInit)
        
        # sumir com o botao iniciar
        pagina.remove(buttonInit)

        # carregar o chat
        pagina.add(chat)

        # sumir com o botao iniciar chat
        pagina.add(button_send)

        # carregar campo de enviar msg
        pagina.add(row_send)

        # add no chat a msg fulano entrou no chat
        user_name = box_name
        message = f"{user_name} joined in the chat"
        pagina.pubsub.send_all(message)

        # atualizando a pagina
        pagina.update()

    # criar popup
    title_popup = ft.Text("Welcome to the PaceZap!")
    box_name = ft.TextField(label= "Write your name...")
    button_popup = ft.ElevatedButton("Join in the chat", on_click= join_chat)

    popup = ft.Alertdialog(title= title_popup, content= box_name, actions= [button_popup])

    # funcao do botao de iniciar
    def open_popup (event):
        print("click")
        popup.open = True
        pagina.update()
        print("Button cliked.")

    # adicionar um botao
    buttonInit = ft.ElevatedButton("Init Chat", on_click= open_popup)
    
    # inserir os objetos na tela
    pagina.add(title)
    pagina.add(buttonInit)

# passo 3: executar uma funcao com o flet
ft.app(main, view= ft.WEB_BROWSER)