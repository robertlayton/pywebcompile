from Contents import Contents
from Compile import compileAll
from Website import Website



website = Website()
website['website_title'] = "Test Compilation Website"


home_page = Contents("index.html")
home_page['document_title'] = "Home page"
home_page['introduction'] = "This is the introduction for the home page, located at index.html"
home_page['contents'] = "Some contents will go here for the homepage, such as the latest updates"
home_page['contents'] = "Isn't compilation nice?"


another_page = Contents("page2.html")
another_page['document_title'] = "Another page"
another_page['introduction'] = "The 'another page' is introduced here."
another_page['contents'] = "Another page will contain moreinformation"
another_page['contents'] = "Isn't compilation really nice?"


contents = [home_page, another_page]


compileAll(contents, website, output_directory="compiled")
