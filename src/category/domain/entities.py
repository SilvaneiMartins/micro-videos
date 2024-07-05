from datetime import datetime
from unittest import TestCase


class Category:

    def __init__(self, name: str, descrition: str, is_active: bool, created_at: datetime) -> None:
        self.name = name
        self.descrition = descrition
        self.is_active = is_active
        self.created_at = created_at
