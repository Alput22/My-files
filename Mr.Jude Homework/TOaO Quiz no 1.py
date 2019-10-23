#%%
Almada Putra A.

1.  a. The parent class is Spell and the child class is Accio and Confundo

    b. The code prints out:
        Accio
        Summoning Charm Accio
        No description
        Confundus Charm Confundo
        Causes the victim to become confused and befuddled.
    
    c. The get description method called is the one on the Confundo class
       because it overrides the get description from the super class Spell
    
    d. We need to add a get description function to Accio so that it overrides
       the one in th class Spell
       Example code :
          class Accio(Spell):
              def __init__(self):
                  Spell.__init__(self, 'Accio', 'Summoning Charm')
              def get_description(self):
                  return 'This charm summons an object to the caster, potentially over a significant distance'
