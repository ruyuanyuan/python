from urllib import request

class HtmlDownloder(object):

    def download(self,url):
        if url is None:
            return None
        req = request.Request(url)
        response = request.urlopen(req)

        if response.getcode() != 200:
            return None
        return response.read().decode('utf-8')
