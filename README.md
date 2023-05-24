# Documentação da API
## Introdução

Neste trabalho, foi desenvolvida uma API utilizando o framework Django em Python. A API permite o cadastro, listagem, edição e exclusão de dados, seguindo o padrão REST. Utilizou-se o formato JSON para a comunicação de dados e também foram aplicados os conceitos de migrations, utilizando um ORM (Object-Relational Mapping).
Instalação e Configuração

Para executar o projeto, siga as instruções abaixo:

    Clone o repositório do projeto: https://github.com/yurecouto/projetoIntegradorVa
    Certifique-se de ter o Python 3.x instalado em seu sistema.
    Crie um ambiente virtual para isolar as dependências do projeto.
    Ative o ambiente virtual.
    Instale as dependências do projeto: pip install -r requirements.txt
    Execute as migrações para criar o banco de dados: python manage.py migrate
    Crie um superusuário para acessar a interface administrativa: python manage.py createsuperuser
    Inicie o servidor local: python manage.py runserver
    Acesse a interface navegável do Django Admin em seu navegador: http://127.0.0.1:8000/admin
    
    Todos os endpoints estao mapeados no arquivo "projetoIntegradorVa.json",
    este arquivo e um arquivo de configuração do Postman, ferramenta para testes http.

## Endpoints da API
A seguir estão os endpoints disponíveis na API:

### Registrar aluno: 
Rota: POST http://127.0.0.1:8000/alunos/

```json
    // Dados da requisição
    {
        "nome": "Anakin Skywalker",
        "sexo": "Masculino",
        "matricula": "00000001",
        "data_nascimento": "1999-12-31"
    }

    // Resposta da API
    {
        "id": 1,
        "nome": "Anakin Skywalker",
        "sexo": "Masculino",
        "matricula": "00000001",
        "data_nascimento": "1999-12-31"
    }
```

### Consultar aluno: 
Rota: GET http://127.0.0.1:8000/alunos/<int:aluno_id>/

```json
    // Resposta da API
    {
        "id": 1,
        "nome": "Anakin Skywalker",
        "sexo": "Masculino",
        "matricula": "00000001",
        "data_nascimento": "1999-12-31"
    }
```

### Alterar matricula: 
Rota: UPDATE http://127.0.0.1:8000/alunos/<int:aluno_id>/

```json
    // Dados da requisição
    {
        "matricula": "99999999",
    }

    // Resposta da API
    {
        "id": 1,
        "nome": "Anakin Skywalker",
        "sexo": "Masculino",
        "matricula": "99999999",
        "data_nascimento": "1999-12-31"
    }
```

### Excluir aluno: 
Rota: DELETE http://127.0.0.1:8000/alunos/<int:aluno_id>/

### Listar turmas:
Rota: GET http://127.0.0.1:8000/turmas/

```json
    // Resposta da API 
    [
        {
            "id": 1,
            "codigo": "00000001",
            "codigo_curso": "12345678"
        },
        {
            "id": 2,
            "codigo": "00000002",
            "codigo_curso": "12345678"
        },
        {
            "id": 3,
            "codigo": "00000003",
            "codigo_curso": "12345678"
        },
        {
            "id": 4,
            "codigo": "00000004",
            "codigo_curso": "12345678"
        }
    ]
```

### Listar alunos da turma: 
Rota: GET http://127.0.0.1:8000/turmas/<int:turma_id>/alunos/

```json
    // Resposta da API
    [
        {
            "id": 2,
            "nome": "Anakin Skywalker",
            "sexo": "Masculino",
            "matricula": "00000001",
            "data_nascimento": "1999-12-31"
        }
    ]
```

### Consultar curso: 
Rota: GET http://127.0.0.1:8000/cursos/<int:curso_id>/

```json
    // Resposta da API
    {
        "id": 1,
        "nome": "Engenharia",
        "codigo": "12345678"
    }
```

### Incluir curso: 
Rota: POST http://127.0.0.1:8000/cursos/

```json
    // Dados da requisição
    {
        "nome": "Engenharia",
        "codigo": "12345678"
    }

    // Resposta da API
    {
        "id": 1,
        "nome": "Engenharia",
        "codigo": "12345678"
    }
```

### Consultar disciplina: 
Rota: GET http://127.0.0.1:8000/disciplinas/<int:disciplina_id>/

```json
    // Resposta da API
    {
        "id": 1,
        "nome": "Matematica",
        "codigo": "42305716"
    }
```

### Incluir disciplina: 
Rota: POST http://127.0.0.1:8000/disciplinas/

```json
    // Dados da requisição
    {
        "nome": "Matematica",
        "codigo": "42305716"
    }

    // Resposta da API
    {
        "id": 1,
        "nome": "Matematica",
        "codigo": "42305716"
    }
```

### Consultar turma: 
Rota: GET http://127.0.0.1:8000/turmas/<int:turma_id>/

### Lancar nota do aluno: 
Rota: POST http://127.0.0.1:8000/notasaluno/

```json
    // Dados da requisição
    {
        "codigo_aluno": "99999999",
        "nota": 8,
        "avaliacao": "va1",
        "disciplina": 1,
        "data": "2022-12-22"
    }

    // Resposta da API
    {
        "id": 1,
        "nota": 8,
        "avaliacao": "va1",
        "data": "2022-12-22",
        "codigo_aluno": "00000001",
        "disciplina": 1
    }
```

### Realizar frequencia: 
Rota: POST http://127.0.0.1:8000/notasaluno/

```json
    // Dados da requisição
    {
        "codigo_aluno": "00000001",
        "codigo_professor": "12345678",
        "codigo_turma": "00000001",
        "data": "2022-12-22"
    }

    // Resposta da API
    {
        "id": 1,
        "data": "2022-12-22",
        "codigo_aluno": "00000001",
        "codigo_professor": "12345678",
        "codigo_turma": "00000001"
    }
```
