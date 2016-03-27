import xml.etree.ElementTree


def myFloat(myList):
    return  [int(n,16) for n in myList]

e = xml.etree.ElementTree.parse('data.xml').getroot()

f = open('data.txt', 'r')
x = f.readlines()
w=[];
k=[];
for p in x:
	a=p.split();
	w.append(a);

for chile in e:
	k.append( (str(int(chile.find('pageno').text)+1)) +" "+ chile.get('title'));
print k;
for g in k:
	s=g.split();
	num=s[0];
	for d in w:
		#print d[1]+" "+num
		if((d[1]) == num):
			print "#define "+d[0]+"//"+g;





