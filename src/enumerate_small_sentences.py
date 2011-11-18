'''
Created on Nov 15, 2011

@author: arnaud
'''

def enumerate(grammar, max_len):
    return _enumerate(grammar, [grammar.start()], max_len)

def _enumerate(grammar, symbols, max_len, nest=0):
    enum = []
    if len(symbols) == 1:
        print ' ' * nest + 'SYMBOL: ', symbols[0]
        if isinstance(symbols[0], str):
            enum.append(symbols[0])
        else:
            for prod in grammar.productions(lhs=symbols[0]):
                print ' ' * nest + 'REWRITE:', prod, max_len
#                n_max_len = max_len - len(prod.rhs()) + 1
                if max_len >= len(prod.rhs()):
                    enum.extend(_enumerate(grammar, prod.rhs(), max_len, nest + 1))                    
    else:
        print ' ' * nest + 'SYMBOLS:', symbols
        for first_symbol in _enumerate(grammar, [symbols[0]], max_len, nest + 1):
            print ' ' * nest + 'FIRST:  ', first_symbol
            for other_symbols in _enumerate(grammar, symbols[1:], max_len - len(first_symbol), nest + 1):
                print ' ' * nest + 'APPEND: ', first_symbol, other_symbols
                enum.append(first_symbol + ' ' + other_symbols)
    return enum

if __name__ == "__main__":
    import nltk
    
    grammar = nltk.parse.load_parser('file:../grammars/tong.cfg').grammar()
    
    sentences = enumerate(grammar, 7) 
    
    for sent in sentences:
        print sent
        
    print len(sentences)
