import tkinter as tk
import random
import math
def m5_algorithm(loc,c,n,k):
    arr=[]
    for i in range(0,n):
        for j in range(i+1,n):
            L=float(loc[j])-float(loc[i])
            arr.append(L)
    arr.sort()
    for L in arr:
        cap=[]
        step=0
        facility=0
        while(step<n and facility<k):
            facility+=1
            temp=step
            for m in range (step,min(n,step+c)):
                if float(loc[m])>float(loc[step])+L:
                    break
                else:
                    temp+=1
            step=temp
            cap.append(step)
        if step==n:
            return L,cap

def algorithm_1(loc,cap,n,k):
    rows, cols = (n, pow(2,k))
    L=[]
    C=[]
    for i in range(rows):
        col = []
        col_1=[]
        for j in range(cols):
            col.append(1)
            col_2=[]
            for m in range (k):
                col_2.append(0)
            col_1.append(col_2)
        L.append(col)
        C.append(col_1)
    for i in range (0,n):
        for j in range (0,k):
            for w in range (1,pow(2,k)):
                if i==int(cap[j])-1 and w==pow(2,j):
                    L[i][w]=float(loc[i])-float(loc[0])
                    C[i][w][0]=int(cap[j])
                elif C[i-int(cap[j])][w-pow(2,j)].count(int(cap[j]))==0:
                    temp=max(L[i-int(cap[j])][w-pow(2,j)],float(loc[i])-float(loc[i-int(cap[j])+1]))
                    if L[i][w]>temp:
                        L[i][w]=temp
                        for q in range (k):
                            if C[i-int(cap[j])][w-pow(2,j)][q]!=0:
                                C[i][w][q]=C[i-int(cap[j])][w-pow(2,j)][q]
                            else:
                                C[i][w][q]=int(cap[j])
                                break
    return L[n-1][pow(2,k)-1],C[n-1][pow(2,k)-1]

def ec():
    def median():
        cv.delete('all')
        locations=X.get().split(',')
        c=int(C.get().split(',')[0])
        for i,x in enumerate(X.get().split(',')):
            if i%(c/2)==0 and i%c!=0:
                draw_facility(ec_window,cv,x)
            if (i+1)%c==0 and i!=0:
                draw_allocation(ec_window,cv,locations[i+1-c],locations[i])
        initalize()

    def m1():
        cv.delete('all')
        locations=X.get().split(',')
        c=int(C.get().split(',')[0])
        draw_facility(ec_window,cv,locations[int(k.get())//2*c-1])
        draw_facility(ec_window,cv,locations[int(k.get())//2*c])
        for i,x in enumerate(X.get().split(',')): 
            if (i+1)%c==0 and i!=0:
                draw_allocation(ec_window,cv,locations[i+1-c],locations[i])
        k_int=int(k.get())
        temp_f=float(locations[k_int//2*c-1])
        for i in range(k_int//2*c-2,0,-1): 
            if (i+1)%c==0 and i!=0:
                if temp_f>=float(locations[i]) and 2*float(locations[i+1])>=temp_f:
                    temp=min(float(locations[i]),2*float(locations[i+1])-temp_f)
                    draw_facility(ec_window,cv,temp)
                    temp_f=temp
        temp_f=float(locations[k_int//2*c])
        for i in range(k_int//2*c+1,int(n.get()),1): 
            if i%c==0:
                if temp_f<=float(locations[i]) and 2*float(locations[i-1])<=1+temp_f:
                    temp=max(float(locations[i]),2*float(locations[i-1])-temp_f)
                    draw_facility(ec_window,cv,temp)
                    temp_f=temp
        initalize()

    def m2():
        cv.delete('all')

        locations=X.get().split(',')
        c=int(C.get().split(',')[0])
        draw_facility(ec_window,cv,locations[int(k.get())//2*c-1])
        draw_facility(ec_window,cv,locations[int(k.get())//2*c])
        k_int=int(k.get())
        temp_f=float(locations[k_int//2*c-1])
        for i in range(k_int//2*c-2,0,-1): 
            if (i+1)%c==0 and i!=0:
                if temp_f>=float(locations[i])and 2*float(locations[i+1])>=temp_f:
                    temp=min(float(locations[i]),2*float(locations[i+1])-temp_f)
                    draw_facility(ec_window,cv,temp)
                    temp_f=temp
                if 2*float(locations[i+1])<temp_f:
                    draw_facility(ec_window,cv,0)
                    break

        temp_f=float(locations[k_int//2*c])
        for i in range(k_int//2*c+1,int(n.get()),1): 
            if i%c==0:
                if temp_f<=float(locations[i]) and 2*float(locations[i-1])<=1+temp_f:
                    temp=max(float(locations[i]),2*float(locations[i-1])-temp_f)
                    draw_facility(ec_window,cv,temp)
                    temp_f=temp
                if 2*float(locations[i+1])>1+temp_f:
                    draw_facility(ec_window,cv,1)
                    break

        initalize()

    def m3():
        cv.delete('all')
        locations=X.get().split(',')
        arrival=R.get().split(',')
        c=int(C.get().split(',')[0])
        draw_facility(ec_window,cv,locations[int(k.get())//2*c-1])
        draw_facility(ec_window,cv,locations[int(k.get())//2*c])
        for i,x in enumerate(X.get().split(',')): 
            if (i+1)%c==0 and i!=0:
                draw_allocation(ec_window,cv,locations[i+1-c],locations[i])
                draw_time(ec_window,max(arrival),locations[i+1-c],locations[i])
        k_int=int(k.get())
        temp_f=float(locations[k_int//2*c-1])
        for i in range(k_int//2*c-2,0,-1): 
            if (i+1)%c==0 and i!=0:
                if temp_f>=float(locations[i]) and 2*float(locations[i+1])>=temp_f:
                    temp=min(float(locations[i]),2*float(locations[i+1])-temp_f)
                    draw_facility(ec_window,cv,temp)
                    temp_f=temp
        temp_f=float(locations[k_int//2*c])
        for i in range(k_int//2*c+1,int(n.get()),1): 
            if i%c==0:
                if temp_f<=float(locations[i]) and 2*float(locations[i-1])<=1+temp_f:
                    temp=max(float(locations[i]),2*float(locations[i-1])-temp_f)
                    draw_facility(ec_window,cv,temp)
                    temp_f=temp
        initalize()
    def m4():
        cv.delete('all')
        locations=X.get().split(',')
        arrival=R.get().split(',')
        c=int(C.get().split(',')[0])
        draw_facility(ec_window,cv,locations[int(k.get())//2*c])
        initalize()

    def initalize():
        point_L=[(100,200),(800,200)]
        labe_S = tk.Label(ec_window,text="0")
        labe_S .place(x=95,y=220)
        labe_E = tk.Label(ec_window,text="1")
        labe_E .place(x=795,y=220)
        point_S=[(100,180),(100,200)]
        point_E=[(800,180),(800,200)]
        line_L=cv.create_line(point_L,fill="black",width=5)
        line_S=cv.create_line(point_S,fill="black",width=5)
        line_E=cv.create_line(point_E,fill="black",width=5)
        print(line_L,line_E,line_S)
        for x in X.get().split(','):
            draw_agent(ec_window,cv,x)


        
    ec_window=tk.Tk()
    ec_window.title('Equal Capacity Setting')
    ec_window.geometry('900x600')
    ec_window['background'] = 'blue'

    cv = tk.Canvas(ec_window, bg="white", width=900, height=400)
    cv.place(x=0,y=0)

    button4=tk.Button(ec_window,text="Median Mechanism",command=median)
    button4.place(x=0,y=500)
    button5=tk.Button(ec_window,text="Mechanism 1",command=m1)
    button5.place(x=150,y=500)
    button6=tk.Button(ec_window,text="Mechanism 2",command=m2)
    button6.place(x=300,y=500)
    button7=tk.Button(ec_window,text="Mechanism 3",command=m3)
    button7.place(x=450,y=500)
    button7=tk.Button(ec_window,text="Mechanism 4",command=m4)
    button7.place(x=600,y=500)

    
    ec_window.mainloop()

def draw_agent(window,cv,location):
    point_X=[(100+700*float(location),150),(100+700*float(location),200)]
    line_x=cv.create_line(point_X,fill="red",width=5)
    print(line_x)
    labe_S = tk.Label(window,text=location)
    labe_S .place(x=95+700*float(location),y=220)

def draw_allocation(window,cv,location_1,location_2):
    point_X=[(100+700*float(location_1),100),(100+700*float(location_2),100)]
    line_x=cv.create_line(point_X,arrow="both",dash=(1,1),fill="green",width=5)
    print(line_x)

def draw_time(window,time,location_1,location_2):
    labe_S = tk.Label(window,text=time)
    labe_S .place(x=95+700*(float(location_1)+float(location_2))/2,y=100)

def draw_facility(window,cv,location):
    point_X=[(100+700*float(location),130),(100+700*float(location),200)]
    line_x=cv.create_line(point_X,arrow='first',fill="blue",width=5)
    print(line_x)
    labe_S = tk.Label(window,text=location)
    labe_S .place(x=95+700*float(location),y=220)



def sc():

    def m5():
        r=random.random()
        cv.delete('all')
        locations=X.get().split(',')
        c=int(C.get().split(',')[0])
        L,alc=m5_algorithm(locations,c,int(n.get()),int(k.get()))
        labe_number = tk.Label(sc_window,text="L="+f'{L:.1f}')
        labe_number.place(x=95,y=50)
        temp=0
        for allo in alc: 
            draw_allocation(sc_window,cv,temp,locations[allo-1])
            if r>0.5:
                draw_facility(sc_window,cv,temp)
            else:
                s=f'{float(temp)+L:.1f}'
                draw_facility(sc_window,cv,s)
            temp=locations[min(int(n.get())-1,allo)]
        initalize()

    def initalize():
        point_L=[(100,200),(800,200)]
        labe_S = tk.Label(sc_window,text="0")
        labe_S .place(x=95,y=220)
        labe_E = tk.Label(sc_window,text="1")
        labe_E .place(x=795,y=220)
        point_S=[(100,180),(100,200)]
        point_E=[(800,180),(800,200)]
        line_L=cv.create_line(point_L,fill="black",width=5)
        line_S=cv.create_line(point_S,fill="black",width=5)
        line_E=cv.create_line(point_E,fill="black",width=5)
        print(line_L,line_E,line_S)
        for x in X.get().split(','):
            draw_agent(sc_window,cv,x)


        
    sc_window=tk.Tk()
    sc_window.title('Spare Capacity Setting')
    sc_window.geometry('900x600')
    sc_window['background'] = 'blue'

    cv = tk.Canvas(sc_window, bg="white", width=900, height=400)
    cv.place(x=0,y=0)


    button5=tk.Button(sc_window,text="Mechanism 5",command=m5)
    button5.place(x=150,y=500)
    
    sc_window.mainloop()

def draw_agent(window,cv,location):
    point_X=[(100+700*float(location),150),(100+700*float(location),200)]
    line_x=cv.create_line(point_X,fill="red",width=5)
    print(line_x)
    labe_S = tk.Label(window,text=location)
    labe_S .place(x=95+700*float(location),y=220)

def draw_allocation(window,cv,location_1,location_2):
    point_X=[(100+700*float(location_1),100),(100+700*float(location_2),100)]
    line_x=cv.create_line(point_X,arrow="both",dash=(1,1),fill="green",width=5)
    print(line_x)

def draw_time(window,time,location_1,location_2):
    labe_S = tk.Label(window,text=time)
    labe_S .place(x=95+700*(float(location_1)+float(location_2))/2,y=100)

def draw_facility(window,cv,location):
    point_X=[(100+700*float(location),130),(100+700*float(location),200)]
    line_x=cv.create_line(point_X,arrow='first',fill="blue",width=5)
    print(line_x)
    labe_S = tk.Label(window,text=location)
    labe_S .place(x=95+700*float(location),y=220)



def ac():

    def m6():
        r=random.random()
        cv.delete('all')
        locations=X.get().split(',')
        c=[]
        for capacity in C.get().split(','):
            c.append(int(capacity))
        L,G=algorithm_1(locations,c,int(n.get()),int(k.get()))
        labe_number = tk.Label(ac_window,text="L="+f'{L:.1f}')
        labe_number.place(x=95,y=50)
        temp=0
        for g in G:
            draw_allocation(ac_window,cv,locations[temp],locations[temp+g-1])
            if r>0.5:
                draw_facility(ac_window,cv,locations[temp])
            else:
                s=f'{float(locations[temp])+L:.1f}'
                draw_facility(ac_window,cv,s)
            temp+=g
        initalize()

    def m7():
        r=random.random()
        cv.delete('all')
        locations=X.get().split(',')
        c=[]
        for capacity in C.get().split(','):
            c.append(int(capacity))
        arrival=R.get().split(',')
        L,G=algorithm_1(locations,c,int(n.get()),int(k.get()))
        labe_number = tk.Label(ac_window,text="L="+f'{L:.1f}')
        labe_number.place(x=95,y=50)
        temp=0
        for g in G:
            draw_allocation(ac_window,cv,locations[temp],locations[temp+g-1])
            draw_time(ac_window,max(arrival),locations[temp],locations[temp+g-1])
            if r>0.5:
                draw_facility(ac_window,cv,locations[temp])
            else:
                s=f'{float(locations[temp])+L:.1f}'
                draw_facility(ac_window,cv,s)
            temp+=g
        
        initalize()


    def initalize():
        point_L=[(100,200),(800,200)]
        labe_number = tk.Label(ac_window,text="L=0.2")
        labe_number.place(x=95,y=50)
        labe_S = tk.Label(ac_window,text="0")
        labe_S .place(x=95,y=220)
        labe_E = tk.Label(ac_window,text="1")
        labe_E .place(x=795,y=220)
        point_S=[(100,180),(100,200)]
        point_E=[(800,180),(800,200)]
        line_L=cv.create_line(point_L,fill="black",width=5)
        line_S=cv.create_line(point_S,fill="black",width=5)
        line_E=cv.create_line(point_E,fill="black",width=5)
        print(line_L,line_E,line_S)
        for x in X.get().split(','):
            draw_agent(ac_window,cv,x)


        
    ac_window=tk.Tk()
    ac_window.title('Arbitrary Capacity Setting')
    ac_window.geometry('900x600')
    ac_window['background'] = 'blue'

    cv = tk.Canvas(ac_window, bg="white", width=900, height=400)
    cv.place(x=0,y=0)


    button6=tk.Button(ac_window,text="Mechanism 6",command=m6)
    button6.place(x=150,y=500)
    button7=tk.Button(ac_window,text="Mechanism 7",command=m7)
    button7.place(x=300,y=500)
    
    ac_window.mainloop()

def draw_agent(window,cv,location):
    point_X=[(100+700*float(location),150),(100+700*float(location),200)]
    line_x=cv.create_line(point_X,fill="red",width=5)
    print(line_x)
    labe_S = tk.Label(window,text=location)
    labe_S .place(x=95+700*float(location),y=220)

def draw_allocation(window,cv,location_1,location_2):
    point_X=[(100+700*float(location_1),100),(100+700*float(location_2),100)]
    line_x=cv.create_line(point_X,arrow="both",dash=(1,1),fill="green",width=5)
    print(line_x)

def draw_time(window,time,location_1,location_2):
    labe_S = tk.Label(window,text=time)
    labe_S .place(x=95+700*(float(location_1)+float(location_2))/2,y=100)

def draw_facility(window,cv,location):
    point_X=[(100+700*float(location),130),(100+700*float(location),200)]
    line_x=cv.create_line(point_X,arrow='first',fill="blue",width=5)
    print(line_x)
    labe_S = tk.Label(window,text=location)
    labe_S .place(x=95+700*float(location),y=220)



root = tk.Tk()
root.title('Final Year Project Demonstration')
root.geometry('900x600')
root['background']='white'
text=tk.Label(root,text="Please input the variables",fg="black",font=('Times', 20, 'bold italic'))
text.place(x=0,y=0)

labe_n = tk.Label(root,text="The number of agents n：",anchor="w")
labe_n.place(x=0,y=50)

labe_X = tk.Label(root,text="The location profile X ：")
labe_X .place(x=0,y=100)
labe_X2 = tk.Label(root,text="Please input values in an increasing order and separate them by commas, e.g. 0.1,0.2,0.3")
labe_X2.place(x=0,y=150)

labe_R = tk.Label(root,text="The arrival stage profile R ：")
labe_R .place(x=0,y=200)
labe_R2 = tk.Label(root,text="Please input values corresponding to X and separate them by commas, e.g. 1,0,2：")
labe_R2.place(x=0,y=250)

labe_k = tk.Label(root,text="The number of facilities k：",anchor="w")
labe_k.place(x=0,y=300)

labe_C = tk.Label(root,text="The capacity constraints C ：")
labe_C .place(x=0,y=350)
labe_C2 = tk.Label(root,text="Please separate values by commas, e.g. 3,3,3")
labe_C2.place(x=0,y=400)

n_e=tk.Entry(root)
n=tk.StringVar()
n_e["textvariable"] = n
n_e.place(x=400,y=50)


X_e=tk.Entry(root)
X=tk.StringVar()
X_e["textvariable"] = X
X_e.place(x=400,y=100)


R_e=tk.Entry(root)
R=tk.StringVar()
R_e["textvariable"] = R
R_e.place(x=400,y=200)


k_e=tk.Entry(root)
k=tk.StringVar()
k_e["textvariable"] = k
k_e.place(x=400,y=300)

C_e=tk.Entry(root)
C=tk.StringVar()
C_e["textvariable"] = C
C_e.place(x=400,y=350)

end=500

button1=tk.Button(root,text="Equal Capacity",command=ec)
button1.place(x=0,y=end)
button2=tk.Button(root,text="Spare Capacity",command=sc)
button2.place(x=200,y=end)
button3=tk.Button(root,text="Arbitrary Capacity",command=ac)
button3.place(x=400,y=end)




root.mainloop()