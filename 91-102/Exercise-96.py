# The Stack class has been implemented.

# HTML is the standard markup language for documents designed to be displayed in a web browser. Web browsers receive HTML documents from a web server or from local storage and render the documents into multimedia web pages.

# In an HTML document, elements are separated by HTML tags. A simple opening HTML tag has the form <name> and the corresponding closing tag is </name>. For example, the opening <body> tag and the matching </body> tag. Other commonly used HTML tags:

#     <body>

#     <h1>, <h2>, ...

#     <center>

#     <p>

#     <ol>

#     <li>

#     <ul>

# Tags usually go in pairs. An opening tag begins a section of page content, and a closing tag ends it. For example, to markup a section of text as a paragraph, you would open the paragraph with an opening paragraph tag <p> and close it with a closing paragraph tag </p> (closing tags always proceed the element with a /).

# A few tags are called non-container tags, because they don't contain any content. Examples are images and line breaks, for example <img>.

# In this exercise, we only consider the tags that need to be closed.


# HTML file example:


#     <html>
#     <head>
#         <title>Title</title>
#     </head>
#     <body>
#         <h1>This is my first page.</h1>
#         <p>Welcome to my blog.</p>
#     </body>
#     </html>


# Implement a function called is_valid_html() that checks if the HTML document (in the form of a str object) is valid for the number of open and closed HTML tags.

# The function returns the boolean value True if the HTML document is valid, on the contrary False. The function takes one argument.

# When implementing is_valid_html() function, think about how you can solve this problem using the stack. For this purpose, use the Stack class.


# Example:


#     html_template = """<html>
#     <head>
#         <title>Title</title>
#     </head>
#     <body>
#         <h1>This is my first page.</h1>
#         <p>Welcome to my blog.</p>
#     </body>
#     </html>"""


#     [IN]: is_valid_html(html_template)
#     [OUT]: True


# You just need to implement the is_valid_html() function. 


class EmptyStackError(Exception):
    pass
    
    
class Stack:
    """The simplest stack."""
    
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def push(self, item):
        self._data.append(item)
    
    def pop(self):
        if self.is_empty():
            raise EmptyStackError('The stack is empty.')
        return self._data.pop()
    
    def is_empty(self):
        return len(self._data) == 0
    
    def top(self):
        if self.is_empty():
            raise EmptyStackError('The stack is empty.')
        return self._data[-1]
    
    
def is_valid_html(html):
    stack = Stack()
    first_char_idx = html.find('<')
    while first_char_idx != -1:
        next_char_idx = html.find('>', first_char_idx + 1)
        if next_char_idx == -1:
            return False
        tag = html[first_char_idx + 1: next_char_idx]
        if not tag.startswith('/'):
            stack.push(tag)
        else:
            if stack.is_empty():
                return False
            if tag[1:] != stack.pop():
                return False
        first_char_idx = html.find('<', next_char_idx + 1)
    return stack.is_empty()