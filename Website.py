""" This class returns HTML objects in a consistent format

    Usage is usually like:
    website = Website(**properties)
    print website.link("Shown text", "http://www.google.com", **args)

    The purpose of this class is to return HTML objects in a way that is consistent
    for an entire website, to enable things like standard lists, etc.
    Things like relative links can be expanded easily as well, if the user wishes.
"""
import os

from WebsiteDefaults import defaults

class Website(object):
    """ Contains information about the website and returns consistent HTML Objects
    """
    def __init__(self, **args):
        self.properties = args


    def get(self, name):
        """ Checks if the property with the given name is set, if not, use default
        """
        global defaults
        if name in self.properties.keys():
            return self.properties[name]
        else:
            return defaults[name]
        
    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.properties[key] = value
        
    def hyperlink(self, shown_text, link_to, **args):
        """ Returns a hyperlink (<a> tag) according to website's settings
        """
        # fix hyperlink if settings are set
        link_to = self.updateLink(link_to)
        link_code = self.get('link_code')
        return link_code.format(link_to=link_to,
                                shown_text=shown_text, **args)
    
    def updateLink(self, link):
        """ Updates the link, if any parameters are set that do so

            Parameters used:
            - extend_relative: changes relative links into absolute links
        """
        if self.get('expand_relative') and isRelative(link):
            return os.path.join(self.properties['absolute_path'], link)
        return link


    def navigation(self, links):
        """ Returns the navigation of the website
        """
        nav_code = self.get('nav_code')
        nav_element = self.get('nav_element')
        all_nav_elements = [nav_element.format(nav_link=self.hyperlink(l[0], l[1]))
                            for l in links]
        return nav_code.format(nav_elements="\n\t".join(all_nav_elements))


    def getCSS(self, media="screen"):
        return self.get("css_%s_default" % media)


    def websiteTitle(self, custom_text=""):
        """ Title of website (within <head> tag)
        """
        return self.get('head_title').format(title=custom_text)

    
    def pageTitle(self, custom_text=""):
        """ Title of webpage (within <body> tag)
        """
        return self.get('page_title').format(title=custom_text)


    def getTemplate(self):
        """ Returns the template used by the site
        """
        return self.get('html_template')


    def pageFooter(self, custom_text=""):
        """ Title of webpage (within <body> tag)
        """
        return self.get('page_footer').format(title=custom_text)


    def cssLink(self, media='screen'):
        css_code = self.get("cssfile_%s" % media)
        cssfile_filename = self.get("cssfile_%s_filename" % media)
        return css_code.format(media=media, cssfile_filename=cssfile_filename)



def isRelative(link):
    raise NotImplementedError("Website.isRelative has not been implemented yet")
