import math
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
print("Specific heat at constant pressure for air at T2=",Cp2) 
h2=round(float(Cp2*(T2-T1)),4) #Enthalpy at T2
print("Enthalpy at T2 =",h2)
Wc=round(float(Ma*(h2-h1)),4) #Work Done Compressor
print("Work done =",Wc)

print("Fresnel Collector Calculations")
#Linear Fresnel Collector
l=44.8          #Length(m)
dn1=960         #Incident sunlight(w/m2)
theta=60
aw=16.56        #Aperture Width(m)
a=513.6         #Area(m2)
iaml=0.3        #Incidence angle modifier
iamt=0.75       #Incidence angle modifier
nlfc=0.61       #Efficiency


elf=round(float(1-(7.4/(1.7320*l))),4)
print("Energy Loss Factor=",elf)

qfcin=round(float(a*dn1*(iaml*iamt)*elf))
print("Qin=",qfcin)

qfco=round(float(qfcin*nlfc))
print("Qout=",qfco)

T3=round(float(T2+(qfco/(Ma*Cp2))))
print("T3=",T3)

print("Combustion Chamber Calculations")
# Combustion Chamber Calculation
T4=int(input("T4"))
ncc=0.995           #Efficiency of Combustion Chamber
LHV=42*10**6        #Lower Heating Value of Natural gas
X0=150
V=35.77
Cp4=round(float((18.615 - (1.06857*(10**-3)*T4)+(9.2492*(10**-6)*(T4**2))-(4.3308*(10**-9)*(T4**3))+ X0*(0.1346-(4.32172*(10**-5)*T4) + (8.8895*(10**-8)*(T4**2))-(3.489*(10**-11)*(T4**3))))/V),4)
Cp3=round(float((1.02304)-(1.76021 * (10**-4) *T3) +(4.0205 *(10**-7)*(T3**2)) - (4.87272*(10**-11)*(T3**3))),4)

he=round(float(Cp4*(T4-T1)))
hi=round(float(Cp3*(T3-T1)))

mf=round(float(Ma*(he-hi)/(LHV*ncc-he)))
me=Ma+mf

Qcc=round(float((me*he)-(Ma*hi)),4)
print("Heat =",Qcc,"J") #Heat produced by Combustion Chamber

print("Turbine Calculations")
# Turbine Calculation
nt=0.92
rp2=12.8703

T5=round(float(T4/(rp2**((R*nt)/Cp2))),4) # Temperature after Expansion
print("Temperature of air after Expansion =",T5,"K")

Cp5=round(float((18.615 - (1.06857*(10**-3)*T5)+(9.2492*(10**-6)*(T5**2))-(4.3308*(10**-9)*(T5**3))+ X0*(0.1346-(4.32172*(10**-5)*T5) + (8.8895*(10**-8)*(T5**2))-(3.489*(10**-11)*(T5**3))))/V),4)
h4=round(float(Cp4*(T4-288.15)),4)
h5=round(float(Cp5*(T5-288.15)),4)
print("Specific Heat at constant pressure at T4=",Cp4,"J/Kg K","Enthalpy(T4)",h4,"J")
print("Specific Heat at constant pressure at T5=",Cp5,"J/Kg K","Enthalpy(T5)",h5,"J")

Wt=round(float(me*(h4-h5)),4)
print("Work done =",Wt,"J")

#Efficiency
ncycle=round(float((Wt-Wc)/Qcc),4)
print("Hybrid Cycle Efficiency",ncycle,"%")





