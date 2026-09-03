from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="AWS ECS Demo Dashboard")


@app.get("/", response_class=HTMLResponse)
def dashboard():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AWS ECS Demo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                text-align: center;
                padding: 50px;
            }

            .container {
                max-width: 900px;
                margin: auto;
            }

            h1 {
                color: #232f3e;
            }

            .subtitle {
                color: #666;
                margin-bottom: 30px;
            }

            .cards {
                display: flex;
                justify-content: center;
                gap: 20px;
                flex-wrap: wrap;
            }

            .card {
                background: white;
                width: 220px;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }

            .card h2 {
                margin: 10px 0;
            }

            .status {
                color: green;
                font-weight: bold;
            }

            .button {
                display: inline-block;
                margin-top: 30px;
                padding: 12px 25px;
                background: #ff9900;
                color: white;
                text-decoration: none;
                border-radius: 6px;
            }
        </style>
    </head>

    <body>

        <div class="container">

            <h1>🚀 AWS ECS Demo Application</h1>

            <p class="subtitle">
                FastAPI application running inside Docker
            </p>

            <div class="cards">

                <div class="card">
                    <h2>🐍 Python</h2>
                    <p>FastAPI Application</p>
                </div>

                <div class="card">
                    <h2>🐳 Docker</h2>
                    <p>Containerized</p>
                </div>

                <div class="card">
                    <h2>☁️ AWS</h2>
                    <p>ECS Fargate</p>
                </div>

                <div class="card">
                    <h2>✅ Status</h2>
                    <p class="status">Application Running</p>
                </div>

            </div>

            <a class="button" href="/docs">
                Open API Documentation
            </a>

        </div>

    </body>
    </html>
    """


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "AWS ECS Demo",
        "version": "1.0"
    }


@app.get("/add/{num1}/{num2}")
def add_numbers(num1: int, num2: int):
    return {
        "num1": num1,
        "num2": num2,
        "result": num1 + num2
    }

