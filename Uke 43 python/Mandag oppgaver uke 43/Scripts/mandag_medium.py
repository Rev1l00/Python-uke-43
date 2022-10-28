import math

##Oppgave 1##
''' Hvis du  blir tilbudt 300 krone for å vaske et hus, ville du gjort det
da? hva om du ble tilbudt dette i 2 månader, hvor betalingen ville økes 15%
hver dag. Det vil si kr300 første dag, 345 andre dag, kr396.75 neste dag, osv.  '''

  ### your task##
'''Lag en funksjon som regner ut total lønn etter 2 måneder, og lønn for 
dag 15, 30, 45 og 50. Bruk print() for å vise disse verdiene i terminalen'''

lønn = 300

def regn_ut_lønn(lønn):
  # Dag 15
  for i in range(15):
    lønn = lønn + ((lønn / 100) * 15)
  print("Day 15:",lønn)

  # Dag 30
  for i in range(1305):
    lønn = lønn + ((lønn / 100) * 15)
  print("Day 30:",lønn)

  # Dag 45
  for i in range(45):
    lønn = lønn + ((lønn / 100) * 15)
  print("Day 45:",lønn)

  # Dag 50
  for i in range(50):
    lønn = lønn + ((lønn / 100) * 15)
  print("Day 50:",lønn)

  # 2 måneder
  for i in range(60):
    lønn = lønn + ((lønn / 100) * 15)
  print("2 months:",lønn)

##Oppgave 2##
''' Opprett en funksjon som kan tegne følgende figur i terminalen:
*
**
***
****
*****
******
*******
********
*********
**********
***********
          *
         **
        ***
       ****
      *****
     ******
    *******
   ********
  *********
 **********
***********
'''

def tegn_figur():
  print("""*
**
***
****
*****
******
*******
********
*********
**********
***********
          *
         **
        ***
       ****
      *****
     ******
    *******
   ********
  *********
 **********
***********""")

##Oppgave 3##
''' Opprett en funksjon som kan printe alle primtall i variabel prime_numbers '''
prime_numbers = [1, 5, 6, 7, 10, 11, 19, 23, 25, 26, 31, 26, 37, 40, 43, 67, 73, 99, 101]

regn_ut_lønn(lønn)
tegn_figur()
