#endswith and startswiths
s="hello this is bhanu"
print(s.endswith("bhanu"))
s="we using starts with method"
print(s.startswith("we"))
#here we using replace method
s="hello goodmorning"
print(s.replace("morning","evening"))
#here we are adding two strings
s="bhanu"+""+"prakash"
print(s)
#her we are finding length of the string
s="hi guys how are u?"
length=len(s)
print(length)
#"here we are doing a session on remoprefix and removesuffix"
s="this is a sample session of the removing perfix"
print(s.removeprefix("this"))
print(s.removesuffix("perfix"))
#here we are doing a session on the splitting of string
s="hello python"
print(s.split())
#here we are using strip,lstrip,rstrip to removing the spaces from the string
s="    uno collection everyday   "
print(s.strip())
print(s.lstrip())
print(s.rstrip())
#here we are using find and index of the string
s="hii this is bhanu"
print(s.index("bhanu"))
print(s.find("hii"))
#here this method is used to count the letters in the strng by usind count method
s="worlds wonderful natural"
print(s.count("w"))
#here we using slice method to print particular part in the string
s="hello everyone"
substring=s[0:3]
print(substring)