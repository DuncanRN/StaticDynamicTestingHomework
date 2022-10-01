### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.


# FIND 6 issues with this code


```python

class CardGame:



  def check_for_ace(self, card):
    if card.value = 1: # This should be "=="
      return True
    else   # This needs a : at the end of the line
      return False
   

  dif highest_card(self, card1 card2): # def not dif 
                                      # AND missing a comma between card1 & card2
  if card1.value > card2.value:
    return card  # should return card1 not card
  else:
    return card2
  


def cards_total(self, cards):
  total # this should be total = 0
  for card in cards:
    total += card.value
    return "You have a total of" + total  # The indentation here is wrong, it will output this many times 
  
```
