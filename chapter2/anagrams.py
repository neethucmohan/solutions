# Problem 36

def find_key(keys, word):
 for key in keys:
  if len(key) != len(word):
   continue
  elif sorted(list(key)) == sorted(list(word)):
   return key
  else:
   continue
   return None

def anagrams(lst):
 keys = []
 res = []
 for word in lst:
  key = find_key(keys, word)
  if key is not None:
   res[keys.index(key)].append(word)
  else:
   res.append([word])
   keys.append(word)
 return res 
   

print anagrams(['eat','ate','done','tea','soup','node'])
