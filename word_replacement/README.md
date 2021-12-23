# Description

Word replacement is a simple way to augment texts and it usually works by replacing a given word with a word of similar meaning and function. Currently, there are two common ways to do that: one is to use a synonym dictionary and one is to use pre-trained word embeddings. 

The `wordReplacement.py` provides a sample script to help you augment texts by both means. The current script supports Chinese and English, but it can be easily adapted for other languages.      


# Usage

You can click the `Word_Replacements.ipynb` file to see how the `wordReplacement.py` script can be used. The basic usage is illustrated below:

```py
from wordReplacement import WordsReplacement

w_replace = WordsReplacement(lang='en', rpl_type='embd')
w_replace.replace_word('I am very happy today', rpl_num=2, out_num=5)
```

Possible outputs (as the word replacement is randomized):

```cmd
[['a', ' ', 'am', ' ', 'very', ' ', 'happy', ' ', 'today'],
 ['is', ' ', 'am', ' ', 'very', ' ', 'happy', ' ', 'today'],
 ['to', ' ', 'am', ' ', 'very', ' ', 'happy', ' ', 'today'],
 ['you', ' ', 'am', ' ', 'very', ' ', 'happy', ' ', 'today']]
```

# Data

For illustration purposes, the `data.zip` provides data for playing with the `wordReplacement.py` script (as such, the data quality is not guaranteed here and the data size is kept small). It comes with the following four files:

- `synonyms_zh.json`: a Chinese synonym dictionary from [my previous work](https://github.com/jaaack-wang/Chinese-Synonyms/tree/main/Trimmed_Synonyms).
- `synonyms_en.json`: extracted from NLTK's WordNet. See `EnglishSynonymDictMaking.ipynb` for details. 
- `embd_zh.txt`: the first 5000 word embeddings from `w2v.weibo.target.word-word.dim300`, downloaded by calling `paddlenlp.embeddings.TokenEmbedding `. Check [my previous tutorial on this](https://github.com/jaaack-wang/dl-nlp-using-paddlenlp/blob/main/paddlenlp_updated_notes_English/WordEmbedding/1-loading%20pre-trained%20word%20embedding%20in%20paddlenp.ipynb).
- `embd_en.txt`: the first 10000 word embeddings from `glove.6B.50d.txt`. See [glove website](https://nlp.stanford.edu/projects/glove/). 


You can also use your own data as long as the data formats are compatible with the provided ones. In theory, you can apply `wordReplacement.py` script to other languages without modifying it given proper data and setups. For example:

```python
from wordReplacement import WordsReplacement

w_replace = WordsReplacement(rpl_type='embd', rpls_path='filepath_to_pre-trained_Arabic Embeddings', tokenizer='a_tokenizer_method_for_Arabic')
```



# Notes

Please note that, neither of synonym-based or embedding-based approaches is reliable enough to generate paragraphs. It is easy to think that words of close embeddings in verctor space do not neccessary have close meaning and function. 

For a synonym dictionry, due to the wide existence of polysemy (i.e., one word with many meanings or multiple parts of speech), it is just often the case that the randomly selected "synonym" of a word is not a real "synmony" in the position of the replaced words. 