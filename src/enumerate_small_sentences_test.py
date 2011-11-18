#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test code for enumerate_small_sentences.
"""

import nltk

import enumerate_small_sentences as es


def assert_unique(sentences):
    assert len(sentences) == len(set(sentences))


def assert_shorter_than(sentences, length):
    for s in sentences:
        assert len(s) <= length


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

    def test_gsimple(self, gsimple):
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
