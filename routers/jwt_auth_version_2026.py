from datetime import datetime, timedelta, timezone
from typing import Annotated
import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from pydantic import BaseModel

ALGORITMO = "HS256"
TOKEN = 1
SECRET = "201d573bd7d1344d3a3bfce1550b69102fd11be3db6d379508b6cccc58ea230b"
crypt_context = CryptContext(schemes=["bcrypt"])
DUMMY_HASH = "$2a$12$dummyhashhere"

app = FastAPI()


oauth = OAuth2PasswordBearer(tokenUrl="login")

class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    hashed_password: str

users_db = {
    "mouredev": {
        "username": "mouredev",
        "full_name": "Brais Moure",
        "email": "braismoure@mouredev.com",
        "disabled": False,
        "hashed_password": "$2a$12$B2Gq.Dps1WYf2t57eiIKjO4DXC3IUMUXISJF62bSRiFfqMdOI2Xa6"
    },
    "mouredev2": {
        "username": "mouredev2",
        "full_name": "Brais Moure 2",
        "email": "braismoure2@mouredev.com",
        "disabled": True,
        "hashed_password": "$2a$12$SduE7dE.i3/ygwd0Kol8bOFvEABaoOOlC8JsCSr6wpwB4zl5STU4S"
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def verify_password(plain_password, hashed_password):
    return crypt_context.verify(plain_password, hashed_password)

def search_user(db, username: str):
    if username in db:
        user_dict = db[username].copy()
        user_dict.pop("hashed_password", None)
        return User(**user_dict)

############# doc ##################
def authenticate_user(username: str, password: str):
    user = search_user_db(username)
    if not user:
        verify_password(password, DUMMY_HASH)
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET, algorithm=ALGORITMO)
    return encoded_jwt
####################################


async def auth_user(token: str = Depends(oauth)):

    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación inválidas",
        headers={"WWW-Authenticate": "Bearer"})

    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITMO]).get("sub")
        if username is None:
            raise exception

    except:
        raise exception

    return search_user(users_db, username)


async def current_user(current_user: Annotated[User, Depends(auth_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/login")
async def login(form: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException( status_code=404, detail="Usuario no encontrado")

    user = authenticate_user(form.username, form.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=TOKEN)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@app.get("/users/me")
async def me(user: Annotated[User, Depends(current_user)]):
    return user