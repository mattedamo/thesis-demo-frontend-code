import yaml, os, sys

def main():
    github_ref = os.environ["GITHUB_REF"]
    default_input_flag = os.environ["DEFAULT_INPUT_FLAG"]
    
    with open("./input.yaml") as file:
        input = yaml.load(file, Loader=yaml.FullLoader)
    if default_input_flag == "false":
        if "master" in github_ref:
            branch = "master"
        elif "features" or "releases" in github_ref:
            branch_list = github_ref.split("/")
            branch = branch_list[-2]+"/"+branch_list[-1]
        if "branch" not in input.keys():
            sys.exit("You have to insert the branch key-value in the input file")
        if branch != input["branch"]:
            sys.exit("You have to insert manually the correct branch name in the input file")
    if "clusters" not in input.keys():
        sys.exit("You have to specific the cluster name(s) where you want to deploy the application!") 
if __name__ == '__main__':
    main()
