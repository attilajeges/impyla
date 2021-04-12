#
# Autogenerated by Thrift Compiler (0.11.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class fb_status(object):
    """
    Common status reporting mechanism across all services
    """
    DEAD = 0
    STARTING = 1
    ALIVE = 2
    STOPPING = 3
    STOPPED = 4
    WARNING = 5

    _VALUES_TO_NAMES = {
        0: "DEAD",
        1: "STARTING",
        2: "ALIVE",
        3: "STOPPING",
        4: "STOPPED",
        5: "WARNING",
    }

    _NAMES_TO_VALUES = {
        "DEAD": 0,
        "STARTING": 1,
        "ALIVE": 2,
        "STOPPING": 3,
        "STOPPED": 4,
        "WARNING": 5,
    }
fix_spec(all_structs)
del all_structs
