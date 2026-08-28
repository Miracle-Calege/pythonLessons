
#faremos um import do modulo time
import time

#teremos o inicio
start_time = time.perf_counter()

#colocaremos o codigo aqui

for i in range(10000000):
    pass


#teremos o fim
end_time = time.perf_counter()


#teremos a diferença
elapsed = end_time - start_time

print(f"elapsed time:{elapsed} seconds")