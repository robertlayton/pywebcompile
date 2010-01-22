""" Methods for compiling templates into finished versions

    Currently has a script method, so don't include yet!
"""
import re, os

br_pattern = re.compile("{{[\w]+}}")

def compileAll(contents, website, output_directory="."):
    for content in contents:
        try:
            filename = os.path.join(output_directory, content.filename)
            with open(filename, 'w') as output_f:
                compileHTML(content, website, output_f)
        except Exception, e:
            print e
            print "Skipping %s" % content.filename
    

def compileHTML(content, website, output_f):
    """ Compiles a template with the given content
    """
    template = website.html_template
    matches = br_pattern.findall(template)
    for match in matches:
        key = match[2:-2] # "{{document}}" --> "document"
        if key in content:
            template = template.replace(match, content[key])
        elif key in website:
            template = template.replace(match, website[key])
    output_f.write(template)
