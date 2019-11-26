# Copyright (C) 2019 Sebastian Pipping <sebastian@pipping.org>
# Licensed under the MIT license

from unittest import TestCase

import surrogates
from parameterized import parameterized


class CodecTest(TestCase):
    @parameterized.expand([
        ('bmp only', 'hello', 'hello'),
        ('pile of poo', chr(0x1f4a9), chr(0xD83D) + chr(0xDCA9)),
        ('face throwing a kiss', chr(0x1F618), chr(0xD83D) + chr(0xDE18)),
    ])
    def test_valid(self, _label, expected_decoded, expected_encoded):
        actual_encoded = surrogates.encode(expected_decoded)
        self.assertEqual(actual_encoded, expected_encoded)

        actual_decoded = surrogates.decode(expected_encoded)
        self.assertEqual(actual_decoded, expected_decoded)


class EncoderTest(TestCase):
    @parameterized.expand([
        ('none', None, TypeError, 'Not a string: None'),
    ])
    def test_invalid(self, _label, decoded, expected_exception,
                     expected_message):
        with self.assertRaises(expected_exception) as catcher:
            surrogates.encode(decoded)

        self.assertEqual(str(catcher.exception), expected_message)


class DecoderTest(TestCase):
    @parameterized.expand([
        ('none', None, TypeError, 'Not a string: None'),
        ('high surrogate early end of string', chr(0xD83D),
         surrogates.DecodeError,
         'Early string end: high surrogate U+D83D not followed '
         'by a low surrogate'),
        ('high surrogate followed by not-low-surrogate character',
         chr(0xD83D) + 'ABC',
         surrogates.DecodeError,
         'High surrogate U+D83D not followed by a low surrogate: found U+41'),
        ('low surrogate first', chr(0xDCA9), surrogates.DecodeError,
         'Low surrogate U+DCA9 not preceded by a high surrogate'),
        ('astral character', chr(0x1f4a9), surrogates.DecodeError,
         'Astral character U+1F4A9 not allowed'),
    ])
    def test_invalid(self, _, encoded, expected_exception, expected_message):
        with self.assertRaises(expected_exception) as catcher:
            surrogates.decode(encoded, reject_astral_characters=True)

        self.assertEqual(str(catcher.exception), expected_message)

    def test_no_exception_with_reject_astral_characters_false(self):
        surrogates.decode(chr(0x1f4a9), reject_astral_characters=False)
