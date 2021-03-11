# Pscan tool

Pscan is a simple web analyzing tool, used to crawl web-pages and extract structured data.
It can be used for a wide range of purposes, from data mining to monitoring and penetration testing.
**Only a one request is done to a given web page**\
Author: Alexander Pushkin aka @nesergeevich \
To contact: https://twitter.com/nesergeevich

##### Version: 0.3.1

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
"cms": "Drupal",
"cms_version": "7.78",
"domain_ip": "151.101.66.217",
"domain_netname": "SKYCA-3",
"external": {
"http://drupal.com/trademark": "registered trademark",
"http://www.prweb.com/releases/on_its_20th_birthday_drupal_poised_to_capture_the_next_generation_of_the_digital_experience_market/prweb17664393.htm": "On Its 20th Birthday, Drupal Poised To Capture The Next Generation Of The Digital Experience Market",
"https://acquia.com": "Acquia",
...
"https://www.srijan.net/": "",
"https://www.thirdandgrove.com/": ""
},
"internal": {
"https://drupal.org/#block-system-main-menu": "",
"https://drupal.org/#block-system-user-menu": "",
...
"https://www.drupal.org/terms": "Terms of service",
"https://www.drupal.org/training": "Training",
"https://www.drupal.org/try-drupal": "Try Drupal"
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
"https://api.drupal.org/": "API.Drupal.org",
"https://events.drupal.org": "DrupalCon",
...
"https://groups.drupal.org/groups": "Groups & meetups",
"https://jobs.drupal.org/": "Jobs"
}
}
```
