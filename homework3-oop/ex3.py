"""
    Create a class World.

    The representation of the World is a grid (matrix).

    public attributes:
        - map_height - int
        - map_width - int
        - world_map - Matrix[int] or List[List[int]]
            - you can represent this using numpy's matrix or just basic
            python list of lists of integers

    public methods:
        - init_world() - returns nothing
            - creates the matrix of size map_height X map_width and all the
            elements of the matrix are initially 0

        - see_world() - returns nothing
            - this PRETTY prints the current map

        - update world(world_entity) - returns nothing
            - this updates the world_map with the entity_id of the world_entity
            passed as a parameter
"""
import numpy as np
import pprint


class World():
    def __init__(self, map_height: int, map_width: int, world_map: list[list[int]]):
        self.map_height = map_height
        self.map_width = map_width
        self.world_map = world_map

    def init_world(self):
        """creates the matrix"""
        matrix = self.map_height * self.map_width
        return matrix

    def see_world(self):
        pprint(self.world_map)

    def world_entity(self):
        self.world_map +=
