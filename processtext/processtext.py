"""texttools"""
import re
import nltk
import string 
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
from autocorrect import Speller
from .exceptions import CleanTextEmptyString


nltk.download('stopwords')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()




# Removing comma(,) in between number e.g 12,000 -> 12000
def degroup_num(text : str)-> str:
    """Given raw string returns comma removed numbers. It is necessary because sometimes in text data numbers are grouped by commas(,)
    
    :param text: Input text to degroup numbers inside it
    """
    text = re.sub(r"(?<=\d),(?=\d)", "",text)
    return text




# Removing hyphen (-)
def remove_hyphen(text: str)-> str:
    """Given raw string replace hyphen (-) with a blank space.
    
    :param text: Input text to replace hyphen with a space
    """
    text = re.sub("-", " ",text)
    return text




# Returns whole numbers in english
def int_to_en(num):
    
    """Returns whole numbers in english text.
    
    :param num: Input str or int
    """
    num  = abs(int(num))
    d = {0 : 'zero', 
         1 : 'one', 
         2 : 'two', 
         3 : 'three', 
         4 : 'four', 
         5 : 'five',
         6 : 'six', 
         7 : 'seven', 
         8 : 'eight', 
         9 : 'nine', 
         10 : 'ten',
         11 : 'eleven', 
         12 : 'twelve', 
         13 : 'thirteen', 
         14 : 'fourteen',
         15 : 'fifteen', 
         16 : 'sixteen', 
         17 : 'seventeen', 
         18 : 'eighteen',
         19 : 'nineteen', 
         20 : 'twenty',
         30 : 'thirty', 
         40 : 'forty', 
         50 : 'fifty', 
         60 : 'sixty',
         70 : 'seventy', 
         80 : 'eighty', 
         90 : 'ninety' }
    
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    #assert(0 <= num)

    if (num < 20):
        return d[num]

    if (num < 100):
        if num % 10 == 0: return d[num]
        else: return d[num // 10 * 10] + '-' + d[num % 10]

    if (num < k):
        if num % 100 == 0: return d[num // 100] + ' hundred'
        else: return d[num // 100] + ' hundred and ' + int_to_en(num % 100)

    if (num < m):
        if num % k == 0: return int_to_en(num // k) + ' thousand'
        else: return int_to_en(num // k) + ' thousand ' + int_to_en(num % k)

    if (num < b):
        if (num % m) == 0: return int_to_en(num // m) + ' million'
        else: return int_to_en(num // m) + ' million ' + int_to_en(num % m)

    if (num < t):
        if (num % b) == 0: return int_to_en(num // b) + ' billion'
        else: return int_to_en(num // b) + ' billion ' + int_to_en(num % b)

    if (num % t == 0): return int_to_en(num // t) + ' trillion'
    else: return int_to_en(num // t) + ' trillion ' + int_to_en(num % t)

    raise AssertionError('num is too large: %s' % str(num))






# Return english of numbers one by one from left to right
def num_to_en(num):
    """Return english text of number one by one from left to right.
    
    :param num: Input str or int
    """
    num = str(num)
    d = {'0' : 'zero', 
         '1' : 'one', 
         '2' : 'two', 
         '3' : 'three', 
         '4' : 'four', 
         '5' : 'five',
         '6' : 'six', 
         '7' : 'seven', 
         '8' : 'eight', 
         '9' : 'nine'}
    

    
    if len(num) ==1:
        return d[num]
    
    if len(num) ==2:
        return d[num[0]] +' '+ d[num[1]]
    
    if len(num) ==3:
        return d[num[0]] +' '+ d[num[1]] +' '+ d[num[2]]
    
    if len(num) ==4:
        return d[num[0]] +' '+ d[num[1]] +' '+ d[num[2]] +' '+ d[num[3]]
    
    if len(num) ==5:
        return d[num[0]] +' '+ d[num[1]] +' '+ d[num[2]] +' '+ d[num[3]] +' '+ d[num[4]]
    
    if len(num) ==6:
        return d[num[0]] +' '+ d[num[1]] +' '+ d[num[2]] +' '+ d[num[3]] +' '+ d[num[4]] +' '+ d[num[5]]
    
    if len(num) ==7:
        return d[num[0]] +' '+ d[num[1]] +' '+ d[num[2]] +' '+ d[num[3]] +' '+ d[num[4]] +' '+ d[num[5]] +' '+ d[num[6]]
    
    if len(num) ==8:
        return d[num[0]] +' '+ d[num[1]] +' '+ d[num[2]] +' '+ d[num[3]] +' '+ d[num[4]] +' '+ d[num[5]] +' '+ d[num[6]] +' '+ d[num[7]]
    
    if len(num) ==9:
        return d[num[0]] +' '+ d[num[1]] +' '+ d[num[2]] +' '+ d[num[3]] +' '+ d[num[4]] +' '+ d[num[5]] +' '+ d[num[6]] +' '+ d[num[7]] +' '+ d[num[8]]
    
    if len(num) >= 10:
        return d[num[0]] +' '+ d[num[1]] +' '+ d[num[2]] +' '+ d[num[3]] +' '+ d[num[4]] +' '+ d[num[5]] +' '+ d[num[6]] +' '+ d[num[7]] +' '+ d[num[8]] +' '+ d[num[9]]


    raise AssertionError('number in decimal place is too large')




# Converting floating point numbers into english text

def float_to_en(f)-> str:
    """Return english text of floating point numbers.
    
    :param num: Input str or int
    """
    # Converitng the floaing point into string
    f = str(f)
    # Spliting the flaoting point number from the dot
    intiger_ , decimal_ = f.split('.')
    # Converting the integer part of the floating point into english text
    int_to_txt = str(int_to_en(intiger_))
    # Converting the decimal pa
    decimal_to_txt = num_to_en(decimal_)
    return int_to_txt + ' point ' + decimal_to_txt
    
    

# Replacing all the whole numbers inside string into English text

def int_to_text(text: str)-> str:
    """Return english text of floating point numbers.
    
    :param num: Input str or int
    """
    # Split the string into words
    words = text.split() 
    # Iterate over the words and replace any numbers with their text representation
    for i in range(len(words)):
        if words[i].isdigit():
            words[i] = int_to_en(words[i])
    
    # Rejoin the words into a string and return it
    return ' '.join(words)



# Replacing all the positive non interger numbers inside string into English text

def float_to_text(string: str)-> str:
    words = []
    for word in string.split():
        try:
            num = float(word)
            words.append(float_to_en(num))
        except ValueError:
            words.append(word)
    return ' '.join(words)



# Decontracting strings

def decontract_strings(string: str)-> str:
    # Doing for ' symbol
    # specific
    string = re.sub(r"won't", "will not", string)
    string = re.sub(r"can\'t", "can not", string)

    # general
    string = re.sub(r"n\'t", " not", string)
    string = re.sub(r"\'re", " are", string)
    string = re.sub(r"\'s", " is", string)
    string = re.sub(r"\'d", " would", string)
    string = re.sub(r"\'ll", " will", string)
    string = re.sub(r"\'t", " not", string)
    string = re.sub(r"\'ve", " have", string)
    string = re.sub(r"\'m", " am", string)
    
    # Doing similar for ’ symbol
    string = re.sub(r"won’t", "will not", string)
    string = re.sub(r"can\’t", "can not", string)

    # general
    string = re.sub(r"n\’t", " not", string)
    string = re.sub(r"\’re", " are", string)
    string = re.sub(r"\’s", " is", string)
    string = re.sub(r"\’d", " would", string)
    string = re.sub(r"\’ll", " will", string)
    string = re.sub(r"\’t", " not", string)
    string = re.sub(r"\’ve", " have", string)
    string = re.sub(r"\’m", " am", string)
    return string



# Emoji remover

def remove_emoji(string: str)-> str:
    """Cleanes emoji inside text.
    
    :param num: Input str
    """
    
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', str(string))


# Final Cleaning
def clean_text(text: str)-> str:
    """Cleanes every unnecessary special characters inside text.
    
    :param num: Input str
    """
    text = re.sub("'", "",text)
    text= re.sub('@[A-Za-z0-9]+','',text ) #removing mentions
    text= re.sub(r"[^a-zA-Z0-9]", " ", text) # Removing non letters
    text= re.sub("#",'',text) #removing #
    text= re.sub('RT[\s]+',' ',text) # removing Retexts
    text= re.sub('https?:\/\/\S+','',text) #removing links
    text= re.sub("[+%|):@(€¥£—•;=*]"," ",text)
    text= re.sub(r'[^\x00-\x7F]+',' ', text)
    text= re.sub('^\d+\s|\s\d+\s|\s\d+$',' ', text)
    return text



# Convering the texts into lowercase
def lowercase(text: str)-> str:
    """Convert the whole texts into lowercase.
    
    :param num: Input str
    """
    text= text.lower()
    return text


# Correcting spelling mistakes
autocorrect = Speller()




# Lematization
def lemmatize(text: str)-> str:
    """Lemmatize the input texts.
    
    :param num: Input str
    """
    words = text.split()
    words = [lemmatizer.lemmatize(word,pos='v') for word in words]
    return ' '.join(words)




# Removing Stop words

# List of words we dont want to remove from the list of stop words
list_of_words = []  # Add later

# Creating a custom list of stopwords
stopwords_ = set(stopwords.words('english'))
s = set(list_of_words)
custom_stopwords_ = list(stopwords_ - s)

def remove_sw(text: str)-> str:
    """Removes the stopwords.
    
    :param num: Input str
    """
    words = [word for word in text.split() if word.lower() not in custom_stopwords_]
    return " ".join(words)




 





def clean(text: str,  # pylint: disable=too-many-arguments, too-many-branches
          clean_all: bool = True,
          extra_spaces: bool = False,
          lemmatisation: bool = False,
          stopwords: bool = False,
          lowercase: bool = False,
          numbers: bool = False,
          punct: bool = False,
          reg: str = '',
          reg_replace: str = '',
          stp_lang: str = 'english') -> str:
    """Given a raw string, return cleaned text

    :param text: Input text to clean
    :param clean_all: Execute all cleaning operations
    :param extra_spaces: Remove extra white spaces
    :param lemmatisation: Lemmatized the words
    :param stopwords: Remove stop words
    :param lowercase: Convert to lowercase
    :param numbers: Remove all digits
    :param punct: Remove all punctuations
    :param reg: Regular expression for removing or replacing
    :param reg_replace: Replace the part with regular expression(reg)
    :param stp_lang: Language for stop words
    :return: Cleaned text
    """
    if clean_all is True:
        active_actions = [k for k, v in locals().items() if k != 'clean_all' and v is True]
        if len(active_actions) > 0:
            clean_all = False

    try:
        stop_words = stopwords.words(stp_lang)
    except LookupError:
        nltk.download('stopwords')
    finally:
        stop_words = stopwords.words(stp_lang)

    if not text:
        raise CleanTextEmptyString("No text is provided to clean")

    if reg != '':
        text = re.sub(reg, reg_replace, text)

    if clean_all:
        while '  ' in text.strip():
            text = text.replace("  ", " ")
        text = "".join([word.casefold() for word in text
                        if word not in string.punctuation])
        text = "".join([_ for _ in text if not _.isdigit()])
        tokens = text.split()
        text = " ".join([ps.stem(word) for word in tokens
                         if word not in stop_words])
        return text.strip()

    if extra_spaces:
        while '  ' in text.strip():
            text = text.replace("  ", " ")
    if lowercase:
        text = text.casefold()
    if numbers:
        text = "".join([_ for _ in text if not _.isdigit()])
    if punct:
        text = "".join([word for word in text
                        if word not in string.punctuation])

    if lemmatisation:
        text = text.split()
        text = " ".join([lemmatizer.lemmatize(word,pos='v') for word in text])



    if stopwords:
        text = text.split()
        text = " ".join([word for word in text if word not in stop_words])


    return text.strip()


def clean_l(text: str,  # pylint: disable=too-many-arguments
                clean_all: bool = True,
                extra_spaces: bool = False,
                stemming: bool = False,
                stopwords: bool = False,
                lowercase: bool = False,
                numbers: bool = False,
                punct: bool = False,
                reg: str = '',
                reg_replace: str = '',
                stp_lang: str = 'english') -> list:
    """Given a raw string, return list of clean words

    :param text: Input text to clean
    :param clean_all: Execute all cleaning operations
    :param extra_spaces: Remove extra white spaces
    :param stemming: Stem the words
    :param stopwords: Remove stop words
    :param lowercase: Convert to lowercase
    :param numbers: Remove all digits
    :param punct: Remove all punctuations
    :param reg: Regular expression for removing or replacing
    :param reg_replace: Replace the part with regular expression(reg)
    :param stp_lang: Language for stop words
    """
    text = clean(text, clean_all, extra_spaces, lemmatisation, stopwords, lowercase,
                 numbers, punct, reg, reg_replace, stp_lang)

    return text.split()
