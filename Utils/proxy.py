import urllib2

def setProxy():
    """
    Works for urllib2
    Returns urllib2.OpenerDirector object
    
    Change proxies accordingly.
    
    Usage:
    >>> opener = setPrxoy()
    >>> urllib2.install_opener(opener)
    
    """
    proxy = {'http':'http://f2010059:j@10.1.9.36:8080',
                    'https':'https://f2010059:j@10.1.9.36:8080'}
    Proxy = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(Proxy)
    return opener
