#Lista 1 (adicional) ex 2

segs = (int(input("Por favor, entre com o número de segundos que deseja converter:")))

dias = segs // 86400
segs_restantes1 = segs % 86400
horas = segs_restantes1 // 3600
segs_restantes2 = segs_restantes1 % 3600
minutos = segs_restantes2 // 60
segundos = segs_restantes2 % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")