import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    if args is None:
        connection_pool = None
        key = ""
        time = 0
    else:
        connection_pool = args.get("connection_pool", None)
        key = args.get("key", "")
        time = args.get("time", 0)
    try:
        invoke_result = xbot_visual.process.invoke_module(module="redis_client", package=__name__, function="key_expire", params={
            "connection_pool": connection_pool,
            "key": key,
            "time": time,
        }, _block=("key_expire", 1, "调用模块"))
    finally:
        pass
