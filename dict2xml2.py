#!/usr/bin/env python
# Amended from https://github.com/quandyfactory/dict2xml/blob/master/dict2xml.py
# coding: utf-8

"""
Converts a native Python dictionary into an XML string. Supports int, float, str, unicode, list, dict and arbitrary nesting.
"""
debug = False

def debug_notify(*args):
    """Prints debug information"""
    if debug == False: 
        return
    for arg in args:
        print '%s; ' % (arg)
    print '\n'

def xml_escape(s):
    if type(s) == str:
        s = s.replace('"',  '&quot;')
        s = s.replace('\'', '&apos;')
        s = s.replace('<',  '&lt;')
        s = s.replace('>',  '&gt;')
        s = s.replace('&',  '&amp;')
    elif type(s) == unicode:
        s = s.replace(u'"',  u'&quot;')
        s = s.replace(u'\'', u'&apos;')
        s = s.replace(u'<',  u'&lt;')
        s = s.replace(u'>',  u'&gt;')
        s = s.replace(u'&',  u'&amp;')
    return s

def convert(obj,attribs):
    """Routes the elements of an object to the right function to convert them based on their data type"""
    debug_notify('Inside convert(): obj=%s' % (obj))
    if type(obj) in (int, float, str, unicode):
        return convert_kv('item', obj,attribs)
    if hasattr(obj, 'isoformat'):
        return convert_kv('item', obj.isoformat(),attribs)
    if type(obj) == bool:
        return convert_bool('item', obj, attribs)
    if type(obj) == dict:
        return convert_dict(obj, attribs)
    if type(obj) == list:
        return convert_list(obj, attribs)
    if type(obj) == set:
        return convert_list([s for s in obj],attribs)
    raise TypeError, 'Unsupported data type: %s (%s)' % (obj, type(obj).__name__)

def convert_dict(obj,attribs):
    """Converts a dict into an XML string."""
    debug_notify('Inside convert_dict(): obj=%s' % (obj))
    output = []
    addline = output.append
    for k, v in obj.items():
        debug_notify('Looping inside convert_dict(): k=%s, v=%s, type(v)=%s' % (k, v, type(v)))
        try:
            if k.isdigit():
                k = 'n%s' % (k)
        except:
            if type(k) in (int, float):
                k = 'n%s' % (k)
        if type(v) in (int, float, str, unicode):
            addline(convert_kv(k, v, attribs))
        elif hasattr(v, 'isoformat'): # datetime
            addline(convert_kv(k, v.isoformat(), attribs))
        elif type(v) == bool:
            addline(convert_bool(k, v, attribs))
        elif type(v) == dict:
            addline('<%s>%s</%s>' % (k, convert_dict(v, attribs), k))
        elif type(v) == list:
            addline('<%s>%s</%s>' % (k, convert_list(v, attribs), k))
        elif type(v) == set: # convert a set into a list
            addline('<%s>%s</%s>' % (k, convert_list([s for s in v], attribs), k))
        elif v is None:
            addline('<%s></%s>' % (k, k))
        else:
            raise TypeError, 'Unsupported data type: %s (%s)' % (v, type(v).__name__)
    return ''.join(output)

def convert_list(items,attribs):
    """Converts a list into an XML string."""
    debug_notify('Inside convert_list(): items=%s' % (items))
    output = []
    addline = output.append
    for item in items:
        debug_notify('Looping inside convert_list(): item=%s, type(item)=%s' % (item, type(item)))
        if type(item) in (int, float, str, unicode):
            addline(convert_kv('item', item, attribs))
        elif hasattr(item, 'isoformat'): # datetime
            addline(convert_kv('item', v.isoformat(), attribs))
        elif type(item) == bool:
            addline(convert_bool('item', item, attribs))
        elif type(item) == dict:
            addline('<item>%s</item>' % (convert_dict(item, attribs)))
        elif type(item) == list:
            addline('<item>%s</item>' % (convert_list(item, attribs)))
        elif type(item) == set: # convert a set into a list
            addline('<item>%s</item>' % (convert_list([s for s in item], attribs)))
        else:
            raise TypeError, 'Unsupported data type: %s (%s)' % (item, type(item).__name__)
    return ''.join(output)

def convert_kv(k, v, attribs):
    """Converts an int, float or string into an XML element"""
    debug_notify('Inside convert_kv(): k=%s, v=%s' % (k, v))
    if attribs == True:
      return '<%s type="%s">%s</%s>' % (k, type(v).__name__ if type(v).__name__ != 'unicode' else 'str', xml_escape(v), k)
    else:
      return '<%s%s>%s</%s>' % (k, '' if type(v).__name__ != '' else '', xml_escape(v), k)


def convert_bool(k, v, attribs):
    """Converts a boolean into an XML element"""
    debug_notify('Inside convert_bool(): k=%s, v=%s' % (k, v))
    
    if attribs == True:
      return '<%s type="bool">%s</%s>' % (k, str(v).lower(), k)
    else:
      return '<%s>%s</%s>' % (k, str(v).lower(), k)
    

def dict2xml2(obj, root=True, attribs=True):
    """Converts a python object into XML"""
    debug_notify('Inside dict2xml(): obj=%s' % (obj))
    output = []
    addline = output.append
    if root == True:
        addline('<?xml version="1.0" encoding="UTF-8" ?>')
        addline('<root>%s</root>' % (convert(obj,attribs)))
    else:
        addline(convert(obj,attribs))
    return ''.join(output)
    
