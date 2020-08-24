import re

def match_strong(text: str) -> str:
    ## inline, so anything around __xxx__
    return re.sub(r'__(.+?)__', r'<strong>\1</strong>', text)

def match_em(text: str) -> str:
    ## inline, so anything around _xxx_
    return re.sub(r'_(.+?)_', r'<em>\1</em>', text)

def match_li(text: str) -> str:
    # line item, break line matters = re.MULTILINE
    return re.sub(r'^\* (.+?$)', r'<li>\1</li>', text, flags=re.MULTILINE)

def match_header(text: str) -> str:
    # from h1 to h7, break line matters = re.MULTILINE
    for i in range(1, 7):
        text = re.sub(r'^{} (.*?$)'.format('#' * i), r'<h{0}>\1</h{0}>'.format(i), text, flags=re.MULTILINE)
    return text

def match_list_group(text: str) -> str:
    # engulfs li in ul for the entire text = re.DOTALL (grabs newlines)
    # it can fail if multiple lists
    return re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', text, flags=re.DOTALL)

def match_paragraph(text: str) -> str:
    # every line - EXCEPT line/block elements - is a paragraph, so re.MULTILINE
    # not starts with <h?>, <li>, <ul>, so ?! = negation for the group
    return re.sub(r'^(?!<[hlu])(.*?$)', r'<p>\1</p>', text, flags=re.MULTILINE)

def parse(markdown: str) -> str:
    html = markdown

    # inline elements, order matters, precedence
    html = match_strong(html)
    html = match_em(html)

    # line elements
    html = match_li(html)
    html = match_header(html)

    # block elements
    html = match_list_group(html)
    html = match_paragraph(html)
    html = html.replace('\n', '')

    return html
