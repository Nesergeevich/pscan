import re
import requests

TIMEOUT = 10

class CMS():
    """ Class CMS is class for detecting content management system (CMS) """

    def __init__(self, data = "", domain = "", scheme = ""):
            self.data = data
            self.domain = domain
            self.scheme = scheme
            self.cms = "undefined"
            self.version = "undefined"


    def drupal_chk(self):
        ''' Drupal checker '''
        reg1 = re.compile('/themes/')
        reg2 = re.compile('generator.+Drupal')
        reg3 = re.compile('drupal\.js')
        reg4 = re.compile('env.+Drupal')
        reg5 = re.compile('X-Generator.+Drupal')
        reg6 = re.compile('icon.+Dupal\.png')
        reg7 = re.compile('/misc1/')
        res1 = reg1.findall(self.data)
        res2 = reg2.findall(self.data)
        res3 = reg3.findall(self.data)
        res4 = reg4.findall(self.data)
        res5 = reg5.findall(self.data)
        res6 = reg6.findall(self.data)
        res7 = reg7.findall(self.data)

        if (res1 != [] and res7 != []) or res2 != [] or res3 != [] or res4 != [] or res5 != [] or res6 != []:
            return True
        else:
            return False


    def wordpress_chk(self):
        ''' Wordpress checker '''
        reg1 = re.compile('/wp-content/')
        reg2 = re.compile('/wp-includes/')
        reg3 = re.compile('env.+wp_username$')
        reg4 = re.compile('generator.{2,20}WordPress')
        reg5 = re.compile('icon.+WordPress\.svg')
        res1 = reg1.findall(self.data)
        res2 = reg2.findall(self.data)
        res3 = reg3.findall(self.data)
        res4 = reg4.findall(self.data)
        res5 = reg5.findall(self.data)
        if res1 != [] or res2 != [] or res3 != [] or res4 != [] or res5 != []:
            return True
        else:
            return False


    def joomla_chk(self):
        ''' Joomla checker '''
        reg1 = re.compile('/media/system/')
        reg2 = re.compile('option=com_')
        # reg3 = re.compile('env+.+[jcomments|Joomla]')
        reg4 = re.compile('generator.{2,20}Joomla')
        reg5 = re.compile('X-Content-Encoded-By : Joomla!.')
        res1 = reg1.findall(self.data)
        res2 = reg2.findall(self.data)
        # res3 = reg3.findall(self.data)
        res4 = reg4.findall(self.data)
        res5 = reg5.findall(self.data)
        if res1 != [] or res2 != [] or res4 != [] or res5 != []:
            return True
        else:
            return False


    def made_simple_chk(self):
        ''' Made Simple checker '''
        reg1 = re.compile('CMS Made Simple')
        reg2 = re.compile('generator.+CMS Made Simple')
        reg3 = re.compile('Set-Cookie/s+:/s+^CMSSESSID')
        res1 = reg1.findall(self.data)
        res2 = reg2.findall(self.data)
        res3 = reg3.findall(self.data)
        if res1 != [] or res2 != [] or res3 != []:
            return True
        else:
            return False


    def contao_chk(self):
        ''' Contao checker '''
        reg1 = re.compile('powered/s+by/s+:/s*TYPOlight|Contao/s+')
        reg2 = re.compile('generator.+Contao Open Source CMS')
        reg3 = re.compile('(typolight|contao)\.css')
        reg4 = re.compile('<link[^>]+(?:typolight|contao)\.css')
        res1 = reg1.findall(self.data)
        res2 = reg2.findall(self.data)
        res3 = reg3.findall(self.data)
        res4 = reg4.findall(self.data)
        if res1 != [] or res2 != [] or res3 != [] or res4 != []:
            return True
        else:
            return False


    def dle_chk(self):
        ''' DLE checker '''
        # reg1 = re.compile('DataLife Engine')
        reg2 = re.compile('env.+dle_root$')
        reg3 = re.compile('generator.+DataLife Engine')
        # res1 = reg1.findall(self.data)
        res2 = reg2.findall(self.data)
        res3 = reg3.findall(self.data)
        # if res1 != [] or res2 != [] or res3 != []:
        if res2 != [] or res3 != []:
            return True
        else:
            return False


    def dotnetnuke_chk(self):
        ''' DNN checker '''
        # reg1 = re.compile('DotNetNuke')
        reg2 = re.compile('/js/dnncore\.js')
        reg3 = re.compile('/js/dnn\.js')
        # res1 = reg1.findall(self.data)
        res2 = reg2.findall(self.data)
        res3 = reg3.findall(self.data)
        # if res1 != [] or res2 != [] or res3 != []:
        if res2 != [] or res3 != []:
            return True
        else:
            return False


    def wps_chk(self):
        ''' WebSphere checker '''
        reg1 = re.compile('/wps/')
        reg2 = re.compile('/websphere/portal.')
        reg3 = re.compile('IBM-Web2-Location')
        res1 = reg1.findall(self.data)
        res2 = reg2.findall(self.data)
        res3 = reg3.findall(self.data)
        if res1 != [] or res2 != [] or res3 != []:
            return True
        else:
            return False


    def instantcms_chk(self):
        ''' InstantCMS checker '''
        if self.data.find("InstantCMS") != -1:
            return True
        else:
            return False


    def mambo_chk(self):
        ''' Mambo checker '''
        if self.data.find("article_seperator") != -1 and self.data.find("contentpaneopen") != -1:
            return True
        else:
            return False


    def bitrix_chk(self):
        ''' Bitrix checker '''
        reg1 = re.compile('/bitrix/tools/')
        reg2 = re.compile('/bitrix/cache/')
        reg3 = re.compile('/bitrix/.+(\.js|templates)')
        # reg4 = re.compile('bitrix')
        res1 = reg1.findall(self.data)
        res2 = reg2.findall(self.data)
        res3 = reg3.findall(self.data)
        # res4 = reg4.findall(self.data)
        if res1 != [] or res2 != [] or res3 != []:
            return True
        else:
            return False


    def sharepoint_chk(self):
        ''' SharePoint checker '''
        reg1 = re.compile('/_layouts/')
        # reg2 = re.compile('Microsoft SharePoint')
        reg3 = re.compile('spBodyOnLoadCalled')
        res1 = reg1.findall(self.data)
        # res2 = reg2.findall(self.data)
        res3 = reg3.findall(self.data)
        # if res1 != [] or res2 != [] or res3 != []:
        if res1 != [] or res3 != []:
            return True
        else:
            return False


    def aspnet_chk(self):
        ''' ASP.NET checker '''
        if self.data.find("__VIEWSTATE") != -1:
            return True
        else:
            return False


    def modx_chk(self):
        ''' Modx checker '''
        reg1 = re.compile('/assets/snippets/')
        reg2 = re.compile('env.+MODX_MEDIA_PATH')
        reg3 = re.compile('Powered by MODX')
        reg4 = re.compile('/assets/css/_style.css')
        reg5 = re.compile('/assets/templates/')
        res1 = reg1.findall(self.data)
        res2 = reg2.findall(self.data)
        res3 = reg3.findall(self.data)
        res4 = reg4.findall(self.data)
        res5 = reg5.findall(self.data)
        if res1 != [] or res2 != [] or res3 != [] or res4 != [] or res5 != []:
            return True
        else:
            return False


    def plone_chk(self):
        ''' Plone checker '''
        if self.data.find("Plone") != -1:
            return True
        else:
            return False


    def typo3_chk(self):
        ''' Typo3 checker '''
        reg1 = re.compile('typo3temp/')
        reg2 = re.compile('TYPO3\.svg')
        reg3 = re.compile('/typo3/')
        res1 = reg1.findall(self.data)
        res2 = reg2.findall(self.data)
        res3 = reg3.findall(self.data)
        if res1 != [] or res2 != [] or res3 != []:
            return True
        else:
            return False


    def umbraco_chk(self):
        ''' Umbraco checker '''
        reg1 = re.compile('/umbraco/')
        reg2 = re.compile('(IMAGE_SERVICE|ITEM_INFO_SERVICE|SETTINGS).*Umbraco')
        reg3 = re.compile('powered by <a href=.+umbraco')
        reg4 = re.compile('/umbraco/login\.aspx')
        res1 = reg1.findall(self.data)
        res2 = reg2.findall(self.data)
        res3 = reg3.findall(self.data)
        res4 = reg4.findall(self.data)
        if res1 != [] or res2 != [] or res3 != [] or res4 != []:
            return True
        else:
            return False


    def umi_chk(self):
        ''' UMI checker '''
        if (self.data.find("umi-cms") != -1):
            return True
        else:
            return False


    def netcat_chk(self):
        ''' Netcat checker '''
        reg1 = re.compile('/netcat_files/')
        reg2 = re.compile('/netcat/modules/')
        res1 = reg1.findall(self.data)
        res2 = reg2.findall(self.data)
        if res1 != [] or res2 != []:
            return True
        else:
            return False


    def ipb_chk(self):
        ''' IPBoard checker '''
        reg1 = re.compile('jscripts/ips_')
        reg2 = re.compile('(IPBoard$|ipb_var|ipsSettings)')
        reg3 = re.compile('ipb\.css')
        res1 = reg1.findall(self.data)
        res2 = reg2.findall(self.data)
        res3 = reg3.findall(self.data)
        if res1 != [] or res2 != [] or res3 != []:
            return True
        else:
            return False


    def mybb_chk(self):
        ''' MyBB checker '''
        reg1 = re.compile('lang.no_new_posts')
        reg2 = re.compile('title=\"Powered By MyBB')
        res1 = reg1.findall(self.data)
        res2 = reg2.findall(self.data)
        if res1 != [] or res2 != []:
            return True
        else:
            return False


    def phpbb_chk(self):
        ''' PhpBB checker '''
        reg1 = re.compile('phpbb_alert')
        reg2 = re.compile('env.+(style_cookie_settings|phpbb_)')
        reg3 = re.compile('Set-Cookie.*:.*phpbb')
        res1 = reg1.findall(self.data)
        res2 = reg2.findall(self.data)
        res3 = reg3.findall(self.data)
        if res1 != [] or res2 != [] or res3 != []:
            return True
        else:
            return False


    def smf_chk(self):
        ''' SMF checker '''
        reg1 = re.compile('/smf/default/')
        reg2 = re.compile('(smf_charset|session_id|smf_theme_url)')
        res1 = reg1.findall(self.data)
        res2 = reg2.findall(self.data)
        if res1 != [] or res2 != []:
            return True
        else:
            return False


    def vbulletin_chk(self):
        ''' vBulletin checker '''
        reg1 = re.compile('vbulletin.css')
        reg2 = re.compile('(vbulletin-core.js|vBulletin_init|vb_meta_bburl)')
        res1 = reg1.findall(self.data)
        res2 = reg2.findall(self.data)
        if res1 != [] or res2 != []:
            return True
        else:
            return False


    def cms_detect(self):
        if self.drupal_chk() == True:
            self.cms = "Drupal"

        elif self.wordpress_chk() == True:
            self.cms = "Wordpress"

        elif self.joomla_chk() == True:
            self.cms = "Joomla"

        elif self.made_simple_chk() == True:
            self.cms = "CMS Made Simple"

        elif self.contao_chk() == True:
            self.cms = "Contao"

        elif self.dle_chk() == True:
            self.cms = "DataLife Engine"

        elif self.dotnetnuke_chk() == True:
            self.cms = "DotNetNuke"

        elif self.wps_chk() == True:
            self.cms = "IBM Websphere Portal"

        elif self.instantcms_chk() == True:
            self.cms = "InstantCMS"

        elif self.mambo_chk() == True:
            self.cms = "Mambo"

        elif self.bitrix_chk() == True:
            self.cms = "1C-Bitrix"

        elif self.sharepoint_chk() == True:
            self.cms = "Microsoft SharePoint"

        elif self.aspnet_chk() == True:
            self.cms = "Microsoft ASP.NET"

        elif self.modx_chk() == True:
            self.cms = "MODx"

        elif self.plone_chk() == True:
            self.cms = "Plone"

        elif self.typo3_chk() == True:
            self.cms = "TYPO3 CMS"

        elif self.umbraco_chk() == True:
            self.cms = "Umbraco"

        elif self.umi_chk() == True:
            self.cms = "UMI"

        elif self.netcat_chk() == True:
            self.cms = "Netcat"

        elif self.ipb_chk() == True:
            self.cms = "IPB"

        elif self.mybb_chk() == True:
            self.cms = "MyBB"

        elif self.phpbb_chk() == True:
            self.cms = "phpBB"

        elif self.smf_chk() == True:
            self.cms = "SMF"

        elif self.vbulletin_chk() == True:
            self.cms = "vBulletin"

        else:
            self.cms = "undefined"


    def get_webpage(self, url):
        headers = {"user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"}
        data = dict()
        try:
            r = requests.get(url, verify=False, headers=headers, timeout=TIMEOUT)
            data['available'] = True
            data['code'] = r.status_code
            data['url'] = r.url
            data['body'] = r.text
            return data
        except requests.exceptions.RequestException as e:
            print('Get web page error: {}'.format(e))
            data['available'] = False
            data['code'] = r.status_code
            data['url'] = r.url
            data['body'] = ""
            return data



    def get_version(self):
        ''' Get CMS version '''
        base_url = self.scheme + "://" + self.domain

        if self.cms == "Drupal":
            data = self.get_webpage(base_url + "/CHANGELOG.txt")
            if data['available'] == True:
                if (data['code'] == 200 and data['body'].find("Drupal") != -1):
                    p = re.compile('\d\.\d{2}')
                    versions = p.findall(data['body'])
                    try:
                        self.version = versions[0]
                    except:
                        pass


        elif self.cms == "Wordpress":
            data = self.get_webpage(base_url + "/readme.html")
            if data['available'] == True:
                if (data['code'] == 200 and data['body'].find("WordPress") != -1):
                    p = re.compile(r'(Version|Версия)\s+(\d\.\d(\.\d)?)')
                    versions = p.search(data['body'])
                    try:
                        self.version = versions.group(2)
                    except:
                        pass
            if self.version == "undefined":
                data = self.get_webpage(base_url)
                if data['available'] == True:
                    if (data['code'] == 200 and data['body'].find("generator") != -1):
                        p = re.compile(r'name="generator"\s+content="WordPress\s+(\d\.\d(\.\d+)?)"')
                        versions = p.search(data['body'])
                        try:
                            self.version = versions.group(1)
                        except:
                            pass

        elif self.cms == "Joomla":
            data = self.get_webpage(base_url)
            if data['available'] == True:
                if (data['code'] == 200 and data['body'].find("generator") != -1):
                    p = re.compile(r'name="generator"\s+content="[^\d]+(\d\.\d(\.\d)?)"')
                    versions = p.search(data['body'])
                    try:
                        self.version = versions.group(1)
                    except:
                        pass

        elif self.cms == "CMS Made Simple":
            data = self.get_webpage(base_url)
            if data['available'] == True:
                if (data['code'] == 200 and data['body'].find("CMS Made Simple") != -1):
                    p = re.compile(r'(CMS Made Simple)\s+(\d\.)')
                    versions = p.search(data['body'])
                    try:
                        self.version = versions.group(1)
                    except:
                        pass

        elif self.cms == "Contao":
            data = self.get_webpage(base_url)
            if data['available'] == True:
                if (data['code'] == 200 and data['body'].find("generator") != -1):
                    p = re.compile(r'name="generator"\s+content="Contao Open Source CMS\s+\d\.+\d\.+\d\."')
                    versions = p.search(data['body'])
                    try:
                        self.version = versions.group(1)
                    except:
                        pass

        elif self.cms == "DataLife Engine":
            data = self.get_webpage(base_url + "/ajax/updates.php")
            if data['available'] == True:
                if (data['code'] == 200 and data['body'].find("DataLife Engine") != -1):
                    p = re.compile(r'DataLife Engine\s+\d{1,2}\.+\d')
                    versions = p.search(data['body'])
                    try:
                        self.version = versions.group(1)
                    except:
                        pass

        elif self.cms == "InstantCMS":
            pass

        elif self.cms == "1C-Bitrix":
            data = self.get_webpage(base_url + "/bitrix/admin/index.php")
            if data['available'] == True:
                if (data['code'] == 200 and data['body'].find("Bitrix") != -1):
                    p = re.compile(r'Управление сайтом:\s+\d\d\.\d\.\d')
                    versions = p.search(data['body'])
                    try:
                        self.version = versions.group(1)
                    except:
                        pass

        elif self.cms == "TYPO3 CMS":
            data = self.get_webpage(base_url)
            if data['available'] == True:
                if (data['code'] == 200 and data['body'].find("TYPO3") != -1):
                    p = re.compile(r'name="generator" content="TYPO3\s+\d+\.+\d+\sCMS"')
                    versions = p.search(data['body'])
                    try:
                        self.version = versions.group(1)
                    except:
                        pass

        elif self.cms == "SMF":
            data = self.get_webpage(base_url)
            if data['available'] == True:
                if (data['code'] == 200 and data['body'].find("SMF") != -1):
                    p = re.compile(r'Powered\s+by\s+SMF\s+\d+\.+\d+\.+\d')
                    versions = p.search(data['body'])
                    try:
                        self.version = versions.group(1)
                    except:
                        pass

        elif self.cms == "UMI":
            pass

        elif self.cms == "Netcat":
            data = self.get_webpage(base_url + "/robots.txt")
            if data['available'] == True:
                if (data['code'] == 200 and data['body'].find("NetCat") != -1):
                    p = re.compile(r'^NetCat\s+(\d+)')
                    versions = p.search(data['body'])
                    try:
                        self.version = versions.group(1)
                    except:
                        pass

        elif self.cms == "vBulletin":
            data = self.get_webpage(base_url)
            if data['available'] == True:
                if (data['code'] == 200 and data['body'].find("vBulletin") != -1):
                    p = re.compile(r'meta name="generator" content="vBulletin\s+\d\.+\d\.+\d?')
                    versions = p.search(data['body'])
                    try:
                        self.version = versions.group(1)
                    except:
                        pass

        elif self.cms == "phpBB":
            data = self.get_webpage(base_url + "/docs/CHANGELOG.html")
            if data['available'] == True:
                if (data['code'] == 200 and data['body'].find("phpBB") != -1):
                    p = re.compile(r'phpBB\s+\d\.+\d\.+x Changelog')
                    versions = p.search(data['body'])
                    try:
                        self.version = versions.group(1)
                    except:
                        pass
