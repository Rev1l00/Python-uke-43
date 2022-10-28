import numpy as np
from playsound import playsound as ps

i = 1
max = 10
hemmeligTall = np.random.randint(1,2)

print("Finn ut hvilket tall jeg tenker på med færrest mulig gjett, fra 1 - 100!")
gjettetTall = int(input("Hvilket tall gjetter du? "))

while gjettetTall != hemmeligTall:
  if gjettetTall < hemmeligTall:      
    print("tallet du gjettet er for lavt, prøv igjen")

  else:
    print("tallet du gjettet er for høyt, prøv igjen")    
  gjettetTall = int(input("Hvilket tall gjetter du? "))
  i = i + 1
  if i == max:
    print ("Du har nådd maks antall forsøk, start på nytt")
    ps("Onsdag oppgaver uke 43\Sound_Effects\lose.wav") 
    break

if gjettetTall == hemmeligTall:
  print("du brukte", i, "forsøk på å gjette det riktige tallet")
  ps("Onsdag oppgaver uke 43\Sound_Effects\win.mp3")