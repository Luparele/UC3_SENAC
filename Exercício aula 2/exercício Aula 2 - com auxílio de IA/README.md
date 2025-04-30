# Calculadora Web com Python (Flask), HTML e CSS

Este projeto consiste em uma calculadora web desenvolvida utilizando Python com o framework Flask para a lógica do servidor e HTML e CSS para a interface do usuário.

## Como executar:

1.  **Instale o Flask:** Se você ainda não tem, abra seu terminal e execute:
    ```bash
    pip install Flask
    ```
2.  **Crie as pastas:** Crie uma pasta principal para o seu projeto. Dentro dela, crie duas subpastas: `templates` e `static`.
3.  **Salve os arquivos:**
    * Salve o código Python como `calculadora.py` na pasta principal.
    * Salve o código HTML como `calculadora.html` dentro da pasta `templates`.
    * Salve o código CSS como `style.css` dentro da pasta `static`.
4.  **Execute o servidor Flask:** Abra seu terminal na pasta principal do projeto e execute:
    ```bash
    python calculadora.py
    ```
5.  **Abra no navegador:** Abra seu navegador web e vá para o endereço `http://127.0.0.1:5000/`. Você deverá ver a interface da calculadora.

## Explicação:

* **HTML (`calculadora.html`):** A estrutura da página com os botões e o display. As funções `onclick` nos botões usam `fetch` para enviar requisições `POST` para o servidor Flask.
* **CSS (`static/style.css`):** O estilo visual da calculadora.
* **Python (`calculadora.py`):**
    * Importa as bibliotecas necessárias (Flask para o servidor web, `render_template` para servir o HTML, `request` para acessar os dados da requisição, `jsonify` para enviar respostas em JSON, e `math` para as funções matemáticas).
    * Cria uma instância do Flask.
    * A função `calcular` contém a lógica da sua calculadora original.
    * A rota `/` (método `GET`) renderiza o arquivo `calculadora.html`.
    * A rota `/calcular` (método `POST`) recebe os dados da operação e dos números via `request.form`, chama a função `calcular` e retorna o resultado em formato JSON.
* **JavaScript (inline no HTML):** Pequenos trechos de JavaScript são usados para:
    * Manipular a entrada no display do lado do cliente (para feedback imediato).
    * Enviar os dados (operação e números) para o servidor Flask usando a API `fetch`.
    * Receber a resposta do servidor (o resultado do cálculo ou um erro) e atualizar o display.