from django.http import HttpResponse
from django.shortcuts import render

def SenacRJ_home(request):
    html = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SenacRJ - Home</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background: linear-gradient(135deg, #6e8efb, #a777e3);
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                color: white;
                text-align: center;
            }
            .container {
                background: rgba(0, 0, 0, 0.7);
                padding: 2rem;
                border-radius: 15px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
            }
            h1 {
                font-size: 2.5rem;
                margin-bottom: 1rem;
            }
            p {
                font-size: 1.2rem;
                margin-bottom: 2rem;
            }
            .btn {
                display: inline-block;
                padding: 10px 20px;
                background: #ff6b6b;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                transition: all 0.3s ease;
            }
            .btn:hover {
                background: #ff5252;
                transform: translateY(-3px);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌟 SenacRJ - Home🌟</h1>
            <p><a href="http://127.0.0.1:8000/contato" class="btn">Contato</a></p>
            <p><a href="http://127.0.0.1:8000/sobre" class="btn">Sobre</a></P>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

def SenacRJ_sobre(request):
    html = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SenacRJ - Sobre</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background: linear-gradient(135deg, #6e8efb, #a777e3);
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                color: white;
                text-align: center;
            }
            .container {
                background: rgba(0, 0, 0, 0.7);
                padding: 2rem;
                border-radius: 15px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
            }
            h1 {
                font-size: 2.5rem;
                margin-bottom: 1rem;
            }
            p {
                font-size: 1.2rem;
                margin-bottom: 2rem;
            }
            .btn {
                display: inline-block;
                padding: 10px 20px;
                background: #ff6b6b;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                transition: all 0.3s ease;
            }
            .btn:hover {
                background: #ff5252;
                transform: translateY(-3px);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌟 SenacRJ - Sobre🌟</h1>
            <p><a href="http://127.0.0.1:8000/" class="btn">Home</a></p>
            <p><a href="http://127.0.0.1:8000/contato" class="btn">Contato</a></P>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

def SenacRJ_contato(request):
    html = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SenacRJ - Contato</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background: linear-gradient(135deg, #6e8efb, #a777e3);
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                color: white;
                text-align: center;
            }
            .container {
                background: rgba(0, 0, 0, 0.7);
                padding: 2rem;
                border-radius: 15px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
            }
            h1 {
                font-size: 2.5rem;
                margin-bottom: 1rem;
            }
            p {
                font-size: 1.2rem;
                margin-bottom: 2rem;
            }
            .btn {
                display: inline-block;
                padding: 10px 20px;
                background: #ff6b6b;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                transition: all 0.3s ease;
            }
            .btn:hover {
                background: #ff5252;
                transform: translateY(-3px);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌟 SenacRJ - Contato🌟</h1>
            <p><a href="http://127.0.0.1:8000/" class="btn">Home</a></p>
            <p><a href="http://127.0.0.1:8000/sobre" class="btn">Sobre</a></P>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

