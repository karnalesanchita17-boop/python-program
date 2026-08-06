# String Programs Collection (1-30)

# 1. String Length
s=input("Enter string: ")
c=0
for _ in s: c+=1
print(c)

# 2. Character Count
s=input("Enter string: ")
v=cons=dig=sp=spec=0
for ch in s:
    if ch.lower() in "aeiou": v+=1
    elif ch.isalpha(): cons+=1
    elif ch.isdigit(): dig+=1
    elif ch==" ": sp+=1
    else: spec+=1
print(v,cons,dig,sp,spec)

# 3. Reverse
s=input()
r=""
for ch in s: r=ch+r
print(r)

# 4. Palindrome
s=input()
print("Palindrome" if s==s[::-1] else "Not Palindrome")

# 5. Upper/Lower Count
s=input();u=l=0
for ch in s:
    if ch.isupper():u+=1
    elif ch.islower():l+=1
print(u,l)

# 6. Replace Characters
s=input();a=input();b=input()
print(s.replace(a,b))

# 7. Remove Spaces
print(input().replace(" ",""))

# 8. Frequency of Character
s=input();ch=input()
print(s.count(ch))

# 9. First and Last Character
s=input()
print(s[0],s[-1])

#10 ASCII Values
s=input()
for ch in s: print(ch,ord(ch))

#11 Word Count
print(len(input().split()))

#12 Longest Word
w=input().split();print(max(w,key=len))

#13 Shortest Word
w=input().split();print(min(w,key=len))

#14 Title Case
print(input().title())

#15 Duplicate Characters
s=input();seen=set()
for ch in s:
    if s.count(ch)>1 and ch not in seen:
        print(ch,end=" ");seen.add(ch)
print()

#16 Character Frequency
s=input()
for ch in dict.fromkeys(s):
    print(ch,s.count(ch))

#17 Anagram
a=input();b=input()
print("Anagram" if sorted(a)==sorted(b) else "Not Anagram")

#18 Remove Duplicate Characters
s=input();r=""
for ch in s:
    if ch not in r:r+=ch
print(r)

#19 Substring Search
s=input();sub=input()
print("Found" if sub in s else "Not Found")

#20 Count Word Occurrences
sen=input();w=input()
print(sen.split().count(w))

#21 Password Validator
p=input()
ok=len(p)>=8 and any(c.isupper() for c in p) and any(c.islower() for c in p) and any(c.isdigit() for c in p) and any(not c.isalnum() for c in p)
print("Valid" if ok else "Invalid")

#22 Run Length Encoding
s=input();res="";i=0
while i<len(s):
    cnt=1
    while i+1<len(s) and s[i]==s[i+1]:
        cnt+=1;i+=1
    res+=s[i]+str(cnt);i+=1
print(res)

#23 String Compression
s=input();comp="";i=0
while i<len(s):
    cnt=1
    while i+1<len(s) and s[i]==s[i+1]:
        cnt+=1;i+=1
    comp+=s[i]+str(cnt);i+=1
print(comp if len(comp)<len(s) else s)

#24 Most Frequent Character
from collections import Counter
s=input();c=Counter(s)
print(c.most_common(1)[0])

#25 Second Most Frequent Character
mc=c.most_common(2)
print(mc[1] if len(mc)>1 else "N/A")

#26 Caesar Cipher
msg=input();shift=int(input())
enc=""
for ch in msg:
    if ch.isalpha():
        base=65 if ch.isupper() else 97
        enc+=chr((ord(ch)-base+shift)%26+base)
    else: enc+=ch
print(enc)

#27 Email Validator
import re
e=input()
print("Valid" if re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",e) else "Invalid")

#28 Word Frequency
from collections import Counter
print(Counter(input().lower().split()))

#29 Sentence Reversal
print(" ".join(input().split()[::-1]))

#30 String Rotation
a=input();b=input()
print("Yes" if len(a)==len(b) and b in a+a else "No")
