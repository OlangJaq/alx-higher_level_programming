#!/usr/bin/python3
"""class rectangle that inherits from thw base class"""

from models.base import Base


class Rectangle(Base):
    """innitiate a rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor."""
        super().__init__(id)
        self.width = width        
        self.height = height
        self.x = x
        self.y = y