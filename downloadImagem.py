import DuckDuckGoImages as ddg
import os

filtro = 'buraco'
destino = os.getcwd() + "/buracos"

print('Inicia...')
try:
    ddg.download(filtro,  folder = destino, remove_folder=False, parallel=True)
except Exception as e:
    print("Errror")
print('Download feito!')