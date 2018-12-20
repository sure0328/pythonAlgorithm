def wordPattern(wordPattern, input):
    word = input.split(' ')				#目标字符串中的单词以空格隔开
    if len(word) != len(wordPattern):	#如果两个字符串的长度不一样，则肯定不匹配
        return False
    hash = {}						#记录模式字符串和目标字符串的对应关系
    used= {}						#记录目前已经使用的字符串都有哪些
    for i in range(len(wordPattern)):
        if wordPattern[i] in hash:			#检查模式字符串中的字符是否已经记录过映射关系
            if hash [wordPattern[i]] != word[i]:	#不是第一次出现，则检查映射关系是否一致
                return False
        else:
           if word[i] in used:				#检查这个单词是否已经使用过，使用过返回不成立
              return False
           hash [wordPattern[i]] = word[i]	#第一次出现，则加入到哈希表即可
           used[word[i]] = True			#在used中保存哪些单词已经使用过
    return True