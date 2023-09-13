import re

vowel=("o","e","a","i","u")

class _what(dict):
  """sentimpiece simple"""
  _verb=("is","too","as","be")
  def un(self,*arguments):
   for arg in range(len(rguments)):
     argument=arguments[arg]
     ad=[
   sum([ n.end()+(1 if(v>1 and n.end) else -1)
      for n in re.findall(vowel[v],argument[i:])])
 for i in range(len(argument)) for v in range(len(vowel))
   for o in (list(re.findall("|".join(vowel),argument[i])),)]
     yield(sorted(ad))
  """un-adjunct word sentiment"""
