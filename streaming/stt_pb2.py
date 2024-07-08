# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streaming/stt.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x13streaming/stt.proto\x12\x03stt\x1a\x1bgoogle/protobuf/empty.proto"\xad\x02\n\x10StreamingOptions\x12\x17\n\nsession_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x0bsample_rate\x18\x02 \x01(\x05\x12\x30\n\x08\x65ncoding\x18\x03 \x01(\x0e\x32\x1e.stt.StreamingOptions.Encoding\x12/\n\x05model\x18\x04 \x01(\x0e\x32\x1b.stt.StreamingOptions.ModelH\x01\x88\x01\x01\x12\x12\n\nauth_token\x18\x05 \x01(\t\x12\x10\n\x03tag\x18\x06 \x01(\tH\x02\x88\x01\x01"\x18\n\x08\x45ncoding\x12\x0c\n\x08LINEAR16\x10\x00"\'\n\x05Model\x12\x0e\n\nRU_GENERAL\x10\x00\x12\x0e\n\nUZ_GENERAL\x10\x01\x42\r\n\x0b_session_idB\x08\n\x06_modelB\x06\n\x04_tag"\xad\x01\n\x10StreamingRequest\x12(\n\x04type\x18\x01 \x01(\x0e\x32\x1a.stt.StreamingRequest.Type\x12(\n\x07options\x18\x02 \x01(\x0b\x32\x15.stt.StreamingOptionsH\x00\x12\x0f\n\x05\x63hunk\x18\x03 \x01(\x0cH\x00")\n\x04Type\x12\r\n\tSTREAMING\x10\x00\x12\x08\n\x04STOP\x10\x01\x12\x08\n\x04\x41UTH\x10\x02\x42\t\n\x07payload"V\n\x12TranscriptionWords\x12\r\n\x05start\x18\x01 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x05\x12\x0c\n\x04word\x18\x03 \x01(\t\x12\x0f\n\x02id\x18\x04 \x01(\tH\x00\x88\x01\x01\x42\x05\n\x03_id"#\n\x05Range\x12\r\n\x05start\x18\x01 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x05"\xcf\x01\n\x11StreamingResponse\x12-\n\x06status\x18\x01 \x01(\x0e\x32\x1d.stt.StreamingResponse.Status\x12\x12\n\nsession_id\x18\x02 \x01(\t\x12\x1d\n\x06result\x18\x03 \x01(\x0b\x32\x0b.stt.ResultH\x00\x12\x1b\n\x05\x65rror\x18\x04 \x01(\x0b\x32\n.stt.ErrorH\x00"/\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\x12\n\x0e\x45ND_OF_SESSION\x10\x02\x42\n\n\x08response"\xd3\x01\n\x06Result\x12(\n\x07offsets\x18\x01 \x03(\x0b\x32\x17.stt.TranscriptionWords\x12\x32\n\x11temporary_offsets\x18\x02 \x03(\x0b\x32\x17.stt.TranscriptionWords\x12\x1c\n\x14total_audio_duration\x18\x03 \x01(\x05\x12 \n\x07\x63ursors\x18\x04 \x01(\x0b\x32\n.stt.RangeH\x00\x88\x01\x01\x12\x1f\n\x17\x65nding_silence_duration\x18\x05 \x01(\x05\x42\n\n\x08_cursors"\xa9\x02\n\x05\x45rror\x12"\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x14.stt.Error.ErrorCode\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x14\n\x07\x64\x65tails\x18\x03 \x01(\tH\x00\x88\x01\x01"\xc8\x01\n\tErrorCode\x12\x11\n\rUNKNOWN_ERROR\x10\x00\x12\x19\n\x15SERVICE_NOT_AVAILABLE\x10\x01\x12\x15\n\x11TOO_MANY_CHANNELS\x10\x02\x12\x1a\n\x16\x41UTHENTICATION_FAILURE\x10\x03\x12\x14\n\x10INVALID_ARGUMENT\x10\x04\x12\x14\n\x10PAYMENT_REQUIRED\x10\x05\x12\x14\n\x10TOO_LONG_SESSION\x10\x06\x12\x18\n\x14\x41UDIO_SIZE_TOO_LARGE\x10\x07\x42\n\n\x08_details2U\n\nRecognizer\x12G\n\x12RecognizeStreaming\x12\x15.stt.StreamingRequest\x1a\x16.stt.StreamingResponse(\x01\x30\x01\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "streaming.stt_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals["_STREAMINGOPTIONS"]._serialized_start = 58
    _globals["_STREAMINGOPTIONS"]._serialized_end = 359
    _globals["_STREAMINGOPTIONS_ENCODING"]._serialized_start = 261
    _globals["_STREAMINGOPTIONS_ENCODING"]._serialized_end = 285
    _globals["_STREAMINGOPTIONS_MODEL"]._serialized_start = 287
    _globals["_STREAMINGOPTIONS_MODEL"]._serialized_end = 326
    _globals["_STREAMINGREQUEST"]._serialized_start = 362
    _globals["_STREAMINGREQUEST"]._serialized_end = 535
    _globals["_STREAMINGREQUEST_TYPE"]._serialized_start = 483
    _globals["_STREAMINGREQUEST_TYPE"]._serialized_end = 524
    _globals["_TRANSCRIPTIONWORDS"]._serialized_start = 537
    _globals["_TRANSCRIPTIONWORDS"]._serialized_end = 623
    _globals["_RANGE"]._serialized_start = 625
    _globals["_RANGE"]._serialized_end = 660
    _globals["_STREAMINGRESPONSE"]._serialized_start = 663
    _globals["_STREAMINGRESPONSE"]._serialized_end = 870
    _globals["_STREAMINGRESPONSE_STATUS"]._serialized_start = 811
    _globals["_STREAMINGRESPONSE_STATUS"]._serialized_end = 858
    _globals["_RESULT"]._serialized_start = 873
    _globals["_RESULT"]._serialized_end = 1084
    _globals["_ERROR"]._serialized_start = 1087
    _globals["_ERROR"]._serialized_end = 1384
    _globals["_ERROR_ERRORCODE"]._serialized_start = 1172
    _globals["_ERROR_ERRORCODE"]._serialized_end = 1372
    _globals["_RECOGNIZER"]._serialized_start = 1386
    _globals["_RECOGNIZER"]._serialized_end = 1471
# @@protoc_insertion_point(module_scope)
