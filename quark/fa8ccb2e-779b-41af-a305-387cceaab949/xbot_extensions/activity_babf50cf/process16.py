import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    if args is None:
        connection_pool = None
    else:
        connection_pool = args.get("connection_pool", None)
    try:
        invoke_result = xbot_visual.process.invoke_module(module="redis_client", package=__name__, function="redis_close", params={
            "connection_pool": connection_pool,
        }, _block=("关闭redis连接", 1, "调用模块"))
    finally:
        pass
