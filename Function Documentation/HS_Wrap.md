vim:fileencoding=utf-8:ts=2:sw=2:expandtab

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
