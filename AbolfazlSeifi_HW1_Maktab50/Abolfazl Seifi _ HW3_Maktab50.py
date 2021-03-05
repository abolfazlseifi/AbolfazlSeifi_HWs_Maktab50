# Temperature conversion

temp= input("\nAre you convert Fahrenheit to Celsius (1) or Celsius to Fahrenheit (2): ")
if temp!="1" and temp!="2":
    print("\nYour choice was incorrect !!!\n")
elif temp == "1":
    x = int(input("\nHow is the weather? : "))
    y = float(((x * 9) / 5) + 32)
    print("\nYour Temperature is %.2f Celsius\n"%y)
elif temp == '2':
    x = int(input("\nHow is the weather? : "))
    z = float(((x - 32) * 5) / 9)
    print("\nYour Temperature is %.2f Fahernheit\n"%z)

# created by Abolfazl Seifi