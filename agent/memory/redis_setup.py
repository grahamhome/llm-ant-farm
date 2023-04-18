"""
Initial setup tasks for Redis DB.
"""
from redis.client import Redis
from redis.commands.search.field import VectorField, TextField


def create_flat_index(redis: Redis):
    redis.ft().create_index(fields=[
        VectorField("vector", "FLAT", {"TYPE": "FLOAT32", "DIM": 512, "DISTANCE_METRIC": "L2", "INITIAL_CAP": 10000, "BLOCK_SIZE": 10000}),
        TextField("")
    ])