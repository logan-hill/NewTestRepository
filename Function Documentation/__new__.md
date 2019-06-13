vim:fileencoding=utf-8:ts=2:sw=2:expandtab

#  __new__ Function of BL Class

'__new__(s)'

- Cleans an HTML Fragment to escape anything that is not listed as allowed content

**Behavior**

- Checks though the ALLOWED_TAGS, ALLOWED_ATTRIBUTES, and ALLOWED_STYLES
- Escapes anything that is found that is not allowed

------meta------

Topic: "__new__ Function"
Category: "Utility Functions"
Category: "Web Functions"

---NOTE---

This function is called '__new__()' in the files, is it supposed to be called 'Clean()'?
