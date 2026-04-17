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
        ], _block=("test", 1, "调用流程"))
        # 往集合里面添加成员
        # process.run
        # 在集合里面移除成员
        _ = xbot_visual.process.run(process="process11", package=__name__, inputs={
            "connection_pool": lambda: connection_pool.connection_pool,
            "key": "xztest",
            "value_list": lambda: ['"啊大阿松大大苏打"'],
            }, outputs=[
        ], _block=("test", 5, "调用流程"))
        process_result3 = xbot_visual.process.run(process="process12", package=__name__, inputs={
            "connection_pool": connection_pool.connection_pool,
            "key": "xztest",
            }, outputs=[
            "value",
        ], _block=("test", 6, "调用流程"))
        xbot_visual.programing.log(type="info", text=process_result3.value, _block=("test", 7, "打印日志"))
        # programing.log
        # programing.comment
        # process.run
        # programing.log
        _ = xbot_visual.process.run(process="process16", package=__name__, inputs={
            "connection_pool": connection_pool.connection_pool,
            }, outputs=[
        ], _block=("test", 12, "调用流程"))
    finally:
        pass
