# Pscan tool

Pscan is a simple web analyzing tool, used to crawl web-pages and extract structured data.
It can be used for a wide range of purposes, from data mining to monitoring and penetration testing.
**Only a one request is done to a given web page**\
Author: Alexander Pushkin aka @nesergeevich \
To contact: https://twitter.com/nesergeevich

##### Version: 0.3.2

## Installation:
```
pip3 -v install bs4
pip3 install ipwhois
```

## Usage:
```
pscan.py url [debug]
```
Attention! Use a absolute page url. Good luck!

## Example:
```
./pscan.py https://www.drupal.org
```

**The result:**
```
{
"basic_url": "https://drupal.org",
"cache_headers": {
"Age": "0",
"Cache-Control": "public, max-age=900",
"ETag": null,
"Expires": "Sun, 19 Nov 1978 05:00:00 GMT",
"Pragma": null,
"Vary": "Cookie,x-compliance-region,Accept-Encoding",
"Warning": null,
"X-Cache": "MISS, MISS",
"X-Cache-Hits": "0, 0",
"X-Drupal-Cache": "MISS"
},
"cms": "Drupal",
"cms_version": "7.80",
"domain_ip": "151.101.2.217",
"domain_netname": "SKYCA-3",
"external": {
"http://drupal.com/trademark": "registered trademark",
"http://www.prweb.com/releases/drupalcon_north_america_2021_keynote_speakers_making_a_positive_impact_in_open_source_and_beyond/prweb17838816.htm": "DrupalCon North America 2021: Keynote speakers making a positive impact in open source and beyond",
"https://acquia.com": "Acquia",
...
"https://www.srijan.net/": "",
"https://www.thirdandgrove.com/": ""
},
"internal": {
"https://drupal.org/#block-system-main-menu": "",
"https://drupal.org/#block-system-user-menu": "",
"https://drupal.org/#content": "Skip to main content",
...
"https://www.drupal.org/swag?utm_source=drupalorg&utm_medium=banner&utm_campaign=drupal_swag_shop_2020_09_17": "Drupal Swag",
"https://www.drupal.org/terms": "Terms of service",
"https://www.drupal.org/training": "Training"
},
"sec_headers": {
"Content-Security-Policy": "frame-ancestors 'self'",
"Public-Key-Pins": null,
"Strict-Transport-Security": "max-age=15552000; includeSubDomains; preload",
"X-Content-Type-Options": "nosniff",
"X-Frame-Options": "SAMEORIGIN",
"X-XSS-Protection": null
},
"subdomain": {
"https://api.drupal.org/": "API.Drupal.org",
"https://events.drupal.org": "DrupalCon",
...
"https://groups.drupal.org/groups": "Groups & meetups",
"https://jobs.drupal.org/": "Jobs"
}
}
```
