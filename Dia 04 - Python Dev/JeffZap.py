import flet as ft

#função principal para executar o aplicativo
def main(pagina):
    # Titulo da aplicação
    titulo = ft.Text('JeffZap')

    # Tunel de comunicação entre usuários
    def websocket_chat(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()
    
    pagina.pubsub.subscribe(websocket_chat)

    # Função para enviar mensagem
    def enviar_mensagem(event):
        nome_usuario = text_area.value
        texto_mensagem = envia_mensagem.value
        
        mensagem = f"{nome_usuario}: {texto_mensagem}"
        pagina.pubsub.send_all(mensagem) # Envia a mensagem para todos os usuários
        envia_mensagem.value = '' # Limpa o campo de texto
        pagina.update()

    envia_mensagem = ft.TextField(label='Digite sua mensagem', on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)

    linha_enviar = ft.Row([envia_mensagem, botao_enviar]) # Cria uma linha com o campo de texto e o botão
    chat = ft.Column()

    def enter_chat(event):
        popup.open = False # Fecha o modal

        pagina.remove(titulo)
        pagina.remove(botao)
        pagina.add(chat)
        pagina.add(linha_enviar)

        nome_usuario = text_area.value
        mensagem = f'{nome_usuario} entrou no chat'
        pagina.pubsub.send_all(mensagem)
        
        pagina.update()
    
    # Criar pop-up
    titulo_popup = ft.Text('Bem vindo ao JeffZap')
    text_area = ft.TextField(label='Digite seu nome')
    botao_popup = ft.ElevatedButton('Entrar no Chat', on_click=enter_chat)
    popup = ft.AlertDialog(title= titulo_popup, content= text_area, actions= [botao_popup])

    # Abre o modal
    def open_dialog(event):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    # Botão inicial
    botao = ft.ElevatedButton('Iniciar Chat', on_click=open_dialog)

    # Adiciona os elementos na página
    pagina.add(titulo)
    pagina.add(botao)
    



# Executa a aplicação
ft.app(main, view=ft.WEB_BROWSER)