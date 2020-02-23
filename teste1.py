

Segundos = int (input ( " Por favor, digite a quantidade de segundos: "))

Dias = Segundos // (3600*24)
TempoRestante = Segundos % (3600*24)
Horas = TempoRestante // 3600
TempoRestante = TempoRestante % 3600
Minutos = TempoRestante // 60
Segundos = TempoRestante % 60

print ( Dias , 'dias', Horas, 'horas', Minutos , 'minutos e', Segundos, "segundos .")

