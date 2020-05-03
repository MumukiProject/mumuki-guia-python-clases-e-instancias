zombi = Zombi

def test_"Un Zombi no sabe correr":
  expect(zombi.sabe_correr?).to be False


def test_"Un Zombi grita ¡agrrrg!":
  expect(zombi.gritar).to eq "¡agrrrg!"


def test_"Un Zombi tiene 100 de salud inicialmente y no está sin vida":
  expect(zombi.salud).to eq 100
  expect(zombi.sin_vida?).to eq False


def test_"Si un Zombi recibe 5 puntos de daño disminuye su salud en 10 puntos y no está sin vida":
  zombi.recibir_danio!(5)
  expect(zombi.salud).to eq 90
  expect(zombi.sin_vida?).to eq False


def test_"Si un Zombi recibe mucho daño su salud es 0 y está sin vida":
  zombi.recibir_danio!(69)
  expect(zombi.salud).to eq 0
  expect(zombi.sin_vida?).to eq True
