from typing import Union

from fastapi import FastAPI

app = FastAPI()
from uce.ai.openaitest import Document
from uce.ai.openaitest import *


@app.get("/",status_code=200)
def read_root():
    return {"Hello": "World"}

#generamos un ENDPOINT de tipo post para enviar informacion en el cuerpo de la peticion

@app.post('/inference',status_code=200) #si funciona retorna el codigo 200
def inference_endpoint(doc: Document):
    response = inference(doc.prompt)
    return {
        'inference':response[0],
        'usage_total':response[1],
        'usage_pront':response[2],
        'usage_completion':response[3]
    }

@app.post('/binario',status_code=200)
def binary_endpoint(doc: Document):
    response= binario(doc.prompt)
    return {
        'inference': response[0],
        'usage_total': response[1],
        'usage_pront': response[2],
        'usage_completion': response[3]
    }


@app.post('/factorial',status_code=200)
def factorial_endpoint(doc: Document):
    response= inference(doc.prompt)
    return {
        'inference': response[0],
        'usage_total': response[1],
        'usage_pront': response[2],
        'usage_completion': response[3]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9043)


#--reload hace que los cambios de actulicen automaticamente


#cambiamos el puerto (si tenemos ese puerto con otros servicios)

#if __name__ == '__main__':
   # app.host()

