# Scrapy settings for wlw project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import scraper_helper as sh

BOT_NAME = 'wlw'

SPIDER_MODULES = ['wlw.spiders']
NEWSPIDER_MODULE = 'wlw.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wlw (+http://www.yourdomain.com)'

DEFAULT_REQUEST_HEADERS = sh.get_dict('''
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9,ar;q=0.8
cache-control: no-cache
cookie: wlw_client_id=CmU/B2P2HstOZQEvA0f0Ag==; CookieConsent={stamp:%27Nx7biwcRDRLkYcJElPQefv468coRdkTqtbyVliUSSsBGtcVzEFEfKg==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:4%2Cutc:1677074130908%2Cregion:%27fr%27}; _fbp=fb.1.1677074132213.1190325046; cjConsent=MHxZfDB8Tnww; hubspotutk=6bedbd4ee9e64b8e70f70a90d595a6e4; aam_uuid=37106860132310257673516849451010659371; _gcl_au=1.1.89142889.1677074134; _hjSessionUser_1300776=eyJpZCI6IjZlOTZmN2ZjLWM3MzgtNTI3OC1hN2U2LTg1ZjBiYTMwMzM2MiIsImNyZWF0ZWQiOjE2NzcwNzQxMzI2MjYsImV4aXN0aW5nIjp0cnVlfQ==; i18n_redirected=de; ufs_returning_user=1; __hstc=80469576.6bedbd4ee9e64b8e70f70a90d595a6e4.1677074132736.1677145098250.1679574331624.3; __hssrc=1; ab_testing_traffic_split_group=explore_b; AMCVS_41833DF75A550B4B0A495DA6%40AdobeOrg=1; AMCV_41833DF75A550B4B0A495DA6%40AdobeOrg=359503849%7CMCIDTS%7C19440%7CMCMID%7C37216381566564415653464588193081991825%7CMCAAMLH-1680179285%7C6%7CMCAAMB-1680179285%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1679581685s%7CNONE%7CvVersion%7C5.0.1; _uetvid=92491c70b2b811edb20d1913ea0f8bd8; cto_bundle=fvwv1l9NMWRMd0VGZk1NYXUzc0p1dnJZVkMxWCUyQjl6Qmo1aEZpejFqbTN5Mm1Hc2ZQdUslMkZEWHJGMGZJNldQMkJWdHFORE9NZCUyRmk5UCUyRkQ4MTF0amY0a0RoREJnNlQ0WUJ2ZHFMZ0pHYUYlMkY2TlFHeE1DY2dUbXpnOHhSQTl0ZGRpTTUxTXEzdmY3QU1wMlJBYUNhZUMwRWRxbW1BJTNEJTNE; _ga=GA1.2.1275744518.1677074131; _ga_W3RRQVVW47=GS1.1.1679587170.5.0.1679587170.0.0.0; ufs_session_id=c7d4c717265d25e90bc16cb6271b6920; ab_testing_variants_v2=%7B%22template%22%3A%7B%22name%22%3A%22treatment%22%2C%22dimension%22%3Anull%2C%22active%22%3Atrue%2C%22expiry%22%3A1680896759%7D%2C%22174_connect_checkbox%22%3A%7B%22name%22%3A%22v1.0%22%2C%22dimension%22%3A%22wlwTestGroup15%22%2C%22active%22%3Atrue%2C%22expiry%22%3A1680896573%7D%2C%22180_get_email_phone_click%22%3A%7B%22name%22%3A%22v2.0%22%2C%22dimension%22%3A%22wlwTestGroup17%22%2C%22active%22%3Atrue%2C%22expiry%22%3A1680896573%7D%7D; wlw_search_term=automation; wlw_search_method=freetext
pragma: no-cache
sec-ch-ua: "Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36
'''
)
DOWNLOAD_DELAY = 0.5
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'wlw.middlewares.WlwSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'wlw.middlewares.WlwDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'wlw.pipelines.WlwPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
