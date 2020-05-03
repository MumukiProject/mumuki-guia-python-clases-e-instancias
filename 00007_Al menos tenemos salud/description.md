Quizá hayas notado que nuestra clase `Zombi` tiene, al igual que tuvieron los objetos `Bouba` y `Kiki` en su momento, un atributo `self.salud`. Seguramente tu `Zombi` se ve similar a este:

```python
class Zombi:

  def __init_(self):
    self.salud = 100


  def salu(self):
    self.salud


  #...y otros métodos


```

Pero ahora que `self.salud` aparece en la clase `Zombi`, ¿eso significa que comparten el atributo? Si `Juliana` ataca a `bouba`, ¿disminuirá también la salud de `kiki`? :hospital:

> ¡Averigualo! Hacé que Juliana ataque a cada zombi con distintos puntos de daño y luego consultá la salud de ambos.
