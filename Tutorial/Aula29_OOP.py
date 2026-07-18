from carro import Carro

carro=Carro("Roll & Royce",2018,"Preto",False)
carro1=Carro("Ferrari",2018,"Vermelho",False)
carro2=Carro("Mercedes Maybach",2018,"Preto",True)


print(carro.modelo)
print(carro.ano)
print(carro.cor)
print(carro.aVenda)

carro1.conduzir()
carro1.parar()
carro2.conduzir()
carro2.parar()
carro.caracteristicas()
carro1.caracteristicas()
carro2.caracteristicas()