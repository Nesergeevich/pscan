#!/usr/bin/env python3

'''
**************************************************************************************************************
*                           => Pscan <=                                                                      *
*                                                                                                            *
* Pscan is a simple web analyzing tool, used to crawl web-pages and extract structured data.                 *
* It can be used for a wide range of purposes, from data mining to monitoring and penetration testing.       *
*                                                                                                            *
* Version: 0.3.1                                                                                             *
* Installing:                                                                                                *
*	pip3 -v install bs4											                                             *
*                                                                                                            *
* Author: Alexander Pushkin aka @nesergeevich                                                                *
*                                                                                                            *
* To contact: https://twitter.com/nesergeevich                                                               *
*                                                                                                            *
**************************************************************************************************************
'''

import sys, socket
import requests, time
import json, urllib3

from bs4 import BeautifulSoup
from urllib.parse import urlparse
from ipwhois import IPWhois

from pprint import pprint

from cms import CMS

# suppress InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ========================== Definitions =======================================

BASE_SCHEME = "http"

# ==============================================================================

class Page():
    """Class Page is a class for storaging and processing a url"""

    def __init__(self, url = "empty"):
        self.url = url
        self.code = 0
        self.length = 0
        self.data = ""
        self.headers = dict()
        self.domain = ""
        self.scheme = ""


    def get_webpage(self):
        headers = {"user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"}
        try:
            r = requests.get(self.url, verify = False, headers = headers)
            self.data = r.text
            self.headers = r.headers
            self.length = len(r.text)
            self.code = r.status_code
            return True
        except requests.exceptions.RequestException as e:
            print('[!] Get web page error: {}'.format(e))
            return False


    def url_maker(self):
        obj = self.url_parse(self.url)
        self.domain = obj["domain"]
        self.scheme = obj["scheme"]

        if self.domain == "":
            return False

        if self.scheme == "":
            if self.url.find("//") == 0:
                self.url = ":".join([BASE_SCHEME, self.url])
            else:
                self.url = "://".join([BASE_SCHEME, self.url])

        if self.url.find("//www.") != -1:
            t = self.url.partition("www.")
            self.url = t[0] + t[2]
        return True


    def url_parse(self, link):
        obj = urlparse(link)
        url_obj = dict()

        if obj.netloc.find(":") != -1:
            url_obj["domain"] = obj.netloc[:obj.netloc.find(":")]
        else:
            url_obj["domain"] = obj.netloc

        url_obj["scheme"] = obj.scheme
        return url_obj


    def href_filter(self, href):
        href = href.strip()
        if href == "" or href == "#" or href.find("mailto:") == 0 or href.find("tel:") == 0 or href.find("javascript:") == 0:
            return False

        href_dic = dict()

        # for relative links
        if href.find("http") != 0 and href.find("//") != 0:
        	if href.find("/") == 0:
        		href = self.scheme + "://" + self.domain + href
        	else:
        		href = self.scheme + "://" + self.domain + "/" + href
        	href_dic["type"] = "internal"
        	href_dic["href"] = href
        	return href_dic

        # for absolute links
        current_href_dic = self.url_parse(href)
        if current_href_dic["domain"] == self.domain or current_href_dic["domain"] == "www." + self.domain:
            href_dic["type"] = "internal"
            href_dic["href"] = href
        elif current_href_dic["domain"].find(self.domain) > 0:
            href_dic["type"] = "subdomain"
            href_dic["href"] = href
        else:
            href_dic["type"] = "external"
            href_dic["href"] = href
        return href_dic

# ==============================================================================

class Domain():
    """Domain class contains an information about IP, netname and so on"""

    def __init__(self, domain = "empty"):
        self.domain = domain
        self.ip = ""
        self.whois = ""

    def get_ip(self):
        try:
            self.ip = socket.gethostbyname(self.domain)
        except:
            self.ip = "undefined"
        return True

    def get_netname(self):
        obj = IPWhois(self.ip)
        try:
            res = obj.lookup_rdap(asn_methods = ['whois'])
            if res['network']['name'] is not None:
                self.whois = res['network']['name']
            if res['network']['country'] is not None:
                self.whois += " - " + res['network']['country']
        except:
            self.whois = "undefined"
        return True

# ==============================================================================

def usage():
    con_header()
    print(
        "\n=> Usage: pscan.py url [debug]\
\n=> Attention! Use a absolute url. Good luck! \n"
    )


def write_file(data, filename):
    try:
        with open(filename, "w") as fh:
            fh.write(data)
        return True
    except Exception as e:
        print('[!] Write file error: {}'.format(e))
        return False


def read_file(filename):
    data = ""
    try:
        with open(filename) as fh:
            data = fh.read()
        return data
    except Exception as e:
        print('[!] Read file error: {}'.format(e))
        return data


def con_report(dic):
    print('\n=> Pscan has been successfully finished')
    print('=> Main report: %s' % dic["filename"])
    print('\n=> Internal links: %d' % dic["internal"])
    print('=> Subdomains links: %d' % dic["subdomain"])
    print('=> External links: %d' % dic["external"])
    print('\n=> CMS: %s' % dic["cms"])
    print('=> CMS version: %s' % dic["cms_version"])
    print('\n')
    return True

def con_header():
    print('\n****************************************************************************\n\
*                           => Pscan <=                                    *\n\
*                                                                          *\n\
* Version: 0.3.1                                                           *\n\
*                                                                          *\n\
****************************************************************************\n')

# ******************************************************************************

def entry_point():
    '''
        Main logic
    '''

    # =================== Stg. 1 Getting parametrs =============================

    main_obj = pg.url_parse(pg.url)
    pg.domain = main_obj["domain"]
    pg.scheme = main_obj["scheme"]
    # getting a file prefix
    file_prefix = "_".join([pg.domain, time.strftime("%Y-%m-%d_%H-%M")])
    file_out = file_prefix + ".json"

    # =================== Stg. 2 Getting a page source =========================

    pg.get_webpage()
    if len(pg.data) == 0:
    	print('[!] Web page is empty\n')
    	return False

    # saving page source in debug mode
    if len(sys.argv) == 3:
        if sys.argv[2] == "debug":
            write_file(pg.data, file_prefix + ".html")

    # ==========================================================================

    # parsing a page source
    soup = BeautifulSoup(pg.data, 'html.parser')

    # a final report
    report = dict()
    report["basic_url"] = pg.url
    report["internal"] = dict()
    report["subdomain"] = dict()
    report["external"] = dict()

    # getting links
    for link in soup.find_all('a'):

        if link.get('href') is not None:
            href_dic = pg.href_filter(link.get('href'))

            if href_dic != False:

                href_text = link.get_text().strip()
                if href_dic["type"] == "internal":
                    report["internal"][href_dic["href"]] = href_text

                elif href_dic["type"] == "subdomain":
                    report["subdomain"][href_dic["href"]] = href_text

                elif href_dic["type"] == "external":
                    report["external"][href_dic["href"]] = href_text

                else:
                    print("Undefined type of href - %s" % href_text)

    # CMS detect
    cms_obj = CMS(pg.data, pg.domain, pg.scheme)
    cms_obj.cms_detect()
    if cms_obj.cms != "undefined":
        cms_obj.get_version()

    report["cms"] = cms_obj.cms
    report["cms_version"] = cms_obj.version

    # getting of security headers
    report["sec_headers"] = dict()
    report["sec_headers"]["X-XSS-Protection"] = pg.headers.get("X-XSS-Protection")
    report["sec_headers"]["X-Frame-Options"] = pg.headers.get("X-Frame-Options")
    report["sec_headers"]["X-Content-Type-Options"] = pg.headers.get("X-Content-Type-Options")
    report["sec_headers"]["Content-Security-Policy"] = pg.headers.get("Content-Security-Policy")
    report["sec_headers"]["Strict-Transport-Security"] = pg.headers.get("Strict-Transport-Security")
    report["sec_headers"]["Public-Key-Pins"] = pg.headers.get("Public-Key-Pins")

    # getting of IP and whois
    dmn_obj = Domain(pg.domain)
    dmn_obj.get_ip()
    if dmn_obj.ip != "undefined":
        dmn_obj.get_netname()

    report["domain_ip"] = dmn_obj.ip
    report["domain_netname"] = dmn_obj.whois

    # write a report to a file
    with open(file_out, 'w') as json_file:
        json.dump(report, json_file, ensure_ascii = False, sort_keys = True, indent = 0)

    # write a short report to console
    console_report = dict()
    console_report["filename"] = file_out
    console_report["internal"] = len(report["internal"])
    console_report["subdomain"] = len(report["subdomain"])
    console_report["external"] = len(report["external"])
    console_report["cms"] = report["cms"]
    console_report["cms_version"] = report["cms_version"]
    con_report(console_report)

    return True

# ==============================================================================

if __name__ == '__main__':
    if len(sys.argv) != 3 and len(sys.argv) != 2:
        usage()
        sys.exit(0)

    con_header()

    pg = Page(sys.argv[1])
    pg.url_maker()

    entry_point()
