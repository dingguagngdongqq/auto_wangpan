import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    value = ""
    if args is None:
        connection_pool = None
        key = ""
    else:
        connection_pool = args.get("connection_pool", None)
        key = args.get("key", "")
    try:
        value = xbot_visual.process.invoke_module(module="redis_client", package=__name__, function="get", params={
            "connection_pool": connection_pool,
            "key": key,
        }, _block=("string_get", 1, "调用模块"))
    finally:
        args["value"] = value
