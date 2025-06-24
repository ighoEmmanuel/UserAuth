from dataclasses import dataclass, field
from typing import Optional


@dataclass
class User:
    name: str
    email: str
    password: str
    id: Optional[str] = field(default=None, repr=False)

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
        }

