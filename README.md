# ==========          processtext          ========== 

**processtext** is a an open-source python package to clean raw text data.          



## Installation

processtext requires [Python 3](https://www.python.org/downloads/), [NLTK](http://www.nltk.org/install.html), and [Autocorrect](https://github.com/filyp/autocorrect) to execute. 

To install using pip, use

`pip install processtext`

[![Downloads](https://static.pepy.tech/badge/processtext)](https://pepy.tech/project/processtext)

## Features 

### processtext package contains different functions such as:
* **degroup_num**: Removes comma(,) in between numbers inside a string
* **remove_hyphen**: Removes hyphen(-) in between texts
* **int_to_en**: Returns whole numbers in english text. e.g. 25 -> twenty-five
* **num_to_en**: Returns english of numbers one by one from left to right
* **float_to_en**: Returns floating point numbers into english text
* **int_to_text**: Replaces all the whole numbers inside string into English text
* **float_to_text**: Replacing all the positive rational numbers inside string into English text
* **decontract_strings**: Decontracts strings e.g. I'm -> I am
* **remove_emoji**: Removes emoji
* **clean_text**: For deep cleaning of texts
* **lowercase**: Converts the texts into lowercase
* **autocorrect**: Corrects spelling mistakes 
* **lemmatize**: Lemmatizes the input texts
* **remove_sw**: Removes stop words
* **clean**: to clean raw text and return the cleaned text
* **clean_l**: to clean raw text and return a list of clean words

##### The processtext.clean() and processtext.clean_l() function can apply all, or a selected combination of the following cleaning operations:
* Remove special symbols/characters
* Remove digits from the text
* Remove punctuations from the text
* Remove extra white spaces
* Remove or replace the part of text with custom regex
* Convert the entire text into a uniform lowercase
* Lemmatize the words 
* Remove stop words, and choose a language for stop words




## Usage

* **Import the library**:

``` python
import processtext as pt
```

* **Choose a method:**

 To return the text in a string format, 
 
``` python
pt.clean("your_raw_text_here") 
```
 
 To return a list of words from the text,
 
``` python
pt.clean_l("your_raw_text_here") 
```
 
 To choose a specific set of cleaning operations,

``` python
pt.clean_l("your_raw_text_here",
clean_all= False # Execute all cleaning operations
extra_spaces=True ,  # Remove extra white spaces 
stemming=True , # Stem the words
stopwords=True ,# Remove stop words
lowercase=True ,# Convert to lowercase
numbers=True ,# Remove all digits 
punct=True ,# Remove all punctuations
reg: str = '<regex>', # Remove parts of text based on regex
reg_replace: str = '<replace_value>', # String to replace the regex used in reg
stp_lang='english'  # Language for stop words
)
```

## Examples


``` python
import processtext as pt
pt.degroup_num('111,222,333')
```

returns,

``` Python
'111222333'
```


``` python
import processtext as pt
pt.remove_hyphen('2022-2023')
```

returns,

``` Python
'2022 2023'
```



``` python
import processtext as pt
print(pt.int_to_en(1998))
print(pt.int_to_en('9123456789'))
```

returns,

``` Python
one thousand nine hundred and ninety-eight

nine billion one hundred and twenty-three million four hundred and fifty-six thousand seven hundred and eighty-nine
```


``` python
import processtext as pt
print(pt.num_to_en(12345))
print(pt.num_to_en('09876'))
```

returns,

``` Python
one two three four five

zero nine eight seven six
```


``` python
import processtext as pt
print(pt.float_to_en(12.345))
print(pt.float_to_en('456.09876'))
```

returns,

``` Python
twelve point three four five

four hundred and fifty-six point zero nine eight seven six
```



``` python
import processtext as pt
print(pt.float_to_en(12.345))
print(pt.float_to_en('456.09876'))
```

returns,

``` Python
twelve point three four five

four hundred and fifty-six point zero nine eight seven six
```


``` python
import processtext as pt
pt.int_to_text('First 100 twin primes have values between 3 & 5 and 3821 & 3823')
```

returns,

``` Python
First one hundred twin primes have values between three & five and three thousand eight hundred and twenty-one & three thousand eight hundred and twenty-three
```


``` python
import processtext as pt
pt.float_to_text('The first 10 digits of pi are 3.141592653')
```

returns,

``` Python
The first ten point zero digits of pi are three point one four one five nine two six five three
```



``` python
import processtext as pt
pt.decontract_strings("I can't believe he'll be graduating from college in just a few months.")
```

returns,

``` Python
I can not believe he will be graduating from college in just a few months.
```



``` python
import processtext as pt
pt.remove_emoji("🌞🌊☀️ Just spent an amazing day at the beach with my friends! 🏖️👭👬 We built sandcastles 🏰, played beach volleyball 🏐, and even went for a swim 🏊‍♀️🏊‍♂️. The sun was shining ☀️ and the water was so refreshing 💦. Can't wait to do it again! 🤩👍")
```

returns,

``` Python
 Just spent an amazing day at the beach with my friends!  We built sandcastles , played beach volleyball , and even went for a swim . The sun was shining  and the water was so refreshing . Can't wait to do it again! 
```



``` python
import processtext as pt
pt.clean_text('The password must contain at least one symbol such as !,^,*,+,=,%,$,~,?,/,<>,|@, #, or %.')
```

returns,

``` Python
The password must contain at least one symbol such as                               or   
```



``` python
import processtext as pt
pt.lowercase('THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG.')
```

returns,

``` Python
the quick brown fox jumped over the lazy dog.
```



``` python
import processtext as pt
pt.lowercase('THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG.')
```

returns,

``` Python
the quick brown fox jumped over the lazy dog.
```



``` python
import processtext as pt
pt.autocorrect("I haven't receeved the package yet, but I think it should arrive somtime tomoro.")
```

returns,

``` Python
I haven't received the package yet, but I think it should arrive sometime tomorrow.
```


``` python
import processtext as pt
pt.autocorrect("I haven't receeved the package yet, but I think it should arrive somtime tomoro.")
```

returns,

``` Python
I haven't received the package yet, but I think it should arrive sometime tomorrow.
```



``` python
import processtext as pt
pt.lemmatize('they were playing in the garden.')
```

returns,

``` Python
they be play in the garden.
```



``` python
import processtext as pt
pt.remove_sw('I went to the store and bought some milk, bread, and eggs.')
```

returns,

``` Python
went store bought milk, bread, eggs.
```
 


``` python
import processtext as pt
pt.clean("TH@@#e Q!@#UicK bR0owN f*#!@)(O000000X JUmp100ED 000oV###3eR Th77777#$$e..........                 L@a/\|z+Y d==OG.", extra_spaces=True, lowercase=True, numbers=True, punct=True)
```

returns,

``` Python
'the quick brown fox jumped over the lazy dog'
```

----

``` Python
import processtext as pt
pt.clean_l('TH@@#e Q!@#UicK bR0owN f*#!@)(O000000X JUmp100ED 000oV###3eR Th77777#$$e..........                 L@a/\|z+Y d==OG.', 
           extra_spaces=True, lowercase=True, numbers=True, punct=True)
```

returns,

``` Python
['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
```

----

``` Python
from processtext import clean
text = "my email id: ujjwal@rkmvu.ac.in and your's: mili@rnlk.ed"
clean(text, reg=r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", reg_replace='********', clean_all=False)

```

returns,

``` Python
'my email id: ******** and your's: ********'
```

## License

##### MIT

