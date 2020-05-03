zombi = SuperZombi(100)

def test_"Si creo un nuevo SuperZombi le puedo especificar su salud inicial":
  zombi42 = SuperZombi(42)
  expect(zombi42.salud). to be 42


def test_"Un SuperZombi sabe correr":
  expect(zombi.sabe_correr?).to be True


def test_"Un SuperZombi grita ¡agrrrg!":
  expect(zombi.gritar).to eq "¡agrrrg!"


def test_"Un SuperZombi con salud inicial 100 no está sin vida":
  expect(zombi.sin_vida?).to eq False


def test_"Si un SuperZombi de salud 100 recibe 5 puntos de daño disminuye su salud en 15 puntos y no está sin vida":
  zombi.recibir_danio!(5)
  expect(zombi.salud).to eq 85
  expect(zombi.sin_vida?).to eq False


def test_"Si un SuperZombi recibe mucho daño su salud es 0 y está sin vida":
  zombi.recibir_danio!(69)
  expect(zombi.salud).to eq 0
  expect(zombi.sin_vida?).to eq True


def test_"Si un SuperZombi se regenera su salud vuelve a 100":
  zombi.regenerarse!
  expect(zombi.salud).to eq 100
