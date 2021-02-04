import sys, os

def main():
    list = (sys.argv)
    del list[0]
    branch = ""
    for b in list:
        if "releases" in b:
            branch = b
            break
    
    if branch == "":
        print("develop")
    else:
        branch_list = branch.split("/")
        if branch_list[-2] == "releases":
            print(branch_list[-2]+"/"+branch_list[-1])
        else:
            print("develop")
    

if __name__ == "__main__":
    main()
