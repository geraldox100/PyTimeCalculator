PyTimeCalculator
================

Não é uma biblioteca, muito menos um framework. Apenas um conjunto de classes que permite definir uma janela de cálculo de tempo entre dois períodos.

A classe Janela permite definir a janela da maneira que for mais conveniente, como uma janela de trabalho, onde a jornada é de 08h com intervalo as 12h, retorno as 14h e finalizando as 18h.

Depois basta utilizar a calculadora para obter a diferença de tempo entre dois períodos.


````
window = BusinessWindow()
window.add_period(8, 12) 
window.add_period(14, 18)
        
calc = Calculator()

initial = datetime.datetime(2010, 07, 16, 8, 0, 0)
final = datetime.datetime(2010, 07, 16, 18, 0, 0)
        
time = calc.time_between(initial, final, self.window)
print time.days, time.hours, time.minutes
                
````


Este projeto também esta disponível em Java neste <a href="https://github.com/geraldox100/JTimeCalculator/">link</a>.
