# Automação de Relatórios Diários de Ações

Este projeto automatiza o envio de relatórios diários sobre ações do mercado financeiro, utilizando a API `yfinance` para obter as informações de ações e o envio de e-mails através do protocolo SMTP.

## Funcionalidades

- **Consulta de Ações**: O script obtém dados de ações, como preço de abertura, fechamento, máximo e mínimo do dia, volume de negociações, variação percentual no dia e média móvel de 5 dias.
- **Envio de Relatórios**: Após coletar as informações, um relatório é gerado e enviado automaticamente para uma lista de e-mails definidos.
- **Agendamento Automático**: O envio do relatório é agendado para ocorrer todos os dias às 17:00.

## Tecnologias Utilizadas

- **Python 3**: Linguagem de programação principal.
- **yfinance**: Biblioteca Python para acessar dados financeiros do Yahoo Finance.
- **smtplib**: Biblioteca Python para envio de e-mails via SMTP.
- **schedule**: Biblioteca para agendamento de tarefas no Python.

## Pré-requisitos

Antes de executar o script, você deve instalar as dependências necessárias.
1. Execute o pip:
    ```bash
    pip install yfinance schedule

## Como usar

1. **Defina seu e-mail de remetente**
No arquivo *main.py*, substitua *"seu_email@gmail.com"* pelo seu e-mail e *"sua_senha_de_aplicativo"* pela senha de aplicativo do seu e-mail:
    remetente = "seu_email@gmail.com"
    senha = "sua_senha_de_aplicativo"

2. **Defina os destinatários**
No mesmo arquivo *main.py*, adicione os e-mails dos destinatários na lista *destinatarios*:
    destinatarios = ["destinatario1@gmail.com", "destinatario2@gmail.com"]

3. **Execute o script**
Execute o arquivo *main.py* para iniciar o envio de relatórios automáticos. O relatório será enviado às 17:00 todos os dias:
    ```bash
    python main.py

## Personalização

- Horário de envio: O horário do envio do relatório pode ser ajustado no código. Atualmente, está configurado para enviar às 17:00 todos os dias, mas você pode alterar essa configuração conforme a necessidade:
    ```python
    schedule.every().day.at("17:00").do(gerar_relatorio)

- Ações a serem monitoradas: A lista de ações monitoradas pode ser alterada diretamente na função gerar_relatorio no arquivo *main.py*:
    ```python
    acoes = ['TSLA34.SA', 'BBAS3.SA', 'PETR4.SA']













