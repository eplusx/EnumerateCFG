#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test code for enumerate_small_sentences.
"""

import pytest
import nltk
from nltk.grammar import Nonterminal

import enumerate_small_sentences as es


def assert_unique(sentences):
    assert len(sentences) == len(set(sentences))


def assert_shorter_than(sentences, length):
    for s in sentences:
        assert len(s.split()) <= length

def assert_correct(grammar, length, count):
    sentences = es.enumerate(grammar, length)
    assert len(sentences) == count
    assert_unique(sentences)
    assert_shorter_than(sentences, length)


class TestEnumerateSmallSentences(object):

    def pytest_funcarg__gsimple(self, request):
        return nltk.parse.load_parser('file:../grammars/simple.cfg').grammar()

    def pytest_funcarg__gtong(self, request):
        return nltk.parse.load_parser('file:../grammars/tong.cfg').grammar()

    def test_enumerate_gsimple_Det(self, gsimple):
        sentences = es._enumerate(gsimple, [Nonterminal('Det')], 1)
        assert sentences == ['the', 'a']

    def test_enumerate_gsimple_N(self, gsimple):
        sentences = es._enumerate(gsimple, [Nonterminal('N')], 1)
        assert sentences == ['man', 'park', 'dog', 'telescope']

    def test_enumerate_gsimple_V(self, gsimple):
        sentences = es._enumerate(gsimple, [Nonterminal('V')], 1)
        assert sentences == ['saw', 'walked']

    def test_enumerate_gsimple_P(self, gsimple):
        sentences = es._enumerate(gsimple, [Nonterminal('P')], 1)
        assert sentences == ['in', 'with']

    def test_gsimple(self, gsimple):
        pytest.skip()
        assert_correct(gsimple, 0, 0)
        assert_correct(gsimple, 1, 0)
        assert_correct(gsimple, 2, 0)
        assert_correct(gsimple, 3, 0)
        assert_correct(gsimple, 4, 0)
        assert_correct(gsimple, 5, 0)
        assert_correct(gsimple, 6, 128)
        assert_correct(gsimple, 7, 128)
        assert_correct(gsimple, 8, 128)
        assert_correct(gsimple, 9, 128)
        assert_correct(gsimple, 10, 128)
        assert_correct(gsimple, 100, 128)
        assert_correct(gsimple, 1000, 128)


def main():
    pytest.main(args=[__file__.replace('.pyc', '.py')])


if __name__ == '__main__':
    main()
