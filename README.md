# Pscan tool

Pscan is a simple web analyzing tool, used to crawl web-pages and extract structured data.
It can be used for a wide range of purposes, from data mining to monitoring and penetration testing.
**Only a one request is done to a given web page**\
Author: Alexander Pushkin aka @nesergeevich \
To contact: https://twitter.com/nesergeevich

##### Version: 0.3

## Installation:
```
pip3 -v install bs4
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
"cms": "Drupal",
"cms_version": "7.75",
"external": {
"http://drupal.com/trademark": "registered trademark",
"https://acquia.com": "Acquia",
"https://dri.es": "Dries Buytaert",
...
"https://www.srijan.net/": "",
"https://www.thirdandgrove.com/": ""
},
"internal": {
"https://drupal.org/#block-system-main-menu": "",
"https://drupal.org/#block-system-user-menu": "",
"https://drupal.org/#content": "Skip to main content",
...
"https://www.drupal.org/terms": "Terms of service",
"https://www.drupal.org/training": "Training"
},
"sec_headers": {
"Content-Security-Policy": "frame-ancestors 'self'",
"Public-Key-Pins": null,
"Strict-Transport-Security": "max-age=10886400; includeSubDomains; preload",
"X-Content-Type-Options": "nosniff",
"X-Frame-Options": "SAMEORIGIN",
"X-XSS-Protection": null
},
"subdomain": {
"http://events.drupal.org/drupalcon2021": "Learn more",
"https://api.drupal.org/": "API.Drupal.org",
"https://events.drupal.org": "DrupalCon",
...
"https://jobs.drupal.org/": "Jobs",
"https://jobs.drupal.org/?utm_source=drupal.org&utm_medium=HPS": "Try It Today"
}
}
```
