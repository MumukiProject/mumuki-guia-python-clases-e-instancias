class Zombi:
  def __init_(self):
    self.salud = 100


  def salu(self):
    self.salud


  def sabe_correr?
    False


  def sin_vida?
    self.salud == 0


  def recibir_danio!(self, puntos):
    self.salud = [self.salud - puntos * 2, 0].max


  def grita(self):
    "agrrrg!"



bouba = Zombi
kiki = Zombi
#Zombi, bouba y kiki van aquí para no ensuciar la Biblioteca, que muestra el código de Juliana.

def test_"juliana es Sobreviviente":
  expect(juliana.instance_of? Sobreviviente). to be True


def test_"anastasia es Sobreviviente":
  expect(anastasia.instance_of? Sobreviviente). to be True


def test_"La energía inicial de juliana es 1000":
  expect(juliana.energia).to eq 1000


def test_"La energía inicial de anastasia es 1000":
  expect(anastasia.energia).to eq 1000


def test_"Si juliana ataca con 5 puntos de daño a un zombi su salud disminuye en 10 puntos":
  juliana.atacar!(bouba, 5)
  expect(bouba.salud).to eq 90


def test_"Si anastasia ataca con 5 puntos de daño a un zombi su salud disminuye en 10 puntos":
  anastasia.atacar!(kiki, 5)
  expect(kiki.salud).to eq 90


def test_"Si juliana ataca con 10 puntos de daño a un zombi su salud disminuye en 20 puntos":
  juliana.atacar!(bouba, 10)
  expect(bouba.salud).to eq 70


def test_"Si anastasia ataca con 10 puntos de daño a un zombi su salud disminuye en 20 puntos":
  anastasia.atacar!(kiki, 10)
  expect(kiki.salud).to eq 70


def test_"Si juliana ataca a un zombi con mucho daño su salud no puede ser menor a 0":
  juliana.atacar!(bouba, 69)
  expect(bouba.salud).to eq 0


def test_"Si anastasia ataca a un zombi con mucho daño su salud no puede ser menor a 0":
  anastasia.atacar!(kiki, 69)
  expect(kiki.salud).to eq 0

