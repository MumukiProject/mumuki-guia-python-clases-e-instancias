def test_"Bouba no sabe correr":
  expect(Bouba.sabe_correr?).to be False


def test_"Kiki no sabe correr":
  expect(Kiki.sabe_correr?).to be False


def test_"Bouba grita ¡agrrrg!":
  expect(Bouba.gritar).to eq "¡agrrrg!"


def test_"Kiki grita ¡agrrrg!":
  expect(Kiki.gritar).to eq "¡agrrrg!"


def test_"Bouba tiene 100 de salud inicialmente y está con vida":
  expect(Bouba.salud).to eq 100
  expect(Bouba.sin_vida?).to eq False


def test_"Kiki tiene 100 de salud inicialmente y está con vida":
  expect(Kiki.salud).to eq 100
  expect(Kiki.sin_vida?).to eq False


def test_"Si Bouba recibe 5 puntos de daño disminuye su salud en 10 puntos y está con vida":
  Bouba.recibir_danio!(5)
  expect(Bouba.salud).to eq 90
  expect(Bouba.sin_vida?).to eq False


def test_"Si Kiki recibe 5 puntos de daño disminuye su salud en 10 puntos y está con vida":
  Kiki.recibir_danio!(5)
  expect(Kiki.salud).to eq 90
  expect(Kiki.sin_vida?).to eq False


def test_"Si Bouba recibe mucho daño su salud es 0 y no está con vida":
  Bouba.recibir_danio!(69)
  expect(Bouba.salud).to eq 0
  expect(Bouba.sin_vida?).to eq True


def test_"Si Kiki recibe mucho daño su salud es 0 y no está con vida":
  Kiki.recibir_danio!(69)
  expect(Kiki.salud).to eq 0
  expect(Kiki.sin_vida?).to eq True
