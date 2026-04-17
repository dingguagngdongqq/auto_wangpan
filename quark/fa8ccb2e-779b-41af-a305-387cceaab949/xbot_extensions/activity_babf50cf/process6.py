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
        field = ""
    else:
        connection_pool = args.get("connection_pool", None)
        key = args.get("key", "")
        field = args.get("field", "")
    try:
        value = xbot_visual.process.invoke_module(module="redis_client", package=__name__, function="hget", params={
            "connection_pool": connection_pool,
            "key": key,
            "field": field,
        }, _block=("hash_hget", 1, "调用模块"))
    finally:
        args["value"] = value
