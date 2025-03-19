import os 
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_familia():
    rows = ["isaac", "gaviria", "mierti"]
    return rows 

@app.get("/superheoresDC")
def get_superheroe():
    rows = ["batman", "superman, flash"]
    return rows

