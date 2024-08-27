## Bienvenido al proyecto correspondiente a la semana número 7
## crear entorno virtual
python -m venv venv
## activar entorno virtual
.\venv\Scripts\activate
## Instalar dependendias del proyecto
pip install -r requerirements.txt  
## Ejecutar en la base de datos el script ubicado en la carpeta script_db
script_db\comercializadora.sql
## Ejecutar proyecto
python run.py