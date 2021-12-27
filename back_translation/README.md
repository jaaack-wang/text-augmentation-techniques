# Description

Back translation is a very reliable way to produce paraphrases and thus augment label-preserving texts but at the expense of a higher cost, either time wise or resource wise. 

`back_trans_model.py` provides a general class method to play with back translation, either for fun or for text augmentation. `back_translators.py` contains three sub-classes that implement the `back_trans_model.py` general class. These three back translators are three online translators I often use: [Baidu Transalte](https://fanyi.baidu.com/?aldtype=16047#auto/zh) (Chinese company), [Google Translate](https://translate.google.ca) (American company), and [Papago Translate](https://papago.naver.com) (Korean company).

`GoogleBackTranslator` is provided for illustration purpose, so you can use it directly to see how the general back translator works. To use `BaiduBackTranslator` and `PapagoBackTranslator`, you need to apply for their cloud translation API at the following two addresses respectively: [BaiduAPI](https://fanyi-api.baidu.com/product/11), [PapagoAPI](https://developers.naver.com/products/papago/nmt/nmt.md). However, the application for the former requires a Chinese domestic phone number for verification. You may also need to transalte the related webpages if you do not understand Chinese or Korean. 



# back_trans_model

`back_trans_model.py` provides a simple and general class method to construct a back translator provided a translator and a language dictionary for that translator. If you search around online, you should be able to identify many (totally or restrictively) free translators either by applying for translation APIs or by rule-based web scraping.

To construct a back translator of your own, do following:
 

```python
>>> from back_trans_model import BackTranslate
# Parameters must be: (query, src_lang, dst_lang). 
# The input and output must both be a str.
>>> translator = 'a method that can translate'
# lang_dict: lang code and name pairs
>>> lang_dict = 'a lang_dict for that the translator'
>>> dst_lang = 'the default dst_lang when doing back translation'
# Initialization and the construction is now done!
>>> BT = BackTranslate(translator, lang_dict, dst_lang)
```


# Usage

You can click `BackTranslationIllustration.ipynb` to see the full illustration of how a constructed back translator can be used. Let's take `GoogleBackTranslator` for example, which can also be seen in `GoogleBackTranslatorExample.ipynb`.

### Initialization 

```python
>>> from back_translators import GoogleBackTranslator
>>> GBT = GoogleBackTranslator('English')
>>> query = 'Today, I am very happy!'
```

### Back Translation

- Through one language (e.g., english --> french --> english)
```python
>>> GBT.back_translate(query, mid_lang='Vietnamese')
# Output: I'm very happy today!
```
- Through multiple languages one at a time  (e.g., en -> L1 -> en; en -> L2 -> en ...)

```python
>>> GBT.back_translate(query, mid_lang=['french', 'zh-cn'])
# Output: ['Today I am very happy!', 'I am really happy today!']
```


- Through multiple languages at one time (e.g., en -> L1, L2, ... Ln -> english)
```python
>>> GBT.back_translate(query, mid_lang=['french', 'zh-cn'], all_mid_lang=True)
# Output: I am really happy today!
```

- To track the entire translation process
```python
>>> GBT.back_translate(query, mid_lang=['french', 'zh-cn', 'japanese'], all_mid_lang=True, out_dict=True)
```
```text
# Output:
{'srcLang': 'english',
 'originText': 'Today, I am very happy!',
 'transLang1': 'french',
 'transText1': "Aujourd'hui, je suis très heureux!",
 'transLang2': 'chinese (simplified)',
 'transText2': '今天我很开心！',
 'transLang3': 'japanese',
 'transText3': '今日は本当に嬉しいです！',
 'dstLang': 'english',
 'finalText': "I'm really happy today!"}
```

- Use `bulk_back_translate` for back translating a list of queries
```python
# query can also be a list of texts too
>>> GBT.bulk_back_translate([query, 'back translation is super fun'], mid_lang='ja')
# output: ["I'm very happy today!", 'Reverse translation is a lot of fun']
```


### Used for augmentation

```python
>>> GBT.augment(query, mid_lang='korean', out_per_text=3)
# Output: ['Today I am very happy!', 'Today, I am so happy!']
```

### Used for translation

```python
# For one query
>>> GBT.translate(query, src_lang='en', dst_lang='zh-cn')
# Output: 今天，我很开心！
# For a list of queries
>>> GBT.bulk_transalte([query, 'back translation is super fun'], src_lang='en', dst_lang='zh-cn')
# Output: ['今天，我很开心！', '回译超级有趣']
```

### Used for fun 

- Machine translation has improved aaaaaaa loooooooot!
```python
>>> query = 'The spirit is willing but the flesh is weak'
>>> GBT.back_translate(query, mid_lang='russian')
# Output: The spirit is willing, but the flesh is weak
# 1960s: The vodka is good, but the meat is rotten
```

# Disclaimer

The methods provided here for accessing Google Translate without applying for access to its API are for illustration purposes. If you are to use Google Transalate to do massive back transaltions, please apply for its API as that is the most reliable and ethical use of its could translation service. 

You can apply for Google Translate API at [here](https://cloud.google.com/translate/). More see:[Quickstarts](https://cloud.google.com/translate/docs/quickstarts) and [Tutorial](https://codelabs.developers.google.com/codelabs/cloud-translation-python3#0).
