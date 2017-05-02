# Problem 33

def nearly_equal(str1,str2):
 words=mutate(str2)
 print str1 in words

def mutate(word):
 l=len(word)
 alp=map(chr,range(97,123))
 ins=[word[:i]+x+word[i:] for i in range(l) for x in alp]
 repl=[word[:i]+x+word[i+1:] for i in range(l) for x in alp]
 dele=[word[:i]+word[i+1:] for i in range(l)]
 swa=[word[:i]+word[i+1]+word[i]+word[i+2:] for i in range(l-1)]
 oper=ins+repl+dele+swa
 return oper

nearly_equal('python','perl')
nearly_equal('perl','pearl')
nearly_equal('python','jython')
nearly_equal('man','woman')
  


