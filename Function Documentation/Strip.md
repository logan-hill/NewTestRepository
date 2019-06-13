vim:fileencoding=utf-8:ts=2:sw=2:expandtab

#  Strip Function of BL Class

'Strip(s)'

- Cleans an HTML Fragment to remove anything that is not listed as allowed content

**Behavior**

- Checks though the ALLOWED_TAGS, ALLOWED_ATTRIBUTES, and ALLOWED_STYLES
- Removes anything that is found that is not allowed
 - As opposed to the function __new__ which just escapes unallowed content

------meta------

Topic: "Strip Function"
Category: "Utility Functions"
Category: "Web Functions"
