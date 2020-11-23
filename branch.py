# Starting the branch and bound algorithm
def branchAndBound(tree):
    total_branch_length = 0
    for i in range(len(tree)):
        temp = tree[i]
        # print(temp[2])
        total_branch_length += temp[2]
        print(tree[i])
    print(total_branch_length)

