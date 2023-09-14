import characters,math

def test_alphabet(s,f=8000,o='hor'):
 achars=[(y,x+off*s+2) for off in range(26) for a in characters.draw(getattr(characters,chr(0x41+off)),s-1) for x,y in a];achars.sort()
 asarr=arraymodule.array('h',chr(0)*s*f)
 globfuncs=globals();globnames=globfuncs.keys();globnames.has_key('rendord_'+o);
 globfuncs['rendord_'+o](achars,asarr,s,f);
 return(asarr) 

#presume sorted by y
def rendord_list(data,out,h,o,f=4000,a=40,p=True):
 m=f/h;w=f+h;
 for x in range(int(h)):
  row=[];
  for c in range(len(data)):
   if (data[c][p and 1 or 0]==x):
    row.append(wavegen((h-data[c][not p and 1 or 0]-(h+o)*h)*w,a,m,f));
  for i in range(int(m)):
   for j in row:
    v=i+int(x*m);
    if (len(out)>v):
     n=math.ceil(out[v]+j[i]);
     if (n>16383):
      n=16383;
     elif (n<-16383):
      n=-16383
     out[v]=n
    else:
     for u in range(len(out),v):
      out.append(0); 
     out.append(math.ceil(j[i]));

# also needs sorted inputs;
def rendord_seq(data,out,height,offset=1,freq=4000,amp=40,p=True):
 m=(freq-height*(offset+height))/height;
 w=freq/2-(height+offset)*height;
 for x in range(height):
  row=[];
  for c in range(len(data)):
   for y in range(len(data[c])):
    if (data[c][y][p and 1 or 0]==x): 
     row.append([math.sin((height*len(data)-(c+1)*height*offset-data[c][y][not p and 1 or 0])/freq*2*math.pi*a/m)*amp for a in range(int(m))]);
  if (len(row)):
   for i in range(int(m)):
    contable(i,int(x*m),row,out=out);
 #pass iter

def contable(n,m,tabs,t=16383,out=None):
 n=(n!=None and (n,)) or range(out!=None and len(out) or m);
 if out==None:
  out=[0]*(len(n)+int(m));
 for o in n:
  r=0; 
  for j in range(len(tabs)):
   if (len(tabs[j])>o):
    r+=tabs[j][o];
    if (abs(r)>t):
     r=r%t; continue;
  #enditer2
  if (r!=0):
   if (len(out)<=int(o+m)):
    while (int(o+m)>len(out)):
     out.append(r);
   else:
    r=out[int(o+m)]+math.ceil(r);
    if (abs(r)>t):
     r%=t; out[int(o+m)]=r;
 return out;
    
def consintable(data,out=None):
  c=0;i=0;
  while (c<len(data)):
   while (i<m):
    i+=1;
    if (len(out)>i+c*m):
     w=out[i+x*m]+math.sin(2*math.pi/i+v);
     if(w>16383):
      w=16383;
     elif(w<-16383):
      w=-16383;
     out[i+x*m]=w;
    else:
     for u in range(len(out),i+x*m):
      out.append(0);
     out.append(math.ceil(math.sin(2*math.pi/i+v)))

def wavegen(freq,ampl,smpf,frat):
 return [math.sin(float(smpf*freq/frat)*2*math.pi*a/float(smpf))*ampl for a in range(int(smpf))]

def degenfourier(data,size):
 for i in size:
  yield math.sqrt(1/size*math.hypot(data[i*2],data[i*2+1]))

