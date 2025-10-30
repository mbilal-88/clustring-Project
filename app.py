# from pydantic import BaseModel

# class User(BaseModel):
#     name:str
#     age:int

# def hello(input:User):
#     return f"Hello {input.name} with age of {input.age}"

# # m = User(
# #     name = "Bilal",
# #     age = 18
# # )  

# # m = {
# #     "name":"Bilal",
# #     "age": 24
# # }

# # print(hello(m))


# #==================

# # Api End point

# from fastapi import FastAPI

# #app

# app = FastAPI()

# # Endpoint(Get/Post)

# @app.post("/get_info")
# def hello(input:User):
#     return f"Hello {input.name} with age of {input.age}"

from predict import prediction
from fastapi import FastAPI

from pydantic import BaseModel
class CustomerInput(BaseModel):
    Genre: str
    Age: int
    Annual_Income: int
    Spending_Score: int

def hello(input:CustomerInput):
    return f"Gender {input.Genre} age is {input.Age} and your Annual Income {input.Annual_Income} and Spending Score is {input.Spending_Score}"


app = FastAPI()

@app.post("/get_info")
def hello(input:CustomerInput):
    # data = ["Male", 24, 100000, 80]
    data = [input.Genre,input.Age,input.Annual_Income,input.Spending_Score]
    output = prediction(data)
    return {"output": int(output[0])}