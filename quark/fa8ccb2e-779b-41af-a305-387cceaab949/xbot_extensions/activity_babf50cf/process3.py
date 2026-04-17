import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    if args is None:
        connection_pool = None
        key = ""
        value = ""
    else:
        connection_pool = args.get("connection_pool", None)
        key = args.get("key", "")
        value = args.get("value", "")
    try:
        invoke_result = xbot_visual.process.invoke_module(module="redis_client", package=__name__, function="set", params={
            "connection_pool": connection_pool,
            "key": key,
            "value": value,
        }, _block=("string_set", 1, "调用模块"))
    finally:
        pass
