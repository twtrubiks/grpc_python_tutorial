# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: service_protos/user.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'service_protos/user.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19service_protos/user.proto\x12\x04user\"\'\n\x0bUserRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"#\n\x06\x44\x65tail\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t\"-\n\x0cUserResponse\x12\x1d\n\x07\x64\x65tails\x18\x01 \x03(\x0b\x32\x0c.user.Detail2<\n\x05Users\x12\x33\n\x08ListUser\x12\x11.user.UserRequest\x1a\x12.user.UserResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_protos.user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_USERREQUEST']._serialized_start=35
  _globals['_USERREQUEST']._serialized_end=74
  _globals['_DETAIL']._serialized_start=76
  _globals['_DETAIL']._serialized_end=111
  _globals['_USERRESPONSE']._serialized_start=113
  _globals['_USERRESPONSE']._serialized_end=158
  _globals['_USERS']._serialized_start=160
  _globals['_USERS']._serialized_end=220
# @@protoc_insertion_point(module_scope)
