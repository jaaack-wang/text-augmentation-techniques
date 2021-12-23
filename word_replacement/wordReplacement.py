'''
Author: Zhengxiang (Jack) Wang 
GitHub: https://github.com/jaaack-wang 
About: Common word replacement method for text augmentation, 
including synonym-based and embedding-based two approaches. 
'''

import json
from random import sample, choice
from itertools import groupby
import jieba
from gensim import models


class WordsReplacement:
    '''Augments texts by synonym-based or embeddings-based word replacements for both Chinese and English. The code
    also works for other languages provided that proper data and setups are given.

    Parameters:
        lang (str): defaults to "zh" (Chinese). Also supports "en" (English).
        rpl_type (str): replacement type, "syn" (synonym-based) or "embd" (embeddings-based). Defaults to "syn".
        rpls_path (str): filepath to the pre-stored synonym or embedding files. If None, uses the default files.
        tokenizer (method): tokenizer for Chinese or English. Should be a function. If None, uses defaults tokenizers.
        topn (int): the number of nearest words to choose for embedding-based word replacements. Defaults to 5.
        sep (str): separator. For Chinese, there is no separator between words; for English, that a space.

    ####################
    Usage:
    ####################
    from wordReplacement import WordsReplacement

    w_replace_en = WordsReplacement(lang='en', rpl_type='embd')
    w_replace_en.replace_word('I am very happy today', rpl_num=2, out_num=5, out_str=False)
    '''
    
    def __init__(self, lang='zh', rpl_type='syn', rpls_path=None, tokenizer=None, topn=5, sep=None):
        self.lang = lang
        self.rpl_type = rpl_type
        self.rpls_path = rpls_path
        self.tokenize = tokenizer
        self.sep = sep
        assert self.lang in ['zh', 'en'], 'self.lang must be either Chinese (zh) or English (en)'
        assert self.rpl_type in ['syn', 'embd'], 'self.rpl_type must be either synonym (syn) or embedding (embd)'
        
        if self.rpl_type == 'syn':
            if not self.rpls_path:
                if self.lang == 'zh':
                    self.rpls_path = 'synonyms_zh.json'
                else:
                    self.rpls_path = 'synonyms_en.json'
            self._syn = json.load(open(self.rpls_path))
            self._get_random_rpl_word = lambda w: choice(self._syn[w])
            self._replaceable_idx = lambda ws: [i for i in range(len(ws)) if ws[i] in self._syn]
        
        else:
            if not self.rpls_path:
                if self.lang == 'zh':
                    self.rpls_path = 'embd_zh.txt'
                else:
                    self.rpls_path = 'embd_en.txt'
                
            self._model = models.KeyedVectors.load_word2vec_format(self.rpls_path, binary=False)
            self._get_random_rpl_word = lambda w: choice(self._model.most_similar(w, topn=topn))[0]
            self._replaceable_idx = lambda ws: [i for i in range(len(ws)) if ws[i] in self._model.index_to_key]
        
        if not self.tokenize:
            if self.lang == 'zh':
                self.tokenize = jieba.lcut
            else:
                self.tokenize = lambda w: w.split()

        if not self.sep:
            if self.lang == 'zh':
                self.sep = ''
            else:
                self.sep = ' '

    @staticmethod
    def _out(func, out_num):
        # a func to helps deduplicate the outputs
        if out_num == 1:
            return func()
        
        out = []
        for _ in range(out_num):
            out.append(func())

        out.sort()        
        return [o for o,_ in groupby(out)]
    
    def _out_str(self, words, out_str):
        # a func to return the output in a right format 
        if out_str:
            return f'{self.sep}'.join(words)
        return words
    
    def replace_word(self, words, rpl_num=1, out_num=1, out_str=False):
        '''Replaces given num of synonyms for randomly chosen eligible words for given times.'''
        def replace():
            words_copy = words.copy()
            rpl_idx = sample(replaceable_idx, rpl_num)
            for i in rpl_idx:
                words_copy[i] = self._get_random_rpl_word(words[i])
            return self._out_str(words_copy, out_str)
        
        if isinstance(words, str):
            words = self.tokenize(words)
        elif isinstance(words, list):
            pass
        else:
            raise TypeError("The input words must be either a str or a list")
            
        replaceable_idx = self._replaceable_idx(words)
        if len(replaceable_idx) == 0:
            return self._out_str(words, out_str)
        if len(replaceable_idx) < rpl_num:
            rpl_num = len(replaceable_idx)
        return self._out(replace, out_num)
