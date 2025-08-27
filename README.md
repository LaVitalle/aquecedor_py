# API FastAPI

Uma API básica construída com FastAPI, incluindo operações CRUD para usuários e itens.

## 🚀 Funcionalidades

- **Usuários**: CRUD completo (Create, Read, Update, Delete)
- **Itens**: CRUD completo (Create, Read, Update, Delete)
- **Documentação automática**: Swagger UI e ReDoc
- **Validação de dados**: Pydantic schemas
- **CORS configurado**: Para integração com frontend
- **Estrutura modular**: Organização em módulos separados

## 📋 Pré-requisitos

- Python 3.8+
- pip

## 🛠️ Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd aquecedor_py
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🚀 Executando a aplicação

### Desenvolvimento
```bash
python main.py
```

### Produção
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

A API estará disponível em: `http://localhost:8000`

## 📚 Documentação

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔗 Endpoints

### Usuários
- `GET /api/v1/users/` - Lista todos os usuários
- `GET /api/v1/users/{user_id}` - Obtém um usuário específico
- `POST /api/v1/users/` - Cria um novo usuário
- `PUT /api/v1/users/{user_id}` - Atualiza um usuário
- `DELETE /api/v1/users/{user_id}` - Remove um usuário

### Itens
- `GET /api/v1/items/` - Lista todos os itens
- `GET /api/v1/items/{item_id}` - Obtém um item específico
- `POST /api/v1/items/` - Cria um novo item
- `PUT /api/v1/items/{item_id}` - Atualiza um item
- `DELETE /api/v1/items/{item_id}` - Remove um item

### Outros
- `GET /` - Página inicial
- `GET /health` - Verificação de saúde da API

## 📁 Estrutura do Projeto

```
aquecedor_py/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── item.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── users.py
│   │   └── items.py
│   └── schemas/
│       ├── __init__.py
│       ├── user.py
│       └── item.py
├── main.py
├── config.py
├── requirements.txt
└── README.md
```

## 🔧 Configuração

Crie um arquivo `.env` na raiz do projeto para configurar variáveis de ambiente:

```env
DEBUG=true
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///./app.db
```

## 🧪 Testando a API

### Exemplo de criação de usuário:
```bash
curl -X POST "http://localhost:8000/api/v1/users/" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "João Silva",
       "email": "joao@example.com",
       "age": 30
     }'
```

### Exemplo de criação de item:
```bash
curl -X POST "http://localhost:8000/api/v1/items/" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Produto Teste",
       "description": "Descrição do produto",
       "price": 29.99,
       "available": true
     }'
```

## 🚀 Deploy no EasyPanel

### Pré-requisitos
- Conta no EasyPanel
- Repositório no GitHub com o código da aplicação

### Passos para Deploy

1. **Preparar o repositório GitHub:**
   - Faça commit e push de todos os arquivos para o GitHub
   - Certifique-se de que os arquivos `Dockerfile`, `docker-compose.yml`, `requirements.txt` e `start.sh` estão no repositório

2. **No EasyPanel:**
   - Acesse o painel do EasyPanel
   - Clique em "Novo Projeto" ou "Adicionar Aplicação"
   - Selecione "GitHub" como método de deploy
   - Conecte sua conta GitHub (se ainda não estiver conectada)
   - Selecione o repositório `aquecedor_py`
   - Escolha a branch (geralmente `main` ou `master`)

3. **Configurações do Deploy:**
   - **Tipo de aplicação:** Python
   - **Comando de inicialização:** `uvicorn main:app --host 0.0.0.0 --port 8000`
   - **Porta:** 8000
   - **Variáveis de ambiente:** (opcional)
     ```
     DEBUG=False
     SECRET_KEY=your-production-secret-key
     ```

4. **Deploy:**
   - Clique em "Deploy" ou "Publicar"
   - Aguarde o processo de build e deploy
   - A aplicação estará disponível no domínio fornecido pelo EasyPanel

### Arquivos de Deploy Criados
- `Dockerfile` - Para containerização
- `docker-compose.yml` - Para orquestração de containers
- `start.sh` - Script de inicialização
- `.dockerignore` - Para otimizar o build

## 🔮 Próximos Passos

- [x] Docker containerization
- [ ] Integração com banco de dados real (PostgreSQL/MySQL)
- [ ] Autenticação e autorização (JWT)
- [ ] Testes automatizados
- [ ] CI/CD pipeline
- [ ] Logging e monitoramento
- [ ] Rate limiting
- [ ] Cache (Redis)

## 📝 Licença

Este projeto está sob a licença MIT.
