# Description

Word replacement is a simple but frequently used method to augment texts and it usually works by replacing a given word with a word of similar meaning and function. Currently, there are two common ways to do that: one is to use a synonym dictionary and one is to use pre-trained word embeddings. 

The `wordReplacement.py` provides a sample script to help you augment texts by both means. The current script supports Chinese and English, but it can also be easily adapted for other languages with proper data and setups (see [the `Dada` section](#data)).      


# Usage

You can click the `Word_Replacements.ipynb` file to see how the `wordReplacement.py` script can be used. A simple example:

```py
from wordReplacement import WordsReplacement
# works for English and use the embedding-based approach
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

<a name='data'></a>
# Data

For illustration purposes, the `data.zip` provides data for playing with the `wordReplacement.py` script (as such, the data quality is not guaranteed here and the data size is kept small). You should unzip it in order to run the script. `data.zip` comes with the following four files:

- `synonyms_zh.json`: a Chinese synonym dictionary from [my previous work](https://github.com/jaaack-wang/Chinese-Synonyms/tree/main/Trimmed_Synonyms).
- `synonyms_en.json`: extracted from NLTK's WordNet. See `EnglishSynonymDictMaking.ipynb` for how it was made. 
- `embd_zh.txt`: the first 5000 word embeddings from `w2v.weibo.target.word-word.dim300`, downloaded by calling `paddlenlp.embeddings.TokenEmbedding `. Check [my previous tutorial](https://github.com/jaaack-wang/dl-nlp-using-paddlenlp/blob/main/paddlenlp_updated_notes_English/WordEmbedding/1-loading%20pre-trained%20word%20embedding%20in%20paddlenp.ipynb) on this.
- `embd_en.txt`: the first 10000 word embeddings from `glove.6B.50d.txt`. See the [glove website](https://nlp.stanford.edu/projects/glove/). 


You can also use your own data as long as the data formats are compatible with the provided ones. In theory, you can apply `wordReplacement.py` script to other languages unmodified given proper data and setups. For example:

```python
from wordReplacement import WordsReplacement

# Initialization
w_replace = WordsReplacement(rpl_type='embd', rpls_path='filepath_to_pre-trained_Arabic Embeddings', tokenizer='a_tokenizer_method_for_Arabic')
```



# Notes

Please note that, neither of synonym-based or embedding-based approaches is reliable enough to generate paragraphs. It is easy to think that words of close embeddings in verctor space do not neccessary have close meaning and function. 

For a synonym dictionary, due to the wide existence of polysemy (i.e., one word with many meanings or multiple parts of speech), it is just often the case that the randomly selected "synonym" of a word is not a real "synmony" in the position of the replaced word. 
