# Copyright (C) 2019 Sebastian Pipping <sebastian@pipping.org>
# Licensed under the MIT license

from itertools import chain as _chain, tee as _tee

_END_OF_STRING = object()

_MESSAGE_EARLY_STRING_END = ('Early string end: high surrogate U+{high:X} '
                             'not followed by a low surrogate')
_MESSAGE_LONE_HIGH_SURROGATE = ('High surrogate U+{high:X} not followed '
                                'by a low surrogate: found U+{second:X}')
_MESSAGE_LOW_SURROGATE_FIRST = ('Low surrogate U+{low:X} not preceded '
                                'by a high surrogate')
_MESSAGE_ASTRAL_CHARACTERS = 'Astral character U+{astral:X} not allowed'


class DecodeError(Exception):
    """
    Indicates an error during decoding of surrogate characters
    """
    pass


def _overlapping_pairs(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ... (s(N-1), sN), (sN, _EndOfString)"
    a, b = _tee(iterable)
    next(b, None)
    return zip(a, _chain(b, [_END_OF_STRING]))


def decode(s: str, reject_astral_characters=False) -> str:
    """
    Turns all surrogate pairs —
    a high surrogate (code points U+D800 to U+DBFF)
    followed by a low surrogate (code points U+DC00 to U+DFFF)
    – in string ``s`` into astral characters (code points U+10000 and bigger).

    May raise exception ``SurrogatesDecodeError`` on broken input.

    With ``reject_astral_characters=True`` any existing astral characters
    in ``s`` will be considered an error and raise ``SurrogatesDecodeError``
    to communicate this violation.

    For Python 3.4 and after ``surrogates.decode(s)`` is similar in effect to
    ``s.encode('utf-16', 'surrogatepass').decode('utf-16')``.
    """
    if not isinstance(s, str):
        raise TypeError('Not a string: {!r}'.format(s))

    decoded_s = []
    skip = False

    for first, second in _overlapping_pairs(s):
        if skip:
            skip = False
            continue

        if 0xD800 <= ord(first) <= 0xDBFF:
            if second is _END_OF_STRING:
                raise DecodeError(_MESSAGE_EARLY_STRING_END
                                  .format(high=ord(first)))

            if 0xDC00 <= ord(second) <= 0xDFFF:
                astral = (0x10000
                          + (ord(first) - 0xD800) * 0x400
                          + (ord(second) - 0xDC00))
                decoded_s.append(chr(astral))
                skip = True
            else:
                raise DecodeError(_MESSAGE_LONE_HIGH_SURROGATE
                                  .format(high=ord(first), second=ord(second)))
        elif 0xDC00 <= ord(first) <= 0xDFFF:
            raise DecodeError(_MESSAGE_LOW_SURROGATE_FIRST
                              .format(low=ord(first)))
        elif reject_astral_characters and ord(first) >= 0x10000:
            raise DecodeError(_MESSAGE_ASTRAL_CHARACTERS
                              .format(astral=ord(first)))
        else:
            decoded_s.append(first)

    return ''.join(decoded_s)


def encode(s: str) -> str:
    """
    Turns all astral characters (code points U+10000 and bigger)
    in string ``s`` into surrogate pairs:
    a high surrogate (code points U+D800 to U+DBFF)
    followed by a low surrogate (code points U+DC00 to U+DFFF).
    """
    if not isinstance(s, str):
        raise TypeError('Not a string: {!r}'.format(s))

    encoded_s = []

    for ch in s:
        if ord(ch) < 0x10000:
            encoded_s.append(ch)
        else:
            high_surrogate = ((ord(ch) - 0x10000) // 0x400) + 0xD800
            low_surrogate = ((ord(ch) - 0x10000) & (0x400 - 1)) + 0xDC00
            encoded_s.append(chr(high_surrogate) + chr(low_surrogate))

    return ''.join(encoded_s)
