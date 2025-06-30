#!/usr/bin/python
#
# Copyright 2025 Ian Lewis
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""run_budoux handles line breaks in Japanese LaTeX text.

run_budoux parses Japanese LaTeX text input and formats it using budoux to
better handle line breaks in LaTeX documents.
"""

import sys

import budoux
from pylatexenc.latexwalker import (
    LatexWalker,
    LatexCharsNode,
)

CHINESE_RANGES = [
    (0x4E00, 0x9FFF),  # CJK Unified Ideographs
    (0x3400, 0x4DBF),  # CJK Unified Ideographs Extension A
    (0x20000, 0x2A6DF),  # CJK Unified Ideographs Extension B
    (0x2A700, 0x2B73F),  # CJK Unified Ideographs Extension C
    (0x2B740, 0x2B81F),  # CJK Unified Ideographs Extension D
]

JAPANESE_RANGES = [
    (0x3040, 0x309F),  # Hiragana
    (0x30A0, 0x30FF),  # Katakana
    (0xFF66, 0xFF9F),  # Half-width Katakana
]

KOREAN_RANGES = [
    (0xAC00, 0xD7AF),  # Hangul Syllables
    (0x1100, 0x115F),  # Hangul Jamo
    (0x1160, 0x11FF),  # Hangul Jamo Extended-A
    (0xA960, 0xA97F),  # Hangul Jamo Extended-B
]


def is_cjk(char: str) -> bool:
    """Check if a character is a CJK character."""
    for char_ranges in [CHINESE_RANGES, JAPANESE_RANGES, KOREAN_RANGES]:
        if any(start <= ord(char) <= end for start, end in char_ranges):
            return True
    return False


def has_cjk(text: str) -> bool:
    """Check if a string contains any CJK characters."""
    return any(is_cjk(c) for c in text)


def main() -> int:
    """Implement the main functionality of run_budoux."""
    parser = budoux.load_default_japanese_parser()
    input_code = sys.stdin.read().strip()

    walker = LatexWalker(input_code)
    nodes, _, _ = walker.get_latex_nodes()

    for node in nodes:
        if node.isNodeType(LatexCharsNode):
            for part in parser.parse(node.chars):
                words = []
                for word in part.split():
                    if has_cjk(word):
                        words.append("\\nolinebreak[3]".join(word))
                    else:
                        words.append(word)
                sys.stdout.write("~".join(words))
                sys.stdout.write("\\allowbreak ")
        else:
            sys.stdout.write(node.latex_verbatim())

    return 0


if __name__ == "__main__":
    sys.exit(main())
