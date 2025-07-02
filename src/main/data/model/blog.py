from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Blog:
    author_id: str
    title: str
    content: str
    id: Optional[str] = field(default=None, repr=False)

    def to_dict(self, include_id=True) :
        return {
            'author_id': self.author_id,
            'title': self.title,
            'content': self.content,
        }



