## dict2xml2

### Summary

The original library (http://github.com/quandyfactory/dict2xml/) Converts a native Python dictionary into an XML string. This is a hacky alteration to allow the library to generate invalid XML - Disgusting as this is, I needed it for a Git post-receive script

### Details

* Supports item (`int`, `float`, `bool`, `str`, `unicode`, `datetime`) and collection (`list`, `set` and `dict`) data types with arbitrary nesting for the collections. Datetime objects are converted to ISO format strings.

* The root object passed into the `dict2xml` function can be any of the following data types: `int`, `float`, `str`, `unicode`, `datetime`, `list`, `set`, `dict`.

* To satisfy XML syntax, by default it wraps all the dict keys/elements and values in a `<root> ... </root>` element. However, this can be disabled to create XML snippets.

* For lists of items, if each item is also a collection data type (`lists`, `dict`), the elements of that item are wrapped in a generic `<item> ... </item>` element.

* Elements with an item data type (`int`, `float`, `bool`, `str`, `datetime`, `unicode`) include a `type` attribute with the data type. Note: `datetime` data types are converted into ISO format strings, and `unicode` and `datetime` data types get a `str` attribute - This can be disabled thanks to my hacks

* Elements with an unsupported data type raise a TypeError exception.


### Installation

Download the tarballed installer - `dict2xml-[VERSION].tar.gz` - for this package from the [dist](https://github.com/bentasker/dict2xml2/tree/master/dist) directory and uncompress it. Then, from a terminal or command window, navigate into the unzipped folder and type the command:

    python setup.py install
    
That should be all you need to do.

### Usage

Once installed, import the library into your script and convert a dict into xml by running the `dict2xml` function:

    >>> import dict2xml2
    >>> xml = dict2xml2.dict2xml2(some_dict)

Alternately, you can import the `dict2xml()` function from the library.

    >>> from dict2xml2 import dict2xml2
    >>> xml = dict2xml2(some_dict)

That's it!

#### Debugging

You can also enable debugging information.

    >>> import dict2xml2
    >>> dict2xml2.debug = True # the console will print debug information for each function as it executes.  
    
    >>> xml = dict2xml2.dict2xml2(some_object)


### Author

* Author: Ben Tasker
* Email: dict2xml2@bentasker.co.uk
* Repository: [http://github.com/bentasker/dict2xml2](http://github.com/bentasker/dict2xml2)



### Copyright and Licence

Copyright 2013 Ben Tasker

(Largely) Based on work by Ryan  McGreal (c) 2012

Released under the GNU General Public Licence, Version 2:  
See LICENSE

