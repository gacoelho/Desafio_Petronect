import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

postgres_url = os.environ.get('POSTGRES_URL')

# Usando o valor obtido
print(postgres_url)