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
julian = Aliado
anastasio = Aliado
candelo = Aliado
#Zombi y los objetos van aquí para no ensuciar la Biblioteca, que muestra el código de Sobreviviente.

def test_"La energía inicial de un aliado es 500":
  expect(julian.energia).to eq 500


def test_"Si un aliado ataca su energía se reduce un 5%":
  julian.atacar!(kiki, 5)
  expect(julian.energia).to eq 500 * 0.95


def test_"Si un aliado ataca masivamente su energía se reduce a la mitad":
  zombis = []
  anastasio.ataque_masivo!(zombis)
  expect(anastasio.energia).to eq 500 / 2


def test_"Si un aliado bebe una bebida energética su energía aumenta un 10%":
  candelo.beber!
  expect(candelo.energia).to eq 500 * 1.10


def test_"Si un aliado ataca con 5 puntos de daño a un zombi su salud disminuye en 10 puntos":
  julian.atacar!(bouba, 5)
  expect(bouba.salud).to eq 90


def test_"Cuando un aliado ataca masivamente les reduce la vida a todos los zombis en 40 puntos":
  zombis = []
  5.times { zombis.push(Zombi) }
  julian.ataque_masivo!(zombis)
  expect(zombis.all? { |zombi| zombi.salud == 60 } ). to be True

