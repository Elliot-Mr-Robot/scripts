import sys,argparse
if sys.version[0] in '2':
   print('\n[x] Not Supported For python 2.x Please Use Python 3.x \n')
   exit()

try:
    import mechanicalsoup
    import requests
except Exception as e:
    print('\n{}[-]{} mechanicalsoup package Not Installed\n'.format(_.R,_.W))
    print('type pip3 install mechanicalsoup')
    exit()

from lib.lib import Parser

urls = []

class crawl(object):

      auth = {
        1:[
            'https://www.google.com',
            'class="r"><a href="/url\?q=(.*?)&amp',
            'fl'
        ],
        2:[
            'https://www.bing.com',
            'h=".*?" href="(h.*?")',
            "b_widePag sb_bp"
        ]
      }

      def __init__(
        self,
        dork,
        proxy = None
      ):
          self.dork = dork
          self.proxy = proxy

      def Bing(self):
          bing = Parser(
            self.dork,
            crawl.auth[2][0],
            crawl.auth[2][1],
            crawl.auth[2][2],
            proxy = self.proxy
          )
          bing.request()
          for url in dir(bing):
              if 'go.microsoft.com' in url or 'bing.com' in url:
                  pass
              else:
                  urls.append(url)

      def Google(self):
          google = Parser(
            self.dork,
            crawl.auth[1][0],
            crawl.auth[1][1],
            crawl.auth[1][2],
            proxy = self.proxy
          )
          google.request()
          for url in dir(google):
              if 'go.microsoft.com' in url or 'bing.com' in url:
                 pass
              else:
                 urls.append(url)
