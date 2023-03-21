from optparse import OptionParser
import ldap3

parser = OptionParser()
parser.add_option("-d", "--domain", dest="domain",help="Domain to scan", metavar="DOMAIN")
(options, args) = parser.parse_args()
domain=options.domain

try:
    server = ldap3.Server(str(domain), get_info=ldap3.ALL, port=389, use_ssl=False,connect_timeout=4)
    connection = ldap3.Connection(server)
    status=connection.bind()
    if status == True:
        print("[+] Anonymous access enabled at "+ domain)
    else:
        print(domain)
except Exception:
    print("")
    
