#
### Hier Integer & Strings mit Typkonvertierung
txt = 'Hallo IHR'
print (txt)


x:int = 5
y:float = 7.34
sum = x + y
print (sum)
print (type(x))
print (str(x))

print (type(y))
print (type(sum))

x = "Danke, hat Spaß gemacht"

print (type(x))

## Boolsche Werte

isLoggedIn = True
wert1 = 100
wert2 = 23
if (wert1 > wert2):
        print ("wert1 ist größer als wert2")
else:
        print ("wert1 ist kleiner als wert2")

a = False

if(a == True):
    print("Nutzer eingeloggt")
else:
    print ("Nutzer NICHT eingeloggt")

Kind = 15

if (Kind < 6):
    print ("Du gehst um 7 ins Bett")
elif ((Kind > 6) & (Kind < 12)):
    print ("Du gehst um 22 Uhr ins Bett")
else: 
    print ("Mach das Licht aus, wenn du nach Hause kommst")
