import math
phy=[15,12,8,8,7,7,7,6,5,3]
hist=[10,25,17,11,13,17,20,13,9,15]
mean_phy=sum(phy)/len(phy)
mean_hist=sum(hist)/len(phy)
num=0
for i in range(len(phy)):
    num=num+(phy[i]-mean_phy)*(hist[i]-mean_hist)
den=0
den1=0
den2=0
for i in range(len(phy)):
    den1=den1+pow(phy[i]-mean_phy,2)
    den2=den2+pow(hist[i]-mean_hist,2)

den=math.sqrt(den1*den2)
ans=num/den
print('%.3f' % (ans))
