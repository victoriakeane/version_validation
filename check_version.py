class Version:
    def checkVersion(self, version_a, version_b):
        version_a, version_b = version_a.replace(".", ""), version_b.replace(".", "")
        vers_list = []
        vers_list.append(version_a)
        vers_list.append(version_b)
        ans = None
        #for loop returns tuple of first element from each item of list
        for i in zip(*vers_list):
            if int(i[0]) > int(i[1]):
                ans = 1
            elif int(i[0]) < int(i[1]):
                ans = -1
        if ans == None:
            if len(version_a) > len(version_b):
                ans = 1
            if len(version_b) > len(version_a):
                ans = -1
            #edge case if versions are equal
            else:
                ans = 0
        return ans

        #this also works but felt like cheating given it took the least amount of work
        # if max(vers_list) == version_a:
        #     return 1
        # else: 
        #     return -1


obj = Version()
print(obj.checkVersion("1.2.3", "1.2"))
