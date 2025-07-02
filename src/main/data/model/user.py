from dataclasses import dataclass, field
from typing import Optional, List

from bson import ObjectId


@dataclass
class User:
    name: str
    email: str
    password: str
    blogs: List[str] = field(default_factory=list)
    id: Optional[str] = field(default=None, repr=False)

    def to_dict(self, include_id=True):
        data = {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "blogs": self.blogs
        }
        if include_id and self.id:
            data["_id"] = ObjectId(self.id)
        return data

