# Script helper (PowerShell) - execute manualmente para criar venv, instalar deps, rodar seed e iniciar servidor
# Uso: abra PowerShell, navegue para a pasta backend e execute: .\run-dev.ps1

Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned -Force
Write-Host "Criando virtualenv..."
python -m venv venv
Write-Host "Ativando ambiente virtual..."
.\venv\Scripts\Activate.ps1
Write-Host "Instalando dependências..."
pip install -r requirements.txt
pip install uvicorn
Write-Host "Rodando seed (populando banco)..."
python seed.py
Write-Host "Iniciando servidor uvicorn em http://127.0.0.1:8000"
uvicorn app:app --host 127.0.0.1 --port 8000 --reload
