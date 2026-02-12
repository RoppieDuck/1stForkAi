from dataclasses import dataclass
from datetime import datetime

@dataclass
class Project:
    name: str
    created_at: str = datetime.now().isoformat()

@dataclass
class Task:
    id: int
    project: str
    title: str
    done: bool = False
    created_at: str = datetime.now().isoformat()