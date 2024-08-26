## Scan-Port
Scan-Port é um script em Python que tem como objetivo realizar uma varredura de portas em um determinado host. O script foi desenvolvido com o intuito de facilitar a identificação de portas abertas em um host, sendo assim, o script é capaz de identificar as portas abertas de um host, além de identificar o serviço padrão que está rodando em uma determinada porta, caso ele esteja mapeado.

## Como usar
Para utilizar o script, basta clonar o repositório, instalar as dependências através do comando `pip install -r requirements.txt` e executar o script passando o host que deseja realizar a varredura. Exemplo:
```bash
python3 scan_port.py
```
O script irá solicitar o host que deseja realizar a varredura, basta informar o host, a porta inicial e a porta final que deseja realizar a varredura.

## Exemplo
```bash
python3 scan_port.py
Host: localhost
Porta inicial: 1
Porta final: 100
```
O script irá realizar a varredura de portas do host `localhost` de 1 a 100.

