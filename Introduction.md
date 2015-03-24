# Introduction #

pywebcompile looks to do the heavy lifting of creating dynamically updated webpages _offline_, by first compiling them as much as possible before making them live.
This could then be served by any framework, such as Django, and the final results could still contain dynamic code, or they may not. The aim is to remove as much as possible, this heavy lifting.


# Details #

An example of this is a blog. For each blog webpage view, a framework must load the content of the blog, calculate the sidebar information (such as archive links) and load the comments.
Using this framework, when a new blog entry is created, the website is compiled and only static pages are found. The current exception is the comments, which could be served using AJAX in real time, delivered by a server optimised for delivering those comments, or added using a different framework. The benefit here is that compilation has reduced the number and size of the database hits, meaning that more website serving can be done with less hardware.

# How can I help? #

The project is in really early stages right now, and I can use all the help I can get.
To start, file an issue with a request for a feature or a bug, and if possible, include a patch or some code.
If I see a user contributing good code a few times, I'll ask them if they want access to write directly onto the svn.
This will happen until the project is up to about version 0.1 to 0.2, at which point I'll be a little more careful about giving access to new people.