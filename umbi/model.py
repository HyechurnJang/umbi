# -*- coding: utf-8 -*-
'''
Created on 2017. 9. 27.
@author: HyechurnJang
'''

# https://cisco.jiveon.com/docs/DOC-1852312

import requests
from jzlib import Inventory

class UmbiAPI(Inventory):
    
    class Domains(Inventory): # Domain Status And Categorization
        def Categorization(self, *names): return (~self).post('/domains/categorization?showLabels', names)
        def Categories(self): return (~self).get('/domains/categories')
        def Score(self, *names): return (~self).post('/domains/score/', names)
        def LatestTags(self, name): return (~self).get('/domains/%s/latest_tags' % (~self).__encode_url__(name))
    
    class Timeline(Inventory): # Timeline
        def __call__(self, name): return (~self).get('/timeline/%s' % (~self).__encode_url__(name))
    
    class URL(Inventory): # Classifiers
        def Classifiers(self, name): return (~self).get('/url/%s/classifiers' % (~self).__encode_url__(name))
        def Info(self, name): return (~self).get('/url/%s/info' % (~self).__encode_url__(name))
    
    class Search(Inventory): # Pattern Search
        def __call__(self, expr, start, category=False): return (~self).get('/search/%s?start=%s&includecategory=true' % (expr, start) if category else '/search/%s?start=%s' % (expr, start))
    
    class Recommendations(Inventory): # Co-Occurrences For A Domain
        def Name(self, name): return (~self).get('/recommendations/name/%s.json' % (~self).__encode_url__(name))
    
    class Links(Inventory): # Related Domains For A Domain
        def Name(self, name): return (~self).get('/links/name/%s.json' % (~self).__encode_url__(name))
    
    class Security(Inventory): # Security Information For A Domain
        def Name(self, name): return (~self).get('/security/name/%s.json' % (~self).__encode_url__(name))
    
    class DnsDB(Inventory): # DNS RR Historay
        def Name(self, name): return (~self).get('/dnsdb/name/a/%s.json' % (~self).__encode_url__(name))
        def IP(self, ip): return (~self).get('/dnsdb/ip/a/%s.json' % ip)
    
    class BgpRoutes(Inventory): # AS Information For A Domain
        def IP(self, ip): return (~self).get('/bgp_routes/ip/%s/as_for_ip.json' % ip)
        def ASN(self, asn): return (~self).get('/bgp_routes/asn/%d/prefixes_for_asn.json' % asn)
    
    class WhoIs(Inventory): # WHOIS Information For A Domain
        def __call__(self, name): return (~self).get('/whois/%s' % (~self).__encode_url__(name))
        def __options__(self, url, **opts):
            if 'limit' in opts: url += '&limit=%d' % opts['limit']
            if 'offset' in opts: url += '&offset=%d' % opts['offset']
            if 'sort' in opts: url += '&sort=%s' % opts['sort'] # created, updated, expired
            return url
        def Emails(self, *emails, **opts): return (~self).get(self.__options__('/whois/emails?emailList=%s' % ','.join(emails), **opts))
        def Nameservers(self, *nameservers, **opts): return (~self).get(self.__options__('/whois/nameservers?nameServerList=%s' % ','.join(nameservers), **opts))
    
    class IPs(Inventory): # Latest Malicious Domains For An IP
        def LatestDomains(self, ip): return (~self).get('/ips/%s/latest_domains' % ip)
    
    class TopMillion(Inventory): # Umbrella Popularity List (Top Million Domains)
        def __call__(self, limit=None): return (~self).get('/topmillion?limit=%d' % limit if limit else '/topmillion')
    
    class Samples(Inventory):
        def __call__(self, name, limit=None): return (~self).get('/samples/%s?limit=%d' % (name, limit) if limit else '/samples/%s' % name)
    
    def __init__(self, token):
        Inventory.__init__(self)
        self.url = 'https://investigate.api.umbrella.com'
        self.token = token
        self.headers = {'Authorization': 'Bearer ' + token}
    
    def __encode_url__(self, url):
        return url.replace('/', '%2F').replace(':', '%3A')
        
    def __inspect_status_code__(self, resp):
        code = resp.status_code
        if code == 200: return resp.json()
        elif code == 204: return None
        elif code == 400: raise Exception("Likely missing a required parameter or malformed JSON. Please check the syntax on your query.")
        elif code == 403: raise Exception("Request had Authorization header but token was missing or invalid. Please ensure your API token is valid.")
        elif code == 404: raise Exception("The requested item doesn't exist, check the syntax of your query or ensure the IP and/or domain are valid.")
        elif code in [500, 502, 503, 504]: raise Exception('Something went wrong on our end.')
        else: raise Exception('Unkown Error')
    
    def get(self, url): return self.__inspect_status_code__(requests.get(self.url + url, headers=self.headers))
    
    def post(self, url, data): return self.__inspect_status_code__(requests.post(self.url + url, headers=self.headers, json=data))

