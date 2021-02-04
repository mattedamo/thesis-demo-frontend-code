import sys, os

def main():
    #devo fare una versione sia per l'hotfix, sia una per la release, qua le metto tutte e 2
    #differenziando i due flow
    #type_branch = "hotfix"
    #print(sys.argv)
    this_branch = os.environ["GITHUB_HEAD_REF"]
    list = (sys.argv)
    del list[0]
    if len(list) == 0:
        new_tag = "v0.1"
    else:
        list.sort()
        last_tag = list[-1]
        last_tag_list = last_tag.split(".")
        if("releases" in this_branch):
            #nuova release
            value_to_update = int(last_tag_list[0][1:])
            value_to_update += 1
            new_tag = "v"+str(value_to_update)+".0"
        else:
            #hotfix    
            value_to_update = int(last_tag_list[1])
            value_to_update += 1
            new_tag = last_tag_list[0]+"."+str(value_to_update)
    print(new_tag)
    

if __name__ == "__main__":
    main()
