""" Contains default values for new Website.Website instances
"""
with open('screen_default.css') as input_f:
    default_css_screen = input_f.read()

with open('default_template.html') as input_f:
    default_html_template = input_f.read()

default = {
    # template information
    'html_template': default_html_template,
    
    # hyperlink properties
    'link_code': "<a href=\"{link_to}\">{shown_text}</a>",
    'expand_relative': False, # don't expand relative links

    # headers and footers
    'head_title': "{title} :: Test Webpage",
    'page_title': "<h1 style='page_heading'>{title}</h1>",
    'page_footer': "{title} (c) Robert Layton, 2010",
    
    # navigation link properties
    'nav_code': "<ul>\n\t{nav_elements}\n</ul>",
    'nav_element': "<li>{nav_link}</li>",
    
    # css file and linking properties
    "cssfile_screen_filename": "basic_style.css",
    "cssfile_print_filename": "basic_style.css",
    "cssfile_print_link": "<link rel=\"stylesheet\" href=\"{cssfile_filename}\" type=\"text/css\" media=\"{media}\" />",
    "cssfile_screen_link": "<link rel=\"stylesheet\" href=\"{cssfile_filename}\" type=\"text/css\" media=\"{media}\" />",

    # css screen file
    "css_screen_default": default_css_screen,
    }
