#String Length
#Write a program to input a string and display its length without using the len() function
string=input("enter a string: ")
count=0
for ch in string:
    count=count+1
print("Length of the string is:",count)


#Character Count
#Count the number of vowels, consonants, digits, spaces, and special characters in a given string. 
string=input("enter a string: ")
vowels=consonants=digits=spaces=special=0
for ch in string:
    if ch.lower() in "aeiou":
        vowels+=1
    elif ch.isalpha():
        consonants+=1
    elif ch.isdigit():
        digits+=1
    elif ch.isspace():
        spaces+=1
    else:
        special+=1
print("vowels:",vowels)
print("consonants:",consonants)
print("digits:",digits)
print("spaces:",spaces)
print("special Characters:",special)


#Reverse String
#Reverse the given string without using built-in reverse functions
string=input("Enter a string:")
reverse=""
for ch in string:
    reverse=ch+reverse
print("reversed string is:",reverse)


#Palindrome Check
#Check whether the entered string is a palindrome. 
string=input("enter a string:")
reverse=""
for ch in string:
    reverse=ch+reverse
if string==reverse:
    print("string is a palindrome")
else:
    print("string is not a palindrome")



#Uppercase and Lowercase Count 
#Count the number of uppercase and lowercase letters in a string    
string=input("enter a string: ")
upper=0
lower=0
for ch in string:
    if ch.isupper():
        uppercase+=1
    elif ch.islower():
        lowercase+=1
print("upper letters:",upper)
print("lower letters:",lower)


#Replace Characters
#Replace all occurrences of a given character with another character
string=input("enter a string:")
old=input("enter the character to replace:")
new=input("enter the new character:")
result=""
for ch in string:
    if ch==old:
        result=result+new
    else:
        result=result+ch
print("updated string:",result)



#Remove Spaces
#Remove all spaces from the input string
string=input("enter a string:")
result= ""
for ch in string:
    if ch != " ":
        result=result+ch
print("String:",result)



#Frequency of Character
#Find the number of times a specified character appears in a string. 
string=input("enter a string: ")
char=input("enter the character:")
count=0
for ch in string:
    if ch==char:
        count+=1
print("number of",char,"is:",count)


#First and Last Character
#Print the first and last character of a string. 
string=input("enter a string:")
if string:
    print("first character:", string[0])
    print("last character:", string[-1])
else:
    print("string is empty")


#Ascii Values
#Display each character of a string along with its ASCII value.
string=input("enter a string:")
for ch in string:
    print(ch,":",ord(ch))


#Word Count
#Count the total number of words in a sentence. 
sentence=input("enter a sentence:")
words=sentence.split()
count=0
for word in words:
    count+=1
print("total number of words:",count)


#Longest Word
#Find the longest word in a given sentence
sentence=input("enter a sentence: ")
words=sentence.split()
longest=""
for word in words:
    if len(word)>len(longest):
       longest = word
print("longest word:",longest)
print("length:",len(longest))


#Shortest Word
#Find the shortest word in a sentence
sentence=input("enter a sentence:")
words=sentence.split()
shortest=words[0]
for word in words:
    if len(word)<len(shortest):
        shortest=word
print("shortest word:",shortest)
print("length:",len(shortest))


#Title Case
#Convert the first letter of every word to uppercase
sentence=input("enter a sentence: ")
words=sentence.split()
result=""
for word in words:
    result=result+word.capitalize()+ " "
print("updated sentence:",result)



#Duplicate Characters
#Print all duplicate characters in a string
string=input("enter a string:")
printed=""
for i in range(len(string)):
    count=0
    for j in range(len(string)):
        if string[i]==string[j]:
            count+=1
    if count>1 and string[i] not in printed:
        print(string[i])
        printed+=string[i]


#Character Frequency
#Display the frequency of every character in a string
string=input("enter a string: ")
checked=""
for ch in string:
    if ch not in checked:
        count=0
        for c in string:
            if ch==c:
                count+=1
        print(ch,":",count)
        checked+=ch


#Anagram Check
#Check whether two strings are anagrams.   
str1=input("enter first string: ")
str2=input("enter second string: ")
s1=sorted(str1.lower())
s2=sorted(str2.lower())
if s1==s2:
    print("strings are anagrams")
else:
    print("strings are not anagrams")



#Remove Duplicate Characters
#Remove duplicate characters while maintaining the original order
string=input("enter a string: ")
result=""
for ch in string:
    if ch not in result:
        result += ch
print("after removing duplicates:",result)



#Substring Search
#Check whether a given substring exists in the main string
mstring=input("enter the main string:")
substring=input("enter the substring:")
if substring in mstring:
    print("Substring found")
else:
    print("Substring not found")


#Count Occurences of Words
#Count how many times a specific word appears in a sentence.   
sentence=input("enter a sentence:")
word=input("enter the word to search:")
words=sentence.split()
count=0
for w in words:
    if w==word:
        count+=1
print("The word",word,"appears",count,"time(s).")



#Password Validator
password=input("enter a password:")
upper=lower=digit=special=0
for ch in password:
    if ch.isupper():
        upper+=1
    elif ch.islower():
        lower+=1
    elif ch.isdigit():
        digit+=1
    else:
        special+=1
if len(password)>=8 and upper>=1 and lower>=1 and digit>=1 and special>=1:
    print("password is valid")
else:
    print("password is invalid")



#Run-Length Encoding 
# Program to compress a string using Run-Length Encoding
string=input("enter a string:")
result=""
count=1
for i in range(len(string)):
    if i < len(string) - 1 and string[i] == string[i + 1]:
        count+=1
    else:
        result = result + string[i] + str(count)
        count=1
print("compressed string:",result)


#String Compression
#Compress repeated characters and return the original string if compression does not reduce the length
string=input("Enter a string:")
compressed=""
count=1
for i in range(len(string)):
    if i < len(string) - 1 and string[i] == string[i + 1]:
        count+=1
    else:
        compressed = compressed + string[i] + str(count)
        count=1
if len(compressed) < len(string):
    print("compressed string:",compressed)
else:
    print("original string:",string)


#Most Frequent Character
#Find the character with the highest frequency     
string = input("enter a string:")
max_char=""
max_count=0
for ch in string:
    count=0
    for c in string:
        if ch==c:
            count+=1
    if count>max_count:
        max_count=count
        max_char=ch
print("character with highest freq:",max_char)
print("frequency:",max_count)



#Second Most Frequent Character
#Find the second most frequently occurring character. 
text=input("Enter a string: ")
freq={}
for ch in text:
    if ch!=" ":
        freq[ch]=freq.get(ch,0)+1
items=sorted(freq.items(),key=lambda x:x[1],reverse=True)
if len(items)>=2:
    print("Second most frequent character:",items[1][0])
else:
    print("No second most frequent character")



#Encrypt and decrypt a message using the Caesar Cipher algorithm. 
text=input("Enter the message:")
shift=int(input("Enter the shift value:"))
e=""
d=""
for ch in text:
    if ch.isalpha():
        if ch.isupper():
            e+=chr((ord(ch)-65+shift)%26+65)
        else:
            e+=chr((ord(ch)-97+shift)%26+97)
    else:
        e+=ch
print("encrypted message:", e)
for ch in e:
    if ch.isalpha():
        if ch.isupper():
            d+=chr((ord(ch)-65-shift)%6+65)
        else:
            d+=chr((ord(ch)-97-shift)%26+97)
    else:
        d+=ch
print("decrypted message:", d)



#Email Validator
#Validate whether a given email address follows a valid format. 
import re
email=input("Enter email: ")
pattern=r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
if re.match(pattern,email):
    print("Valid Email")
else:
    print("Invalid Email")


#Word Frequency Dictionary
#Count the frequency of every word in a paragraph.  
text=input("Enter a paragraph: ")
words=text.lower().split()
freq={}
for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
for word,count in freq.items():
    print(word,":",count)

#Sentence Reversal 
#Reverse the order of words in a sentence without changing the words themselves. 
sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_s = ""
for i in range(len(words) - 1, -1, -1):
    reversed_sentence += words[i] + " "
print("Reversed sentence:",reversed_s.strip())


#String Rotation
# Program to check whether one string is a rotation of another
str1=input("Enter first string:")
str2=input("Enter second string:")
if len(str1)==len(str2) and str2 in (str1+str1):
    print("String is a rotation")
else:
    print("String is not a rotation")