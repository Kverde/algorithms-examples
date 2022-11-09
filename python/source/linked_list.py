
from dataclasses import dataclass

from __future__ import annotations


@dataclass
class Node:
    data: str
    next: Node


class LinkedList:
    def __init__(self) -> None:
        self.list: Node = None
