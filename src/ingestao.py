import requests
import os
from dotenv import load_dotenv

BASE_URL = "https://teste-engenheiro.onrender.com"

# Carrega variáveis do arquivo .env
load_dotenv()

TOKEN = os.getenv("MAXINUTRI_API_TOKEN")
