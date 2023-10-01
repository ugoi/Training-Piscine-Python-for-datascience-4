import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random 15-char lowercase ID."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Data representation of a student."""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False, default_factory=lambda: 'Eagle')
    id: str = field(init=False, default_factory=generate_id)
