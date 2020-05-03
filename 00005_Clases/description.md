Si tenemos más de un objeto que se comporta **exactamente** de la misma forma, lo que podemos hacer es generalizar ese comportamiento declarando una **clase**. Por ejemplo, si tenemos dos celulares con el mismo saldo y ambos tienen las mismas funcionalidades, `realizar_llamada!` y `cargar_saldo!` :iphone: :

```python
module CelularDeMaría
  self.saldo = 25

  def self.realizar_llamada!
    self.saldo -= 5


  def self.cargar_saldo!(self, pesos):
    self.saldo += pesos



module CelularDeLucrecia
  self.saldo = 25

  def self.realizar_llamada!
    self.saldo -= 5


  def self.cargar_saldo!(self, pesos):
    self.saldo += pesos


```

Podemos generalizarlos en una **clase** `Celular`:

```python
class Celular:
  def __init_(self):
    self.saldo = 25


  def realizar_llamada!
    self.saldo -= 5


  def cargar_saldo!(self, pesos):
    self.saldo += pesos


```

> Veamos si se entiende: como `Bouba` y `Kiki` se comportan exactamente de la misma forma, **generalizalos** creando una clase `Zombi` que entienda los mismos cinco mensajes que ellos. Podés ver el código de ambos zombis en la solapa Biblioteca.
