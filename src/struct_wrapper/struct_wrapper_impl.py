import struct


class BaseType:
    __slots__ = ["layout", "size"]
    layout: struct.Struct
    size: int

    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.size = cls.layout.size

    @classmethod
    def frombytes(cls, data: bytes):
        return cls.layout.unpack(data)[0]

    @classmethod
    def tobytes(cls, value) -> bytes:
        return cls.layout.pack(value)


class I8(BaseType):
    layout = struct.Struct("b")


class U8(BaseType):
    layout = struct.Struct("B")


class I16(BaseType):
    layout = struct.Struct("h")


class U16(BaseType):
    layout = struct.Struct("H")


class I32(BaseType):
    layout = struct.Struct("i")


class U32(BaseType):
    layout = struct.Struct("I")


class I64(BaseType):
    layout = struct.Struct("q")


class U64(BaseType):
    layout = struct.Struct("Q")


class F32(BaseType):
    layout = struct.Struct("f")


class F64(BaseType):
    layout = struct.Struct("d")


class I16BE(BaseType):
    layout = struct.Struct(">h")


class U16BE(BaseType):
    layout = struct.Struct(">H")


class I32BE(BaseType):
    layout = struct.Struct(">i")


class U32BE(BaseType):
    layout = struct.Struct(">I")


class I64BE(BaseType):
    layout = struct.Struct(">q")


class U64BE(BaseType):
    layout = struct.Struct(">Q")


class F32BE(BaseType):
    layout = struct.Struct(">f")


class F64BE(BaseType):
    layout = struct.Struct(">d")


class I16LE(BaseType):
    layout = struct.Struct("<h")


class U16LE(BaseType):
    layout = struct.Struct("<H")


class I32LE(BaseType):
    layout = struct.Struct("<i")


class U32LE(BaseType):
    layout = struct.Struct("<I")


class I64LE(BaseType):
    layout = struct.Struct("<q")


class U64LE(BaseType):
    layout = struct.Struct("<Q")


class F32LE(BaseType):
    layout = struct.Struct("<f")


class F64LE(BaseType):
    layout = struct.Struct("<d")
