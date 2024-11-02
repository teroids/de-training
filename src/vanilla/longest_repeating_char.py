def max_repeating(s):
    max_ = 0
    c = 1
    longest=''
    if len(s) ==1:
        return 1, s[0]
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            c = c + 1
        if c > max_:
            max_ = c
            longest = s[i-1]
        if s[i] != s[i-1]:
            c=1
    return max_, longest

as_ = ['aabbaaccbbbaa', 'adccccbbbbc','a', '', 'aaaaaaabbbbbbbbccxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx']

def longestPalindrome(s: str) -> str:
    n = len(s)
    w1=1
    w2=2
    output=s[0]
    max_ = output
    max_2 = output
    for i in range(n):
        if i+w1<n and s[i] == s[i+w1]:
            max_ = s[i:i+w1+1]
            l,r = i-1, i+w1+1
            while l >= 0 and r < n and s[l]==s[r]:
                max_ = s[l] + max_ + s[r]
                r += 1
                l -= 1
        if i+w2<n and s[i] == s[i+w2]:
            max_2 = s[i:i+w2+1]
            l,r = i-1, i+w2+1
            while l >= 0 and r < n and s[l]==s[r]:
                max_2 = s[l] + max_2 + s[r]
                r += 1
                l -= 1
        if len(max_) > len(output) or len(max_2) > len(output):
            output = max_ if len(max_) > len(max_2) else max_2
    return output
                
tests = ["a","aa","aaa","aaaa","xaaaa","cbbd", "abcdefedcxyz"]
for test in tests:
    print(test, "->", longestPalindrome(test))
