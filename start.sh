#!/bin/bash

# Script de inicialização para o EasyPanel

echo "Iniciando a aplicação FastAPI..."

# Instalar dependências se necessário
if [ -f "requirements.txt" ]; then
    echo "Instalando dependências..."
    pip install -r requirements.txt
fi

# Executar migrações se existirem
if [ -f "alembic.ini" ]; then
    echo "Executando migrações..."
    alembic upgrade head
fi

# Iniciar a aplicação
echo "Iniciando servidor..."
exec uvicorn main:app --host 0.0.0.0 --port 8000
