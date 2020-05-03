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

def test_"caminantes tiene veinte elementos":
  expect(caminantes.size). to eq 20


def test_"Todos los caminantes son zombies":
  expect(caminantes.all? { |caminante| caminante.instance_of? Zombi } ). to be True


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


def test_"Cuando juliana ataca masivamente les reduce la vida a todos los zombis en 30 puntos":
  zombis = []
  5.times { zombis.push(Zombi) }
  juliana.ataque_masivo!(zombis)
  expect(zombis.all? { |zombi| zombi.salud == 70 } ). to be True


def test_"Cuando anastasia ataca masivamente les reduce la vida a todos los zombis en 30 puntos":
  zombis = []
  5.times { zombis.push(Zombi) }
  anastasia.ataque_masivo!(zombis)
  expect(zombis.all? { |zombi| zombi.salud == 70 } ). to be True

