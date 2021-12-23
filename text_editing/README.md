# Description

The `reda.py` script augments texts by 5 simple text editing operations for both Chinese and English, including Synonym Replacement, Random Swapping, Random Insertion, Random Deletion, and Random Mixes. The current program supports both Chinese and English and can be applied to other languages with proper data and setups.

This program is based on [a paper of mine](https://arxiv.org/abs/2111.14709) in this regard, which is inspired by the [Esay Data Augmentation](https://github.com/jasonwei20/eda_nlp) program. `reda` stands for <ins>Revised Esay Data Augmentation</ins>. Please refer to [my previous repository](https://github.com/jaaack-wang/linguistic-knowledge-in-DA-for-NLP) to find out more about the differences between the EDA and  REDA programs. 

<a name='usage'></a>
# Usage

You can click the `reda_example.ipynb` file to see how the `reda.py ` script can be used. A simple example:

```py
from reda import REDA

reda_en = REDA(lang='en')
text = 'I am very happy today'
reda_en.augment_text(text, out_num_each=1, max_out_num=10, out_str=True)
```

Possible outputs (as the text editing operations are randomized):

```cmd
['1 atomic_number_53 sad very happy today super am do you',
 'I am dress happy today super sad very real you',
 'I am rattling happy today super distressing do you know',
 'I am very glad today tops sad do you know',
 'I am very happy today super do you know',
 'I am very happy today super sad you know',
 'I am very happy well-chosen today super sad do you know',
 'I am very rattling happy today super sad do you know',
 'sad am very happy I super today do you know',
 'super am very happy today know sad do you I']
```

If you only want to do one or parts of the five text editing operations, you can call the corresponding functions separately. Please note that, in this case, 
you need to pass a list of tokenized words to the function instead of a string. The parameters below are randomly given:

```python
from reda import REDA

reda_en = REDA(lang='en')
text = 'I am very happy today'
text = reda_en.tokenize(text)
# synonym replacement
reda_en.replace_syn(text, rpl_num=2, out_num=5, out_str=False)
# random swapping
reda_en.swap_words(text, swap_num=2, out_num=5, out_str=True)
# random insertion
reda_en.insert_words(text, insert_num=2, out_num=5, out_str=True)
# random deletion
reda_en.delete_words(text, delete_num=2, out_num=5, out_str=True)
# random mixes (random 2~4 of the 4 operations above)
reda_en.mixed_edits(text, max_mix=3, out_num=5, out_str=False)
```

# Data

For illustration purposes, the `syn_dics.zip` provides synonym dictionaries for playing with the `reda.py` script. You should unzip it in order to run the script. `syn_dics.zip ` comes with the following two dictionaries:

- `synonyms_zh.json`: a Chinese synonym dictionary from [my previous work](https://github.com/jaaack-wang/Chinese-Synonyms/tree/main/Trimmed_Synonyms).
- `synonyms_en.json`: extracted from NLTK's WordNet. Check [here](https://github.com/jaaack-wang/text-augmentation-techniques/blob/main/word_replacement/EnglishSynonymDictMaking.ipynb) to learn how it was made. 


You can also use your own data as long as the data formats are compatible with the provided ones. In theory, you can apply `reda.py` script to other languages unmodified given proper data and setups. For example:

```python
from wordReplacement import WordsReplacement

# Initialization
syn_path ='filepath_Arabic_syn_dic'
tokenizer ='a_tokenizer_method_for_Arabic'
sep = 'separator_for_Abrabic_words'
reda_ab = REDA(syn_path=syn_path, tokenizer=tokenizer, sep=sep)
```



# Notes

As you might have noticed in the [Usage](#usage) section, the quality of the synonym dictionary is very critical for synonym replacements. However, a high-quality synonym is hard to find. Moreover, as a word can have different meanings and parts of speech, its synonyms are not all "synonyms" under all circumstances, which is a problem I do not address here.   
