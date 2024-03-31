#strings are immutable
#upper(),lower(),strip(),rstrip(),replace(),split(),capitalize(),center(),count(),endswith(),find(),index()
#isalnum(),isalpha(),islower(),isprintable(),isspace(),istitle(),isupper(),startswith(),swapcase(),title()
str1="abddASDVSBasxdvSDvsd"
print(str1.upper())
print(str1.lower())
str2=" abcakjsbBIU NOIBboiu "
print(str2.strip())
str3="Hello !!!"
print(str3.rstrip("!"))
str4="bhavya is a bad boy"
print(str4.replace("bad","good"))
print(str4.split(" "))
print(str1.capitalize())
print(str3.center(50))
print(str3.center(50,"."))
print(str2.count("a"))
print(str3.endswith("!!!"))
