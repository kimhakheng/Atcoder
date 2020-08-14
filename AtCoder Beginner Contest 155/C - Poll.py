    from collections import defaultdict
    from collections import OrderedDict
    N = int(input())
    ans = dict()
    for _ in range(N):
        k = str(input())
        if k in ans:
            ans[k]+=1
        else:
            ans.update({k:1})
    groupedByValue = defaultdict(list)
    for key, value in sorted(ans.items()):
        groupedByValue[value].append(key)
    l = groupedByValue[max(groupedByValue)]
    for i in l:
        print(i)
