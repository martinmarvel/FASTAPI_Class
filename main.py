
from fastapi import FastAPI
app = FastAPI()

#fast api instance ı oluışturduk
#uvicorn main:app --reload virtual server başlttık fast api özelliği

@app.get("/")#burakadi "@" bir dekaratör, altında yazılan kodu fastapi ile ilişkilendirmeye yarar, "get" http metodu, "/" root path denir, 
#path değişebilir örneğin "/login" url de login path inde işlemler yapmamıza yarar
async def root():#fonks. ismi önemli değil 
    return {"message": "Hello Ömer1 World"}#buradaki data jsona dönüştürülüyor

@app.get("/posts")
def getPosts():
    return {"data":"yeni data"}