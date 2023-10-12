"""
 Diseñar un programa para calcular el impuesto sobre la renta (ISR) correspondiente a un sueldo mensual dado. El ISR se calcula usando la tarifa de la siguiente tabla.
 750722.
"""

sueldo = float(input("Ingrese el sueldo mensual: "))

if sueldo <= 3644.94: #Excedente
    excedente = sueldo - 0.01
    impuesto_marginal = excedente + 0.1
    isr = impuesto_marginal + 12.88
elif  sueldo >=3644.95 and sueldo <= 7446.19:
    excedente = sueldo - 3644.95
    impuesto_marginal = excedente + 0.2
    isr = impuesto_marginal + 303.76
elif sueldo >= 7446.20 and sueldo <=10298.35:
    excedente = sueldo - 7446.20
    impuesto_marginal = excedente * 0.3
    isr = impuesto_marginal + 1063.92
else:
    excedente = sueldo - 10298.36
    impuesto_marginal = excedente * 0.35
    isr = impuesto_marginal + 3327.42

print("ISR: ", isr)
