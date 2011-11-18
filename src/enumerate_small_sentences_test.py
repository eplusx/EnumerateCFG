#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test code for enumerate_small_sentences.
"""

import pytest
import nltk
from nltk.grammar import Nonterminal

import enumerate_small_sentences as es


def setup_module(module):
    import logging
    handler = logging.StreamHandler()
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(handler)


def assert_unique(sentences):
    assert len(sentences) == len(set(es.flattened(sentences)))


def assert_shorter_than(sentences, length):
    for symbols in sentences:
        assert len(symbols) <= length

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
        assert es.flattened(sentences) == ['the', 'a']

    def test_enumerate_gsimple_N(self, gsimple):
        sentences = es._enumerate(gsimple, [Nonterminal('N')], 1)
        assert es.flattened(sentences) == ['man', 'park', 'dog', 'telescope']

    def test_enumerate_gsimple_V(self, gsimple):
        sentences = es._enumerate(gsimple, [Nonterminal('V')], 1)
        assert es.flattened(sentences) == ['saw', 'walked']

    def test_enumerate_gsimple_P(self, gsimple):
        sentences = es._enumerate(gsimple, [Nonterminal('P')], 1)
        assert es.flattened(sentences) == ['in', 'with']

    def test_enumerate_gsimple_NP(self, gsimple):
        sentences = es._enumerate(gsimple, [Nonterminal('NP')], 2)
        assert es.flattened(sentences) == \
            ['the man', 'the park', 'the dog', 'the telescope',
             'a man', 'a park', 'a dog', 'a telescope']

    def test_enumerate_gsimple_VP(self, gsimple):
        sentences = es._enumerate(gsimple, [Nonterminal('VP')], 3)
        assert es.flattened(sentences) == \
            ['saw the man', 'saw the park', 'saw the dog', 'saw the telescope',
             'saw a man', 'saw a park', 'saw a dog', 'saw a telescope',
             'walked the man', 'walked the park', 'walked the dog',
             'walked the telescope', 'walked a man', 'walked a park',
             'walked a dog', 'walked a telescope']

    def test_gsimple_short(self, gsimple):
        assert_correct(gsimple, 0, 0)
        assert_correct(gsimple, 1, 0)
        assert_correct(gsimple, 2, 0)
        assert_correct(gsimple, 3, 0)
        assert_correct(gsimple, 4, 0)

    def test_gsimple(self, gsimple):
        assert_correct(gsimple, 5, 0)
        assert_correct(gsimple, 6, 128)
        assert_correct(gsimple, 7, 128)
        assert_correct(gsimple, 8, 128)
        assert_correct(gsimple, 9, 128)

    def test_gsimple_long(self, gsimple):
        assert_correct(gsimple, 10, 128)
        assert_correct(gsimple, 100, 128)
        assert_correct(gsimple, 1000, 128)

    def test_enumerate_gtong_PropN(self, gtong):
        sentences = es._enumerate(gtong, [Nonterminal('PropN')], 1)
        assert es.flattened(sentences) == ['John', 'Mary']

    def test_enumerate_gtong_IVsing(self, gtong):
        sentences = es._enumerate(gtong, [Nonterminal('IVsing')], 1)
        assert es.flattened(sentences) == ['walks', 'lives']


def main():
    pytest.main(args=[__file__.replace('.pyc', '.py')])


if __name__ == '__main__':
    main()
