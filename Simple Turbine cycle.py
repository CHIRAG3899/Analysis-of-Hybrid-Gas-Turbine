print("Compressor Calculations")
# Compresser Calculation
T1=288.15   # Temperature of air before compression
nc=0.88            # Efficiency of Compressor
R=0.287
Ma=50              # Mass flow rate of air
Cp1=1.005          # Specific heat at constant pressure
rp1=int(input("Enter Rp"))               # Pressure ratio


T2= round(float(T1*rp1**(R/(Cp1*nc))),4) #Temperature after compression
print("Temperature of air after compression is",T2,"K")

# Calculate Work done in Compressor
h1=0               # T1= T atm
Cp2=round(float((1.02304)-(1.76021 * (10**-4) *T2) +(4.0205 *(10**-7)*(T2**2)) - (4.87272*(10**-11)*(T2**3))),4)
print("Specific heat at constant pressure for air at T2=",Cp2,"J/Kg K") 
h2=round(float(Cp2 * (T2-T1)),4) #Enthalpy at T2
print("Enthalpy at T2 =",h2,"J")
Wc=round(float(Ma*(h2-h1)),4) #Work Done Compressor
print("Work done =",Wc,"J") 

print("Combustion Chamber Calculations")
# Combustion Chamber Calculation
ncc=0.995           #Efficiency of Combustion Chamber
LHV=42*10**6        #Lower Heating Value of Natural gas
he=1558.6568
hi=253.1383
mf=1.6225           # Fuel Mass Flow rate
me=51.6225          # Mass of Gases me=ma+mf

Qcc=round(float((me*he)-(Ma*hi)),4)
print("Heat =",Qcc,"J") #Heat produced by Combustion Chamber

print("Turbine Calculations")
# Turbine Calculation
T3=int(input("Enter T3"))
nt=0.92
rp2=12.8703

T4=round(float(T3/(rp2**((R*nt)/Cp2))),4) # Temperature after Expansion
print("Temperature of air after Expansion =",T4,"K")

# Calculate Work Done in Turbine
X0=150
V=35.77
Cpg1=round(float((18.615 - (1.06857*(10**-3)*T3)+(9.2492*(10**-6)*(T3**2))-(4.3308*(10**-9)*(T3**3))+ X0*(0.1346-(4.32172*(10**-5)*T3) + (8.8895*(10**-8)*(T3**2))-(3.489*(10**-11)*(T3**3))))/V),4)
h3=round(float(Cpg1*(T3-288.15)),4)
print("Specific Heat at constant pressure at T3=",Cpg1,"J/Kg K","Enthalpy(T3)",h3,"J")

Cpg2=round(float((18.615 - (1.06857*(10**-3)*T4)+(9.2492*(10**-6)*(T4**2))-(4.3308*(10**-9)*(T4**3))+ X0*(0.1346-(4.32172*(10**-5)*T4) + (8.8895*(10**-8)*(T4**2))-(3.489*(10**-11)*(T4**3))))/V),4)
h4=round(float(Cpg2*(T4-288.15)),4)
print("Specific Heat at constant pressure at T4=",Cpg2,"J/Kg K","Enthalpy(T4)",h4,"J")

Wt=round(float(me*(h3-h4)),4)
print("Work done =",Wt,"J")

#Efficiency
ncycle=round(float((Wt-Wc)/Qcc),4)
print("Cycle Efficiency",ncycle,"%")

