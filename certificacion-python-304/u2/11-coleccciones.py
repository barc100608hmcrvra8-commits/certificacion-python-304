run_run=[]
n = int(input("ingresa el numero de productos para tu run run: "))
for i in range(n):
    p=input("ingresa el producto a tu rn run: ")
    run_run.append(p)

print("lista creada correcta mente")
run_run[0]="barritas"

print(run_run[0])
print(run_run[1])
print(run_run)