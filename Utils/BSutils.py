from BeautifulSoup import BeautifulSoup

def getPrintUnicode(soup):
    """
    Requires BeautifulSoup
    
    >>> soup = BeautifulSoup('<a href="https://github.com/jayrambhia" class="name">jayrambhia</a>')
    >>> print getPrintUnicode(soup)
    u'jayrambhia'
    
    Input must be BeautifulSoup.BeautifulSoup object
    """
    
    body=''
    if isinstance(soup, unicode):
        soup = soup.replace('&#39;',"'")
        soup = soup.replace('&quot;','"')
        soup = soup.replace('&nbsp;',' ')
        soup = soup.replace('&gt;','>')
        soup = soup.replace('&lt;','<')
        body = body + soup
    else:
        if not soup.contents:
            return ''
        con_list = soup.contents
        for con in con_list:
            body = body + getPrintUnicode(con)
    return body

    
