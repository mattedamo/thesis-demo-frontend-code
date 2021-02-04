import yaml, os, sys

def main():
    with open("./config.yaml") as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    #check if mandatory key-values are present in config.yaml and in general, if keys have allowed values
    mandatory_elements = ["docker-backend-repo", "docker-frontend-repo", "infrastructure-repo", "backup-input-repo", "tier"]
    for e in mandatory_elements:
        if e not in config.keys():
            sys.exit(e + " not present in config file. It is a mandatory value.")
        if e == "tier":
            if config[e] not in ["backend", "frontend"]:
                sys.exit(e + " has a not valid value. It must be \"backend\" or \"frontend\". ")
    #check if keys have allowed values
    optional_elements = ["default-input-prod", "default-input-feature", "default-input-feature"]
    for e in optional_elements:
        if e in config.keys():
            if config[e] not in [True, False]:
                sys.exit(e + " has a not valid value. It must be a boolean value.")

if __name__ == '__main__':
    main()
