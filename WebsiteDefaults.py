""" Contains default values for new Website.Website instances
"""
with open('screen_default.css') as input_f:
    default_css_screen = input_f.read()

with open('default_template.html') as input_f:
    default_html_template = input_f.read()

defaults = {
    # website information
    "location": "/home/bob",
    "creator_name": "Robert Layton",
    "creation_date": "2010",
    
    # template information
    'html_template': default_html_template,
    
    # hyperlink properties
    'link_code': "<a href=\"{link_to}\">{shown_text}</a>",
    'expand_relative': False, # don't expand relative links

    # headers and footers
    'website_title': "Untitled Website!",
    'head_title': "{document_title} :: {website_title}",
    'page_title': "Untitled Document",
    'document_title': "<h1>{page_title}</h1>",
    'page_footer': "{page_title} (c) {creator_name}, {creation_date}",
    'head_declarations': "{css_declarations}\n{code_about}",
    'code_about': "<!-- Compilation Software by Robert Layton, 2010 (c) -->",
    
    # navigation link properties
    'nav_code': "Navigation code not set",
    
    # css file and linking properties
    "cssfile_screen_filename": "basic_style.css",
    "cssfile_print_filename": "basic_style.css",
    "cssfile_print_link": "<link rel=\"stylesheet\" href=\"{cssfile_print_filename}\" type=\"text/css\" media=\"print\" />",
    "cssfile_screen_link": "<link rel=\"stylesheet\" href=\"{cssfile_screen_filename}\" type=\"text/css\" media=\"screen\" />",
    "css_declarations": "\t{cssfile_screen_link}\n\t{cssfile_print_link}",
    # css screen file
    "css_screen_default": default_css_screen,

    # standard contents
    'introduction': "An introduction for the page will go here",
    'contents': "Content will go here",
    'sidebar': "Intersting side information will go here",
    }
