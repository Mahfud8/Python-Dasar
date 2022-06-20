def my_spells(spellnum):
  num = spellnu
  spells = ['Obliviate', 'Sectumsempra', 'Avada Kedavra', 
            'Alohomora', 'Lumos', 'Expecto Patronum',
            'Wingardium Leviosa', 'Accio', 'Expelliarmus']
  print(spells[num % 9], end=" ")

print(my_spells(0))