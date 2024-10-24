from fastapi import FastAPI
import json
app = FastAPI()


with open('doughnuts.json', 'r') as file:
    data = json.load(file)

@app.get("/")
async def healthcheck():
    return {"message": "Server is Running"}

@app.get("/api/doughnuts/info")
async def info_doughnuts(max_calories:int = 99999,allow_nuts:bool = True):
    if allow_nuts == True:
        return_data = [d for d in data["doughnut_data"] if d["calories"] < max_calories]
    else:
        return_data = [d for d in data["doughnut_data"] if d["calories"] < max_calories and d["contains_nuts"] == False] 
    return {"doughnut_data":return_data}
    

