# Compresser Calculation
T1=int(input())    # Temperature of air before compression
nc=0.88            # Efficiency of Compressor
R=0.287
Ma=50              # Mass flow rate of air
Cp1=1.005          # Specific heat at constant pressure
rp1=14              # Pressure ratio


T2= T1*rp1**(R/(Cp1*nc)) #Temperature after compression
print("Temperature of air after compression is",T2)

# Calculate Work done in Compressor
h1=0               # T1= T atm
Cp2=(1.02304)-(1.76021 * (10**-4) *T2) +(4.0205 *(10**-7)*(T2**2)) - (4.87272*(10**-11)*(T2**3))
print("Specific heat at constant pressure for air at T2=",Cp2) 
h2=Cp2 * (T2-T1) #Enthalpy at T2
print("Enthalpy at T2 =",h2)
Wc=Ma*(h2-h1)*nc    #Work Done Compressor
print("Work done =",Wc) 


# Combustion Chamber Calculation
ncc=0.995           #Efficiency of Combustion Chamber
LHV=42*10**6        #Lower Heating Value of Natural gas
he=1558.6568
hi=253.1383
mf=1.6225           # Fuel Mass Flow rate
me=51.6225          # Mass of Gases

Qcc=(me*he)-(Ma*hi)
print("Heat =",Qcc) #Heat produced by Combustion Chamber

# Turbine Calculation
T3=1500
nt=0.92
rp2=12.8703

T4=T3/(rp2**((R*nt)/Cp2)) # Temperature after Expansion
print("Temperature of air after Expansion =",T4)

# Calculate Work Done in Turbine
X0=150
V=35.77
Cpg1=(18.615 - (1.06857*(10**-3)*T3)+(9.2492*(10**-6)*(T3**2))-(4.3308*(10**-9)*(T3**3))+ X0*(0.1346-(4.32172*(10**-5)*T3) + (8.8895*(10**-8)*(T3**2))-(3.489*(10**-11)*(T3**3))))/V
h3=Cpg1*(T3-288.15)
print(Cpg1,h3)

Cpg2=(18.615 - (1.06857*(10**-3)*T4)+(9.2492*(10**-6)*(T4**2))-(4.3308*(10**-9)*(T4**3))+ X0*(0.1346-(4.32172*(10**-5)*T4) + (8.8895*(10**-8)*(T4**2))-(3.489*(10**-11)*(T4**3))))/V
h4=Cpg2*(T4-288.15)
print(Cpg2,h4)

Wt=me*(h3-h4)
print(Wt)




#Solar Power Calculation
P1=250
Hr=5
nsp=0.75

Psp=P1*Hr*nsp

N=Wc/Psp
print(N)

