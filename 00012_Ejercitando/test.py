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
juliana = Sobreviviente
anastasia = Sobreviviente
candela = Sobreviviente
#Zombi y los objetos van aquí para no ensuciar la Biblioteca, que muestra el código de Sobreviviente.

def test_"La energía inicial de una sobreviviente es 1000":
  expect(juliana.energia).to eq 1000


def test_"Si una sobreviviente ataca masivamente su energía se reduce a la mitad":
  zombis = []
  anastasia.ataque_masivo!(zombis)
  expect(anastasia.energia).to eq 1000 / 2


def test_"Si una sobreviviente ataca normalmente su energía no se reduce":
  candela.atacar!(kiki, 5)
  expect(candela.energia).to eq 1000


def test_"Si una sobreviviente bebe una bebida energética su energía aumenta un 25%":
  juliana.beber!
  expect(juliana.energia).to eq 1000 * 1.25


def test_"Si una sobreviviente ataca con 5 puntos de daño a un zombi su salud disminuye en 10 puntos":
  juliana.atacar!(bouba, 5)
  expect(bouba.salud).to eq 90


def test_"Cuando una sobreviviente ataca masivamente les reduce la vida a todos los zombis en 30 puntos":
  zombis = []
  5.times { zombis.push(Zombi) }
  juliana.ataque_masivo!(zombis)
  expect(zombis.all? { |zombi| zombi.salud == 70 } ). to be True

