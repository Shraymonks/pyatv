"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.extension_dict
import google.protobuf.message
import pyatv.protocols.mrp.protobuf.CommandInfo_pb2
import pyatv.protocols.mrp.protobuf.CommandOptions_pb2
import pyatv.protocols.mrp.protobuf.PlayerPath_pb2
import pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class SendCommandMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    COMMAND_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    PLAYERPATH_FIELD_NUMBER: builtins.int
    command: pyatv.protocols.mrp.protobuf.CommandInfo_pb2.Command.V = ...
    @property
    def options(self) -> pyatv.protocols.mrp.protobuf.CommandOptions_pb2.CommandOptions: ...
    @property
    def playerPath(self) -> pyatv.protocols.mrp.protobuf.PlayerPath_pb2.PlayerPath: ...
    def __init__(self,
        *,
        command : typing.Optional[pyatv.protocols.mrp.protobuf.CommandInfo_pb2.Command.V] = ...,
        options : typing.Optional[pyatv.protocols.mrp.protobuf.CommandOptions_pb2.CommandOptions] = ...,
        playerPath : typing.Optional[pyatv.protocols.mrp.protobuf.PlayerPath_pb2.PlayerPath] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"command",b"command",u"options",b"options",u"playerPath",b"playerPath"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"command",b"command",u"options",b"options",u"playerPath",b"playerPath"]) -> None: ...
global___SendCommandMessage = SendCommandMessage

sendCommandMessage: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2.ProtocolMessage, global___SendCommandMessage] = ...