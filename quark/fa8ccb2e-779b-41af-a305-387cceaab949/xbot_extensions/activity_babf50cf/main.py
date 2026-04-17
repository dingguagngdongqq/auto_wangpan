import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    try:
        connection_pool = xbot_visual.process.run(process="process2", package=__name__, inputs={
            "host": "127.0.0.1",
            "port": "6379",
            "password": "",
            "db": lambda: 0,
            }, outputs=[
            "connection_pool",
        ], _block=("main", 1, "调用流程"))
        _ = xbot_visual.process.run(process="process5", package=__name__, inputs={
            "connection_pool": lambda: connection_pool.connection_pool,
            "key": lambda: 'hash_names',
            "field": lambda: 'zhangsan',
            "value": lambda: 'hello redis hash',
            }, outputs=[
        ], _block=("main", 2, "调用流程"))
        _ = xbot_visual.process.run(process="process16", package=__name__, inputs={
            "connection_pool": connection_pool.connection_pool,
            }, outputs=[
        ], _block=("main", 3, "调用流程"))
    finally:
        pass
