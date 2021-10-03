def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    import re
    pattern = r"[\s]*[+-]?[\d]+"
    match = re.match(pattern, str)
    if match:
        res = int(match.group(0))
        if res > 2 ** 31 - 1:
            res = 2 ** 31 -1
        if res < - 2 ** 31:
            res = - 2 ** 31
    else:
        res = 0
    return res

ICC_ratio=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
IDD_ID=""
IDD_ID=input()
print(IDD_ID)
sum=0
tot=0
for i in IDD_ID:
    sum+=(myAtoi(i))*ICC_ratio[tot];
    tot=tot+1
    if tot==17:
        break
if (12-(sum%11))==1:
    last_word=10
if (12-(sum%11))==0:
    last_word=1
if (12-(sum%11))==1:
    last_word=0
else:
    last_word=(12-(sum%11))
if last_word!=10:
    print(last_word)
else:
    print('X')
    
   
