# 🟠 Dashboard de Usuários - FastAPI + MongoDB

Projeto de **Dashboard de Gestão de Usuários** utilizando **FastAPI** como backend, **MongoDB** como banco de dados e **HTML/CSS** para frontend.  
O layout possui **Dark Mode** em tons alaranjados e permite criar, editar, deletar e listar usuários de forma simples e funcional.

---

## 🛠 Tecnologias

- **Backend:** FastAPI  
- **Banco de Dados:** MongoDB via PyMongo  
- **Frontend:** HTML + CSS (Dark Mode)  
- **Containerização:** Docker + Docker Compose  
- **Python:** 3.12  

---

## ⚙️ Funcionalidades

- ✅ Criar novos usuários (ID e Nome)  
- ✅ Editar usuários existentes  
- ✅ Deletar usuários  
- ✅ Listar todos os usuários em cards  
- ✅ Layout responsivo e Dark Mode  

---

## 📁 Estrutura do Projeto

project/
│
├─ app/
│ ├─ static/
│ │ ├─ dashboard.html # Frontend HTML
│ │ └─ dashboard.css # Estilo CSS
│ ├─ main.py # Aplicação FastAPI
│ └─ schemas/
│ └─ database.py # Conexão com MongoDB
│
├─ Dockerfile
├─ docker-compose.yml
└─ requirements.txt

yaml
Copiar código

---

## 🚀 Executando o Projeto

### 1. Instalar Docker e Docker Compose
- [Docker](https://docs.docker.com/get-docker/)  
- [Docker Compose](https://docs.docker.com/compose/install/)

### 2. Subir o projeto
No terminal, dentro da pasta do projeto:

```bash
docker-compose up -d --build
3. Acessar o Dashboard
Abra o navegador em:

arduino
Copiar código
http://localhost:8000/
📦 Dependências
No arquivo requirements.txt:

makefile
Copiar código
fastapi==0.115.2
uvicorn[standard]==0.30.6
pymongo
python-multipart
🔧 Configuração do MongoDB
O Docker Compose inicializa o MongoDB com:

Usuário: admin

Senha: secret

Banco de dados: mydatabase

Porta: 27017

A conexão está configurada em app/schemas/database.py.

🔗 Rotas do Backend
Método	Rota	Descrição
GET	/users/all	Listar todos os usuários
GET	/users/find	Buscar usuário por ID
POST	/users/add	Criar novo usuário
PUT	/users/update	Atualizar usuário existente
DELETE	/users/remove	Remover usuário

🎨 Design
Layout Dark Mode com tons alaranjados

Botões coloridos com hover animado

Interface limpa e responsiva

Frontend em HTML/CSS com JS embutido

👤 Autor
Gabriel Cardoso - 2025
