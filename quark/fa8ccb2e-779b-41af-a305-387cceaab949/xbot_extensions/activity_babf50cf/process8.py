import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    values_dict = {}
    if args is None:
        connection_pool = None
        key = ""
    else:
        connection_pool = args.get("connection_pool", None)
        key = args.get("key", "")
    try:
        values_dict = xbot_visual.process.invoke_module(module="redis_client", package=__name__, function="hgetall", params={
            "connection_pool": connection_pool,
            "key": key,
        }, _block=("hash_hgetall", 1, "调用模块"))
    finally:
        args["values_dict"] = values_dict
