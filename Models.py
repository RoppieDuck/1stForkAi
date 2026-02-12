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
    description: str
    priority: str       # bijv. "laag", "medium", "hoog"
    status: str = "open"  # open, bezig, afgerond
    created_at: str = datetime.now().isoformat()
