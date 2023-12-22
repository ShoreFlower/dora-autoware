#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from dora import Node

# node = Node()

# event = node.next()
# if event["type"] == "INPUT":
#     print(
#         f"""Node received:
#         id: {event["id"]},
#         value: {event["data"]},
#         metadata: {event["metadata"]}"""
#     )


from typing import Callable
from dora import DoraStatus
import pickle


class Operator:
    """
    反序列化后，输出各类消息内容
    """

    def __init__(self):
        pass
        
    def on_event(
        self,
        dora_event: dict,
        send_output: Callable[[str, bytes], None],
    ) -> DoraStatus:
        if dora_event["type"] == "INPUT":
            return self.on_input(dora_event, send_output)
        return DoraStatus.CONTINUE

    def on_input(
        self,
        dora_input: dict,
        send_output: Callable[[str, bytes], None],
    ):
        # print(dora_input["id"])
        if "Imu100D4" == dora_input["id"]:
            dora_input = dora_input["value"]
            # print(dora_input["value"])
            dora_input_bytes = bytes(dora_input.to_pylist())
            self.receDoraSentence = pickle.loads(dora_input_bytes)
            print(self.receDoraSentence)


        return DoraStatus.CONTINUE
