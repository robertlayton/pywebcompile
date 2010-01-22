""" Methods for compiling templates into finished versions

    Currently has a script method, so don't include yet!
"""
import re, os
from Contents import Contents

br_pattern = re.compile("{[\w]+}")

def compileAll(contents, website, output_directory="."):
    """ Compiles the entire website, including css files
    """
    for content in contents:
        filename = os.path.join(output_directory, content.filename)
        with open(filename, 'w') as output_f:
            compileHTML(content, website, output_f)
    # output the css file
    filename = os.path.join(output_directory, website['cssfile_screen_filename'])
    with open(filename, 'w') as output_f:
        output_f.write(website["css_screen_default"])

def compileHTML(content, website, output_f):
    """ Compiles a template with the given content and website properties
    """
    template = website['html_template']
    output_f.write(compileProperty(template, content, website))


def compileProperty(value, content, website):
    if not isinstance(value, basestring):
        return value
    matches = br_pattern.findall(value)
    for match in matches:
        key = match[1:-1] # "{document}" --> "document"
        p = None
        # try find the key in contents, then in website
        try:
            p = content[key]
        except KeyError:
            try:
                p = website[key]
            except KeyError:
                # not found: just leave the text as it is
                continue
        if p is not None:
            p = compileProperty(p, content, website)
            value = value.replace(match, p)
        
    return value
