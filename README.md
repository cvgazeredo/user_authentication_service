# MVP 03 - Project HomeBroker 

Projeto de uma aplicação responsavel por comprar e vender ações. 

---

## Componente D: User Authentication
 + Gerencia autenticação e registro de usuários;
 + Permite que o usuário se cadastre, faça login e gerencie suas informações;
 + Implementa autenticação baseada em tokens.

---



### Execução através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) 
instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal.
Execute **como administrador** o seguinte comando para construir a imagem Docker:


```
docker build -t authentication .
```

Caso nao esteja criada, execute o comando abaixo, para a criação de uma nova
network:

```
docker network create <my_network> 
```

Para a execução o container basta executar, **como administrador**, seguinte o comando:
```
docker run -p 8000:8000 --name authentication --network <my_network> authentication
```