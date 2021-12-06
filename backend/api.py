from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import quests

app = FastAPI()

# CORS
app.add_middleware(CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/quests/{count}")
def read_item(count: int):
    return quests.get_full_quests(count)


@app.get("/quest/{quest}")
def read_item(quest: str):
    return {quests.read_quest(quest)}


@app.get("/done/{quest}")
def read_item(quest: str):
    quests.mark_as_done(quest)
    quests.escalate_quests()

@app.get("/escalate/{quest}")
def read_item(quest: str):
    quests.escalate_add(quest)

@app.get("/advance/{count}")
def read_item(count: int):
    quests.escalate_quests()
    return quests.get_full_quests(count) 
