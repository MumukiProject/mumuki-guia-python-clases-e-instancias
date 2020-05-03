zombi = Zombi(100)

def test_"Si creo un nuevo Zombi le puedo especificar su salud inicial":
  zombi42 = Zombi(42)
  expect(zombi42.salud). to eq 42


def test_"Un Zombi no sabe correr":
  expect(zombi.sabe_correr?).to be False


def test_"Un Zombi grita ¡agrrrg!":
  expect(zombi.gritar).to eq "¡agrrrg!"


def test_"Un Zombi con salud inicial 100 no está sin vida":
  expect(zombi.sin_vida?).to be False


def test_"Si un Zombi de salud 100 recibe 5 puntos de daño disminuye su salud en 10 puntos y no está sin vida":
  zombi.recibir_danio!(5)
  expect(zombi.salud).to eq 90
  expect(zombi.sin_vida?).to be False


def test_"Si un Zombi recibe mucho daño su salud es 0 y está sin vida":
  zombi.recibir_danio!(69)
  expect(zombi.salud).to eq 0
  expect(zombi.sin_vida?).to be True
