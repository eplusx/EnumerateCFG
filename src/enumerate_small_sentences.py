'''
Created on Nov 15, 2011

@author: arnaud
'''

import logging


logger = logging.getLogger('enumerate')


def enumerate(grammar, max_len):
    return _enumerate(grammar, [grammar.start()], max_len)

def _enumerate(grammar, symbols, max_len, nest=0):
    enum = []
    if len(symbols) == 1:
        logger.debug(' ' * 2 * nest + 'SYMBOL:  {0} (max_len {1})'.format(
                     symbols[0], max_len))
        if isinstance(symbols[0], str):
            enum.append(symbols[0])
        else:
            for prod in grammar.productions(lhs=symbols[0]):
                logger.debug(' ' * 2 * nest + 'REWRITE: {0}'.format(prod))
#                n_max_len = max_len - len(prod.rhs()) + 1
                if max_len >= len(prod.rhs()):
                    enum.extend(_enumerate(grammar, prod.rhs(), max_len, nest + 1))
    else:
        logger.debug(' ' * 2 * nest + 'SYMBOLS: {0} (max_len {1})'.format(
                     symbols, max_len))
        logger.debug(' ' * 2 * nest + 'FIRST:   {0}'.format(symbols[0]))
        for first_symbol in _enumerate(grammar, [symbols[0]], max_len, nest + 1):
            logger.debug(' ' * 2 * nest + 'FIRST\':  {0}'.format(first_symbol))
            logger.debug(' ' * 2 * nest + 'OTHERS:  {0}'.format(symbols[1:]))
            for other_symbols in _enumerate(grammar, symbols[1:], max_len - len(first_symbol), nest + 1):
                logger.debug(' ' * 2 * nest + 'CONCAT:  {0} {1}'.format(
                             first_symbol, other_symbols))
                enum.append(first_symbol + ' ' + other_symbols)
    logger.debug(' ' * 2 * nest + 'RETURN:  {0}'.format(enum))
    return enum

if __name__ == "__main__":
    import nltk
    
    grammar = nltk.parse.load_parser('file:../grammars/tong.cfg').grammar()
    
    sentences = enumerate(grammar, 7) 
    
    for sent in sentences:
        print sent
        
    print len(sentences)
