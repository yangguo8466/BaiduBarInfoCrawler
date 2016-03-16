#-*-coding:utf8-*-

from lxml import etree

class Analysiser(object):
    def __init__(self,html):
        self.selector = etree.HTML(html)

    def readXpath(self,xpath):
        """ Return the value of xpath in the html text """
        value = self.selector.xpath(xpath)
        return value

    def getDatas(self, xpath_dicts):
        """Returt collections of dictionary"""
        datas = {}
        for section in xpath_dicts:
            item = {}
            items = xpath_dicts[section]
            for key in items:
                item[key] = self.readXpath(items[key]+"")
            datas[section] = item
        return datas