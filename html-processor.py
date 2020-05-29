import re


def remove_tags(m):
    if m.group(1)[:6] == 'script' or m.group(1)[:5] == 'style':  # if it works it aint stupid
        return ' '
    else:
        return m.group(0)


def replace_special(m):
    if m.group(0) == '&amp;':
        return '&'
    elif m.group(0) == '&gt;':
        return '>'
    elif m.group(0) == '&lt;':
        return '<'
    elif m.group(0) == '&nbsp;':
        return ' '


text = open('text', 'r').read()
tag = re.compile(r'<.+?>', re.DOTALL)

# remove the title tags and export the title
titleRexp = re.compile(r'<title>.+?</title>')
title = re.findall(titleRexp, text)
print(tag.sub(' ', title[0]))

# remove all them comments
comments = re.compile('<!--.+?-->', re.DOTALL)
text = comments.sub(' ', text)

# remove script and style tags
fullTag = re.compile(r'<.+?>.+?</(.+?)>', re.DOTALL)
text = fullTag.sub(remove_tags, text)

# extract the links and the text from the anchor tags
anchorTag = re.compile(r'<a.+?>.+?</a>')
anchors = anchorTag.findall(text)  # list of all anchor tags
href = re.compile('href="(.+?)"')
for anchor in anchors:
    link = re.search(href, anchor).group(1)  # links
    print(link, end=' ')
    anchor = tag.sub(' ', anchor)  # get rid of all the tags in the anchor
    print(anchor)  # print the remaining text, if any

# remove all the tags
text = tag.sub(' ', text)

# replace the special html characters with regular ones
special = re.compile('&.+?;')
text = special.sub(replace_special, text)

# remove all the whitespaces
text = re.compile(r'\s+').sub(' ', text)


print(text)
