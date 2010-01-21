""" This class returns HTML objects in a consistent format

    Usage is usually like:
    website = Website(**arguments)
    print website.link("Shown text", "http://www.google.com", **args)

    The purpose of this class is to return HTML objects in a way that is consistent
    for an entire website, to enable things like standard lists, etc.
    Things like relative links can be expanded easily as well, if the user wishes.
"""
import os

class Website(object):
    """ Contains information about the website and returns consistent HTML Objects
    """
    def __init__(self, **args):
        self.arguments = args

    def get(self, name, default):
        if name in self.arguments.keys():
            return self.arguments[name]
        else:
            return default
        
    def hyperlink(self, shown_text, link_to, **args):
        """ Returns a hyperlink (<a> tag) according to website's settings
        """
        # fix hyperlink if settings are set
        link_to = self.updateLink(link_to)
        link_code = self.get('link_code', "<a href=\"{link_to}\">{shown_text}</a>")
        return link_code.format(link_to=link_to,
                                shown_text=shown_text, **args)
    
    def updateLink(self, link):
        """ Updates the link, if any parameters are set that do so

            Parameters used:
            - extend_relative: changes relative links into absolute links
        """
        if 'extend_relative' in self.arguments and isRelative(link):
            return os.path.join(self.arguments['absolute_path'], link)
        return link

    def navigation(self, links):
        """ Returns the navigation of the website
        """
        nav_code = self.get('nav_code', "<ul>{nav_elements}</ul>")
        nav_element = self.get('nav_element', "<li>{nav_link}</li>")
        all_nav_elements = [nav_element.format(nav_link=self.hyperlink(l[0], l[1]))
                            for l in links]
        return nav_code.format(nav_elements="\n\t".join(all_nav_elements))

    def outputCSS(self):
        css = ""
        for key, value in self.arguments.items():
            if key.startswith("css_"):
                css += value
        return css
