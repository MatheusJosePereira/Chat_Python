import flet as ft


#Criar função principal do App

def main(pagina):
    
    #funcionalidades
    
    
    
    titulo = ft.Text('MaZap')
    
    titulo_janela = ft.Text('MaZap')
    campo_nome_usuario = ft.TextField(label='digite seu nome')
    
    
    
    chat = ft.Column()
    campo_mensagem = ft.TextField(label='Digite sua mensagem')
    
    def enviar_mensagem_tunel(mensagem):
        texto_chat =  ft.Text(mensagem)
        chat.controls.append(texto_chat)
        texto_entrar_chat = ft.Text()
        chat.controls.append(texto_entrar_chat)
        pagina.update()
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    def enviar_mensagem(evento):
        texto_mensagem = campo_mensagem.value
        nome_usuario = campo_nome_usuario.value
        mensagem = f"{nome_usuario}: {texto_mensagem}"
       
        pagina.pubsub.send_all(mensagem)
       
        
        campo_mensagem.value=''
 
        pagina.update()
        
    botao_enviar_mensagem = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    
    linha_mensagem = ft.Row([campo_mensagem, botao_enviar_mensagem])
    
    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False
        
        pagina.add(chat)
        pagina.add(linha_mensagem)
        mensagem = f"{campo_nome_usuario.value}: Entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()
        
    botao_entrar = ft.ElevatedButton('Confirmar', on_click= entrar_chat)
    janela = ft.AlertDialog(
            title=titulo_janela,
            content=campo_nome_usuario,
            actions=[botao_entrar]
        )
    
    
    
    
    def iniciar_chat(evento):
        pagina.dialog = janela
        janela.open = True    
        pagina.update()
    
    botao_iniciar = ft.ElevatedButton('Iniciar Bate-Papo', on_click=iniciar_chat)
    
    #Adiciona e valida elemento para visualização do APP
    pagina.add(titulo)
    pagina.add(botao_iniciar)
    
#Iniciar o APP

ft.app(target = main)