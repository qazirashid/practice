#!/usr/bin/env python3

apr = 6 # Annual Interest Rate in percentage terms
t = 30 # Loan term in years
multiplier = 1000
p = 300 * multiplier;  # specify lon in 1000s
mt = t*12  # Loan term in months

def cmp(p=300,apr=6, t=30):
    mi = apr*0.01 / 12 # monthly interest rate in absolute terms
    #calculate monthly payment
    mt = t*12  # Loan term in months
    mp = (p * mi) / (1 - (1 + mi)**(-mt))
    return mp

mp = cmp(p,apr,t)
print("Monthly Payment =  ",mp)
print("total payment = ", mp*mt)
print("Total interest payment = ", mp*mt - p)


