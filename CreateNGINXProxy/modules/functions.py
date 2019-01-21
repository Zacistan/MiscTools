import os
import sys, getopt

def parse_arguments(args):
    return_dictionary = {}
    # Help text to print if invalid argument or help is requested.
    help_text = ("create_nginx_proxy.py -p <proxy_hostname> -u <proxied_service_url> -a [nginx_sites_available_dir] "
                 "-e [nginx_sites_enabled_dir] -t [nginx_sites_conf_template]")
    
    # Set default paths (Can be overridden by optional arguments).
    return_dictionary["nginx_sites_available_dir"] = "/etc/nginx/sites-available"
    return_dictionary["nginx_sites_enabled_dir"] = "/etc/nginx/sites-enabled"
    return_dictionary["nginx_sites_conf_template"] = "./template"

    # Try to get options. P and U arguments are mandatory as indicated by :'s.
    try:
        opts, args = getopt.getopt(args,"h:p:u:a:e:t:")
    except getopt.GetoptError:
        print(help_text)
        sys.exit(2)
    
    # Assign arguments to values in the dictionary.
    for opt,arg in opts:
        if opt == '-h':
            print(help_text)
            sys.exit()
        elif opt == '-p':
            return_dictionary["proxy_hostname"] = arg
        elif opt == '-u':
            return_dictionary["proxied_service_url"] = arg
        elif opt == '-a':
            return_dictionary["nginx_sites_available_dir"] = arg
        elif opt == '-e':
            return_dictionary["nginx_sites_enabled_dir"] = arg
        elif opt == '-t':
            return_dictionary["nginx_sites_conf_template"] = arg
    
    return return_dictionary

def validate_paths(sites_available_dir, sites_enabled_dir, sites_conf_template):
    # Validate that the NGINX folders exists.
    print("INFO: Checking that nginx folders exist.")
    if not os.path.isdir(sites_available_dir):
        raise Exception("ERROR: Not an accessible directory: {0}".format(sites_available_dir))

    if not os.path.isdir(sites_enabled_dir):
        raise Exception("ERROR: Not an accessible directory: {0}".format(sites_enabled_dir))
    print("INFO: Success! Nginx folders exist.")

    # Validate that the template configuration file exists.
    print("INFO: Checking that template configuration file exists.")
    if not os.path.exists(sites_conf_template):
        raise Exception("ERROR: Not accessible or does not exist: {0}".format(sites_conf_template))
    print("INFO: Success! Template configuration file exists.")