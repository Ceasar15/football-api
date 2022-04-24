from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from api.endpoints import endpoint
from users import api

app = FastAPI()
app.include_router(endpoint.router)
app.include_router(api.router)


@app.get("/", response_class=HTMLResponse)
def index():
    return """
<!Doctype html>
    <html>
        <body>
            <h1>Football API Leaderboard</h1>
            <div class="btn-group">
                <a href="/docs"><button>SwaggerUI</button></a>
                <a href="/redoc"><button>Redoc</button></a>
            </div>
        </body>
    </html>
"""
