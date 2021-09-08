"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import pyatv.protocols.mrp.protobuf.NowPlayingClient_pb2
import pyatv.protocols.mrp.protobuf.NowPlayingPlayer_pb2
import pyatv.protocols.mrp.protobuf.Origin_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class PlayerPath(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ORIGIN_FIELD_NUMBER: builtins.int
    CLIENT_FIELD_NUMBER: builtins.int
    PLAYER_FIELD_NUMBER: builtins.int
    @property
    def origin(self) -> pyatv.protocols.mrp.protobuf.Origin_pb2.Origin: ...
    @property
    def client(self) -> pyatv.protocols.mrp.protobuf.NowPlayingClient_pb2.NowPlayingClient: ...
    @property
    def player(self) -> pyatv.protocols.mrp.protobuf.NowPlayingPlayer_pb2.NowPlayingPlayer: ...
    def __init__(self,
        *,
        origin : typing.Optional[pyatv.protocols.mrp.protobuf.Origin_pb2.Origin] = ...,
        client : typing.Optional[pyatv.protocols.mrp.protobuf.NowPlayingClient_pb2.NowPlayingClient] = ...,
        player : typing.Optional[pyatv.protocols.mrp.protobuf.NowPlayingPlayer_pb2.NowPlayingPlayer] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"client",b"client",u"origin",b"origin",u"player",b"player"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"client",b"client",u"origin",b"origin",u"player",b"player"]) -> None: ...
global___PlayerPath = PlayerPath