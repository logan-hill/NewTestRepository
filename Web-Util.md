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

Places a delimiter (comma as default) between every iterator in the group

**Behavior**

- Places a delimiter between each iterator
- Returns None is the iterator is None

------meta------

Topic: "DELIM Function"
Category: "Utility Functions"
Category: "Web Functions"#  DELIM Function

'DELIM(iterator, delimiter=',', default=None)'

Places a delimiter (comma as default) between every iterator in the group

**Behavior**

- Places a delimiter between each iterator
- Returns None is the iterator is None

------meta------

Topic: "DELIM Function"
Category: "Utility Functions"
Category: "Web Functions"
