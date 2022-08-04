from fastapi import FastAPI

app = FastAPI()


@app.get("/criacao_lead")
def home():
    return "MEU AMOR E MEU NENÉM, O PAPAI AMA MUITO VOCÊS"


"""def buscar_dados():
    request = requests.get("https://api.github.com/users/peeemax")
    print(request.json())

buscar_dados() """
