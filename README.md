# Introdução

Nesse artigo aborda a integração Python com Google Drive, mostrando como é feita a configuração e depois a implementação de um upload de arquivo, adicionar permissões para ser um arquivo público e depois gerar o link para acesso ao arquivo. Depois do link gerado, irei mostrar a codificação de um envio de email utilizando o smtp do gmail.

------------ goole_drive_upload.py

# Instalação
`pip install PyDrive`

# Autenticação
O arquivo de credenciais exportado precisa ser renomado para client_secrets.json
A Autenticação é feita por essas funções e através do json de autenticação

`g_login = GoogleAuth()`

`drive = GoogleDrive(g_login)`

# Upload File
`file = open('teste.txt')`

`fn = os.path.basename(file.name)`

`file_drive = drive.CreateFile({'title': fn })`

`file_drive.SetContentString(file.read())`

`file_drive.Upload()`


# Adicionando Permissão para público
OBS: Se não adicionar essa função, os arquivos serão privados e o acesso via login e senha

`permission = file_drive.InsertPermission({'type': 'anyone','value': 'anyone','role': 'reader'})`

# URL do arquivo
`file_drive['alternateLink']`

------------ send_email.py - Codificação do Envio de Email com smtp do GMAIL

# Configuração
- email_smtp_ssl_host=smtp.gmail.com
- email_smtp_ssl_port=465
- email_username=email@gmail.com
- email_password=senha
- email_from_addr=email@gmail.com

# Criação da Mensagem
        `message = MIMEText(text)`
        `message['subject'] = title`
       `message['from'] = from_addr`
        `message['to'] = ', '.join(to_addrs)`

# Envio do Email
        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        server.login(username, password)
        server.sendmail(from_addr, to_addrs, message.as_string())


# Artigo completo
https://medium.com/p/integra%C3%A7%C3%A3o-google-drive-com-python-e-enviar-o-link-pelo-gmail-5d048907976
