import os
import json
import sys
from modules.functions import parse_arguments,validate_paths

def main(argv):
    # Parse the arguments and put them into a dictionary.
    arguments = parse_arguments(args=argv)

    # Validate paths exist and are accessible.
    validate_paths(sites_available_dir=arguments["nginx_sites_available_dir"], 
                   sites_enabled_dir=arguments["nginx_sites_enabled_dir"], 
                   sites_conf_template=arguments["nginx_sites_conf_template"])

    # Load the template and replace placeholder values with real values.
    with open(arguments["nginx_sites_conf_template"]) as template_file:
        config_text = template_file.read()
        config_text = config_text.replace("__proxy_hostname__",arguments["proxy_hostname"])
        config_text = config_text.replace("__proxied_service_url__",arguments["proxied_service_url"])

    # Create the paths for the sites available config file and the sites enabled symbolic link.
    site_config_file = os.path.join(arguments["nginx_sites_available_dir"],arguments["proxy_hostname"])
    site_enabled_symlink = os.path.join(arguments["nginx_sites_enabled_dir"],arguments["proxy_hostname"])
    
    # Write the modified configuration from the template to the site config file.
    with open(site_config_file,"w+") as site_config:
        site_config.write(config_text)

    # Create a symbolic link in the sites enabled to the sites available.
    os.symlink(site_config_file, site_enabled_symlink)
    
if __name__ == "__main__":
    main(sys.argv[1:])