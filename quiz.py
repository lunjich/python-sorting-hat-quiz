print('welcome to the sorting house quiz!')

Gryffindor = 0
Hufflepuff = 0
Ravenclaw = 0
Slytherin = 0

Q1 = input('Q1) Do you like Dawn or Dusk? '
'1) Dawn '
'2) Dusk')
if Q1 == '1':
    Gryffindor = Gryffindor + 1
    Ravenclaw = Ravenclaw + 1
elif Q1 == '2':
    Slytherin = Slytherin + 1
    Hufflepuff = Hufflepuff + 1
  
Q2 = input('Q2) When I’m dead, I want people to remember me as:'
    '1) The Good'
    '2) The Great'
    '3) The Wise'
    '4) The Bold')

if Q2 == '1':
    Hufflepuff = Hufflepuff + 2;
elif Q2 == '2':
    Slytherin = Slytherin + 2;
elif Q2 == '3':
    Ravenclaw = Ravenclaw + 2;
elif Q2 == '4':
    Gryffindor = Gryffindor + 2;
else:
    print('Invalid input')

Q3 = input('Q3) Which kind of instrument most pleases your ear?'
        '1) The violin'
        '2) The trumpet'
        '3) The piano'
        '4) The drum')
  
if Q3 == '1':
    Slytherin = Slytherin + 4;
elif Q3 == '2':
    Hufflepuff = Hufflepuff + 4;
elif Q3 == '3':
    Ravenclaw = Ravenclaw + 4;
elif Q3 == '4':
    Gryffindor = Gryffindor + 4;
else:
    print('Invalid input')

final = max(Gryffindor, Hufflepuff, Ravenclaw, Slytherin)
if final == Gryffindor:
    print('You belong to Gryffindor')
elif final == Hufflepuff:
    print('You belong to Hufflepuff')
elif final == Ravenclaw:
    print('You belong to Ravenclaw')
else: 
    print('You belong to Slytherin')


#uhhh end
