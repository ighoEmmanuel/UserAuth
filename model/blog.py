from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Blog:
    author_id:str
    title: str
    id: Optional[str] = field(default=None, repr=False)
