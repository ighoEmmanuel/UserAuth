from dataclasses import dataclass, field
from typing import Optional, List

from model.blog import Blog


@dataclass
class User:
    name: str
    email: str
    password: str
    blogs: List[str] = field(default_factory=list)
    id: Optional[str] = field(default=None, repr=False)


    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "blogs": self.blogs,
        }

