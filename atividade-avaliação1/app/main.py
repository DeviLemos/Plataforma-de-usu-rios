from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import app.schemas.database as database
import os

app = FastAPI(title="FastAPI Dashboard", version="0.1.0")

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Monta a pasta de arquivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# Banco de Dados

@app.on_event("startup")
def on_startup():
    database.connect_to_mongo()  # conecta ao Mongo

@app.on_event("shutdown")
def on_shutdown():
    database.close_mongo_connection()  # fecha conexão


# Schemas Pydantic

class NewUser(BaseModel):
    id: int
    name: str

class ModifyUser(BaseModel):
    id: int
    new_name: str

class RemoveUser(BaseModel):
    id: int


# Rotas


# Página inicial (HTML)
@app.get("/")
def dashboard():
    return FileResponse(os.path.join("app", "static", "dashboard.html"))

# Listar todos os usuários
@app.get("/users/all")
def list_users():
    cursor = database.db["usuarios"].find({}, {"_id": 0, "id": 1, "name": 1})
    users = list(cursor)
    return {"users": users}

# Buscar usuário por ID
@app.get("/users/find")
def find_user(user_id: int):
    user = database.db["usuarios"].find_one({"id": user_id}, {"_id": 0, "id": 1, "name": 1})
    if not user:
        return JSONResponse(content={"error": "User not found"}, status_code=404)
    return user

# Criar novo usuário
@app.post("/users/add")
def add_user(new_user: NewUser):
    database.db["usuarios"].insert_one(new_user.dict())
    return {"message": "User added successfully"}

# Atualizar usuário
@app.put("/users/update")
def update_user(mod_user: ModifyUser):
    result = database.db["usuarios"].update_one(
        {"id": mod_user.id}, {"$set": {"name": mod_user.new_name}}
    )
    if result.matched_count == 0:
        return JSONResponse(content={"error": "User not found"}, status_code=404)
    return {"message": "User updated successfully"}

# Deletar usuário
@app.delete("/users/remove")
def remove_user(del_user: RemoveUser):
    result = database.db["usuarios"].delete_one({"id": del_user.id})
    if result.deleted_count == 0:
        return JSONResponse(content={"error": "User not found"}, status_code=404)
    return {"message": "User removed successfully"}
