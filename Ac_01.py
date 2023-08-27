def exercicio01(vl, au, inss):
    salario = float(vl)*float(au)
    liquido = round(salario-(salario*(float(inss)/100)),2)
    return liquido

def exercicio02(valor):
    novo_vl = valor-(valor*0.09)
    vl_desc = valor*0.09
    return [novo_vl, vl_desc]

def exercicio03(vl, desc):
    valor_promo = vl - desc
    return valor_promo

def exercicio04(vl):
    valor_tt = round(vl+(vl*0.10),2)
    gorjeta = round(vl*0.10,2)
    return [valor_tt, gorjeta]
