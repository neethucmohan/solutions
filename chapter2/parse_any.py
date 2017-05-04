# Problem 31

def parse(fname,d,c):
    lines=open(fname).readlines()
    i=0
    print lines
    while i<len(lines):
	  cond=c in lines[i]
          if cond==False:
             lines[i]=lines[i].strip()
             print lines[i]
             lines[i]=lines[i].split(d)
             i=i+1
	  else:
		lines.pop(i)
          
    return lines
print parse('p.txt','!','#') 
