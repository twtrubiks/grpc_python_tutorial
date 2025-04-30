from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserRequest(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class Detail(_message.Message):
    __slots__ = ("id", "value")
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    id: int
    value: str
    def __init__(self, id: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...

class UserResponse(_message.Message):
    __slots__ = ("details",)
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    details: _containers.RepeatedCompositeFieldContainer[Detail]
    def __init__(self, details: _Optional[_Iterable[_Union[Detail, _Mapping]]] = ...) -> None: ...
