import os
import openai
from pydantic import BaseModel
#para usar open AI necesitams unsar tokens el de organizacion y el key


class Document(BaseModel): #BASE model se usa para validar los datos
    prompt: str = ''






#definimos una funcion

def inference(prompt: str) -> list:
   openai.organization = 'org-1p947TFp3k0E8nXKLXDXy9QT '
   openai.api_key = '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'

   print('[PROCESANDO]'.center(40,'-'))

   completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": """Se una calculadora de factoriales que solo admite numeros, si texto manda Syntax error
       E.G: Los factoriales son
       -El facotorial de 5 es 120 , 
       """},
      {"role": "user", "content": prompt}
   ],
    temperature=0.2,
    max_tokens = 100
   )
   content = completion.choices[0].message.content #choice[0] arreglo de un solo elemento
   prompt_tokens = completion.usage.prompt_tokens
   completion_tokens = completion.usage.completion_tokens
   total_tokens = completion.usage.total_tokens
   print('[TERMINO DE PROCESAR]'.center(40,'-'))
   res = [content,total_tokens,prompt_tokens,completion_tokens]
   print(res)
   return [content,total_tokens,prompt_tokens,completion_tokens]




# convertidor a binario
def binario(prompt: str) -> list:
    openai.organization = 'org-1p947TFp3k0E8nXKLXDXy9QT '
    openai.api_key = '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'
    print('[PROCESANDO]'.center(40, '-'))

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Convertidor binario
        E.G: Matematica
        -El numero 28 en binario es 11100"""},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=100
    )
    content = completion.choices[0].message.content  # choice[0] arreglo de un solo elemento
    prompt_tokens = completion.usage.prompt_tokens
    completion_tokens = completion.usage.completion_tokens
    total_tokens = completion.usage.total_tokens
    print('[TERMINO DE PROCESAR]'.center(40, '-'))
    respuesta = [content, total_tokens, prompt_tokens, completion_tokens]
    print(respuesta)
    return respuesta



#rolplay es como quieres que se comporte
# temperatura cuanto divaga 0 nada 1 para arriba
#few shot: dar un cierto ejemplo

#genera la respuesta y la guarda en completion

