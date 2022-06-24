"""Faça um Programa que peça as 4 notas bimestrais e mostre a média."""
if __name__ == '__main__':
    nota1 = float(input('Digite a premeira nota do bimestre: '))
    nota2 = float(input('Digite a segunda nota do bimestre: '))
    nota3 = float(input('Digite a Terceira nota do bimestre: '))
    nota4 = float(input('Digite a Quarta nota do bimestre: '))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f'Sua media Bimestral é:', media)
