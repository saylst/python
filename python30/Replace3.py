# 替换列表中所有的 3 为 3a

if __name__ == '__main__':

    nums = ['harden', 'lampard', 3, 34, 45, 56, 76, 3, 3, 876, 999]

    for i in range(nums.count(3)):
        ele_index = nums.index(3)
        nums[ele_index] = '3a'

    print(nums)
