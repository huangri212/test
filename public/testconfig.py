import ConfigParser,os,sys

config = ConfigParser.ConfigParser()
config_dir =r'C:/Users/huanri/Documents/apa_auto/public/baseconfig.ini'
config.read(config_dir)

class GetTestConfig:
    @staticmethod
    def getUrl():
        try:
            url = config.get("url","TEST_ENV_URL")

        except ConfigParser.NoOptionError:
            print('could not read configuration file')
            sys.exit(1)
        
        return url

    @staticmethod
    def getAccount():
        account = {}
        try:
            username = config.get("account","username")
            password = config.get("account","password")
            account['username'] = username
            account['password'] = password
        except ConfigParser.NoOptionError:
            print 'could not read configuration file'
            sys.exit(1)
        
        return username,password

    @staticmethod
    def getCompany():
        company = {}
        try:
            companyName = config.get("company","companyName")
        except ConfigParser.NoOptionError:
            print 'could not read configuration file'
            sys.exit(1)
        return companyName

    @staticmethod
    def getProcess():
        try:
            processName = config.get("process","processName")
        except Exception as NoOptionError:
            print 'could not read configuration file'
            sys.exit(1)
        return processName

