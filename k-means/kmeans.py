from sklearn.cluster import KMeans
import pandas as pd
from sklearn .preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

df=pd.read_csv("unsup1.csv")
#print(df.head())
y=np.array(df['x1'])
x=np.array(df['x2'])
plt.scatter(x,y)
#plt.show()
k=6
centroids=[]
iteration=0
mu=np.array([[3000,2000],[2000,5000],[2000,700],[800,6000],[4000,7612],[9999,1234]])
colors=['b','g','r','c','m','y']
n=5000
def plot(sets,x,y,mu):
    for i in range(n):
        for t in range(k):
            if(sets[i]==t):
                plt.scatter(x[i],y[i],label='skitscat', color=colors[t],s=1.5)
    plt.show()
    #plt.pause(0.8)
        
def dist(a,b):
    return np.linalg.norm(a-b)

def convergence(c,i):
    #print("converging")
    #print(c)
    if(i<2*k):
        return False
    else:
        ans=True
        for t in range(k):
            if(c[i-2*(k-t)][0]==c[i-(k-t)][0] and c[i-2*(k-t)][1]==c[i-(k-t)][1]):
                ans=True
            else:
                return False
        return ans
        

def k_means(c,i,k,mu):
    #print("out")
    while(i<4000):
       # print("in")
       
        sets=[]
        for t in range(k):
            c.append(mu[t])
        for j in range(n):
            mini=1e6
            m=0
            for t in range(k):
                if dist(np.array([x[j],y[j]]),mu[t])<mini:
                    mini=dist(np.array([x[j],y[j]]),mu[t])
                    m=t
            sets.append(m)
        print(sets)

        for t in range(k):
            x1=0
            y1=0
            no=0
            for j in range(n):
                if sets[j]==t:
                    x1+=x[j]
                    y1+=y[j]
                    no+=1
            if(no>0):
                mu[t]=[x1/no,y1/no]
        
        i+=k
        
        ani=FuncAnimation(plt.gcf(),plot(sets,x,y,mu), interval=10,blit=False, repeat=False)
        
k_means(centroids,iteration,k,mu)
print(centroids[iteration-2])
print(centroids[iteration-1])
                
        
        
