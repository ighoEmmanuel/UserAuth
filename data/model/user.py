from dataclasses import dataclass, field
from typing import Optional, List

from bson import ObjectId


@dataclass
class User:
    name: str
    email: str
    password: str
    blogs: List[ObjectId] = field(default_factory=list)
    id: Optional[str] = field(default=None, repr=False)


    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "blogs": self.blogs,
        }

