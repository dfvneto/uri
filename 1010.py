line1=input().split()
line2=input().split()
p1,q1,v1 = line1
p2,q2,v2 = line2
total = int(q1)*float(v1)+int(q2)*float(v2)
print("VALOR A PAGAR: R$ %.2f" % total)