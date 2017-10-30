# -*- coding: utf-8 -*-
'''
Created on 2017. 10. 12.
@author: HyechurnJang
'''

import json
from umbi import UmbiAPI

def v(data):
    print json.dumps(data, indent=2)

api = UmbiAPI('85aaa4d3-333e-4212-a7bd-b64300321193')

# print 'Domains'
# v(api.Domains.Categorization('hecloud.org', 'google.com'))
# v(api.Domains.Categories())
# v(api.Domains.Score('hecloud.org', 'google.com'))
# v(api.Domains.LatestTags('hecloud.org'))
# print ''

# print 'Timeline'
# v(api.Timeline('domain.com'))
# print ''

# print 'URL'
# v(api.URL.Classifiers('hecloud.org'))
# v(api.URL.Info('hecloud.org'))
# print ''

# print 'Search'
# v(api.Search('hecloud.org', '-30days', True))
# print ''

# print 'Recommendations'
# v(api.Recommendations.Name('hecloud.org'))
# print ''

# print 'Links'
# v(api.Links.Name('hecloud.org'))
# print ''

# print 'Security'
# v(api.Security.Name('hecloud.org'))
# print ''

# print 'DnsDB'
# v(api.DnsDB.Name('hecloud.org'))
# v(api.DnsDB.IP('8.8.8.8'))
# print ''

# print 'BGP'
# v(api.BgpRoutes.IP('8.8.8.8'))
# v(api.BgpRoutes.ASN(11425))

# print 'WhoIs'
# v(api.WhoIs('hecloud.org'))
# v(api.WhoIs.Emails('dns-admin@google.com', 'hostmaster@charter.com', limit=2, offset=10, sort='created'))
# v(api.WhoIs.Nameservers('ns1.google.com', 'ns2.google.com', limit=2, offset=10, sort='created'))
# print ''

# print 'IPs'
# v(api.IPs.LatestDomains('218.23.28.135'))
# print ''

# print 'TopMillion'
# v(api.TopMillion(limit=100))
# print ''

print 'Samples'
v(api.Samples('208.100.26.234'))
print ''
