import math 

a = 5
b = 6
c = 2
d = 1

# level: easy

############## complete following exercices########

## Oppgave 1##
'''hvilken varibel bør summeres med a for å få 12? variabel "result" skal lagre verdien av operasjonen. Bruk funksjonen print() for å vise verdien til
result i terminalen'''

result = a + b + d
#print(result)

## Oppgave 2##
'''opprett en ny variabel (du kan gi hvilket som helst navn) som tar imot produktet til multiplikasjon mellom a og b minus c
deretter bruk funsjonen print() for å vise verdien til variabel i terminalen.'''

oppgave2 = a * b -c
print("Svaret er", oppgave2)

## Oppgave 3##
'''complete the following else statement og deretter opprett en elif statement.'''

z = 'spicy food'

if z =='spicy food':
    print('I love it!')
else:
    pass
    ## your implementation here


## Oppgave 4##

'''Opprett en funksjon som inneholder en for loop for å iterere alle elementer i variabel  year. Bruk funksjonen print() for å printe disse elementene'''
year = ['january', 'february', 'mars', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

## Oppgave 5##

'''opprett en funksjon som printer KUN de elementene av variabel "prime_tall" som IKKE er partall.  '''
prime_tall = [1, 3, 2, 5, 8, 49, 0, 15, 212, 13, 176, 21, 7, 29, 20, 14]

def is_prime(prime_tall):
  for number in prime_tall:
    for i in range(2,int(math.sqrt(number))+1):
        if (number%i) == 0:
            print(number)

is_prime(prime_tall)
