# gerenciamento_funcionario
## Installation / Usage

#### Dependência
* Será necessário criar um ambiente virtual e preparalo com a instalação do requirements:
    ```
    $ pip install -r requirements.txt
    ```

#### Executando o sistema em seu localhost
* Crie seu banco de dados e execute os passos abaixo:
    * Necessário ter um database chamado 'localdb'
    ```
    $ export FLASK_APP=test-confitec/app.py
    ```
    ```
    $ flask run --host=0.0.0.0
    ```

#### Endpoints

* **Você porderá executar do Heroku ou local**

* Base endpoint:
    
        http://API-URL:5000/
        http://localhost:8000/
        http://127.0.0.1:8000/
    
* Endpoint de funcionarios:
    * listagem de todos os funcionarios:
        - $url-to-api/top_musicas/ - GET

        * params:{
            "artist": "str",
            "cache": "str" --opcional
        }

