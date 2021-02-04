import os, yaml, sys

def main():
    args = sys.argv
    k = args[-1]
    with open("./config.yaml") as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    if k in ["docker-backend-repo", "docker-frontend-repo", "infrastructure-repo", "backup-input-repo"]:
        if k not in config.keys():
            sys.exit(k + " not present in config file, add it")
        else:
            print(config[k])
    elif k == "tier":
        if k not in config.keys():
            sys.exit(k + " not present in config file, add it")
        else:
            if config[k] not in ["backend", "frontend"]:
                sys.exit(k + " has a not valid value. It must be \"backend\" or \"frontend\" ")
            else:
                print(config[k])
    elif k  in ["default-input-prod", "default-input-release", "default-input-feature"]:
        if k not in config.keys():
            print("false")
        else:
            if config[k] not in [True, False]:
                sys.exit(k + " has a not valid value. It must be True or False")
            else:
                if config[k] == True:
                    print("true")
                else:
                    print("false")

if __name__ == "__main__":
    main()
