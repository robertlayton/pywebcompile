""" Methods for compiling templates into finished versions

    Currently has a script method, so don't include yet!
"""
import re, os

br_pattern = re.compile("{{[\w]+}}")

def compileAll(template, contents, website, output_directory="."):
    for content in contents:
        try:
            filename = os.path.join(output_directory, content.filename)
            with open(filename, 'w') as output_f:
                compileHTML(template, content, website, output_f)
        except Exception, e:
            print e
            print "Skipping %s" % content.filename
    

def compileHTML(template, content, website, output_f):
    """ Compiles a template with the given content
    """
    matches = br_pattern.findall(template)
    for match in matches:
        key = match[2:-2] # "{{document}}" --> "document"
        if key in content:
            template = template.replace(match, content[key])
        elif key in website:
            template = template.replace(match, website[key])
    output_f.write(template)



test_content = {
    "webpage_title": "First compilation!",
    "head_declarations": "<link rel=\"stylesheet\" href=\"basic_style.css\" type=\"text/css\" media=\"screen\" />",
    "document_title": "First testing compilation",
    "navigation": "links here",
    "introduction": "sample introduction",
    "content": "content goes here",
    "sidebar": "this is an aside",
    "footer": "Copyright (c) Robert Layton",
    }

with open("compiled/test.html", 'w') as output_f:
    with open("template.html", 'r') as template_f:
        compileHTML(template_f.read(), test_content, output_f)
