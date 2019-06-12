vim:fileencoding=utf-8:ts=2:sw=2:expandtab

# HSDEC Function

'HSDEC(text)'

Decodes HTML special characters from an input of an HTML string.

**Behavior**

- 'None' will be passed through unaffected
- Unescapes any other Special Characters
- Returns unescaped character as a string

------meta------

Topic: "HSDEC Function"
Category: "Utility Functions"
Category: "Web Functions"

# QA Function

'QA(text)'

Places quotes around Attributes

**Behavior**

- Turns attributes into strings by placing quotes around it
- Turns false attributes into an empty string ('')

------meta------

Topic: "QA Function"
Category: "Utility Functions"
Category: "Web Functions"

# UE Function

'UE(URL)'

Encodes parts of a URL

**Behavior**

- Turns URLs into strings
- Turns false URLs into an empty string ('')

------meta------

Topic: "UE Function"
Category: "Utility Functions"
Category: "Web Functions"

# UD Function

'UD(URL)'

Places quotes around Attributes

**Behavior**

- Turns URLs into strings
- Turns false URLs into an empty string ('')

------meta------

Topic: "UD Function"
Category: "Utility Functions"
Category: "Web Functions"

#  ML Function

'ML(URL, list of two tuples, _ReplaceScriptPath=None, _ReplaceScriptPath=None, **text)'

Creates a link out of a given URL

**Behavior**

- Creates a link from a URL input
- Filters out keys using the **kwargs argument, and appends them to the end

------meta------

Topic: "ML Function"
Category: "Utility Functions"
Category: "Web Functions"

#  JN Function

'JN(iterator, func=None'

Joins a group of iterators and a lambda together into a string

**Behavior**

- Joins a group of iterators from the argument together
- Joins the iterators and a lambda (func) if that is given as well


------meta------

Topic: "JN Function"
Category: "Utility Functions"
Category: "Web Functions"

#  DELIM Function

'DELIM(iterator, delimiter=',', default=None)'

Places a delimiter (comma as default) between every iterator in the group

**Behavior**

- Places a delimiter between each iterator
- Returns None is the iterator is None

------meta------

Topic: "DELIM Function"
Category: "Utility Functions"
Category: "Web Functions"

#  WRAPIF Function

'WRAPIF(start, content, end)'

Combines the start, content, and end arguments

**Behavior**

- Combines and returns the three arguments
- Returns an empty string is content is empty

------meta------

Topic: "WRAPIF Function"
Category: "Utility Functions"
Category: "Web Functions"

#  BR Function

'BR(text)'

Replaces the new line operator '\n', with an HTML friendly <br />.

**Behavior**

- Finds the first occurence of '\n' in a given text
- Replaces the found occurence of '\n' with <br />

------meta------

Topic: "BR Function"
Category: "Utility Functions"
Category: "Web Functions"

#  HS_BR Function

'HS_BR(text, OrElseHTML='', OrElse='')'

Replaces the new line operator '\n', with an HTML friendly <br />, can work with Special HTML characters.

**Behavior**

- Turns all HTML special characters into strings
- Finds all occurences of '\n' in a given text
- Replaces the found occurence of '\n' with <br />

------meta------

Topic: "HS_BR Function"
Category: "Utility Functions"
Category: "Web Functions"

#  HS_Wrap Function

'HS_Wrap(start, iterator, end, OrElseHTML='', OrElse='')'

- Creates a string that contains the start and end arguements, and a v variable, which is sent through an iterator using v as the index.
- Continually adds to the string untill the v variable fully goes through the iterator argument

**Behavior**

- Creates a string that is made up of an empty string followed by the start argument, then the current version of the v variable that is run through the HS() function, then the end argument.
- Will repeat the above command and add to the string untill the v variable reaches the end of the iterator

------meta------

Topic: "HS_Wrap Function"
Category: "Utility Functions"
Category: "Web Functions"

#  HS_Join Function

'HS_Join(delimiter, iterator, OrElseHTML='', OrElse='')'

- Creates a string that contains a delimiter character and a v variable
- Continually adds to the string untill the v variable fully goes through the iterator argument

**Behavior**

- Creates a string using the delimeter argument and the v variable run through HS()
- Repeats untill the v has passed through the iterator argument

------meta------

Topic: "HS_Join Function"
Category: "Utility Functions"
Category: "Web Functions"

#  HS_Tag Function

'HS_Tag(tagname, content=None, **args)'

- Forces all attributes into the lower case

**Behavior**

- Creates a tag using the tagname and args arguments

------meta------

Topic: "HS_Tag Function"
Category: "Utility Functions"
Category: "Web Functions"

#  HS_A Function

'HS_A(href, label, **args)'

- Forces all attributes into the lower case

**Behavior**

- Creates a tag using the tagname and args arguments

------meta------

Topic: "HS_A Function"
Category: "Utility Functions"
Category: "Web Functions"
