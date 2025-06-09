from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

""" from fastapi import FastAPI

app= FastAPI()
 

@app.get("/")
async def read_root():
    return {"message":"Hola Sertech"}

@app.get("/items/{item_id}")
async def read_item(item_id:int,q :str=None):
    return {"item_id":item_id,"q":q} """

@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Docker App Sertech</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" />
        <style>
            body {
                background-color: #d7dbdd ;
                color: #495057;
            }
            .container {
                margin-top: 100px;
            }
            .custom-heading {
                font-size: 3rem;
                color: #007bff;
                font-weight: bold;
            }
            .highlight-text {
                color: #e74c3c;
                font-size: 1.5rem;
            }
            .btn-custom {
                background-color: #007bff;
                color: white;
                padding: 10px 20px;
                font-size: 1.2rem;
                font-weight: bold;
            }
            .lead {
            font-size: 1.25rem;
            color: #17202a;
            font-weight: bold;
            line-height: 1.6;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        </style>
    </head>
    <body>
        <div class="container text-center">
            <h1 class="custom-heading">¡Bienvenidos a DockerFastAPI Sertech!</h1>
            <h2 class="highlight-text">Mejorado listo para escalar</h2>
            <p class="lead">Hola a todos, como están, este es el lugar donde las aplicaciones modernas se encuentran con la eficiencia.</p>
            <p>Descubre más sobre el desarrollo de aplicaciones web en <a href="https://sertech.pe/back-office-app/" class="btn btn-info btn-custom">SERTECH</a></p>
        </div>
    </body>
    </html>
    """
    return html_content

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
