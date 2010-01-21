import re

br_pattern = re.compile("{{[\w]+}}")

def compileHTML(template, content, output_f):
    matches = br_pattern.findall(template)
    for match in matches:
        key = match[2:-2] # "{{document}}" --> "document"
        template = template.replace(match, content[key])
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
