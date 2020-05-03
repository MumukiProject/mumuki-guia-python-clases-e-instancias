def test_"Bouba no sabe correr":
  expect(Bouba.sabe_correr?).to be False


def test_"Bouba grita ¡agrrrg!":
  expect(Bouba.gritar).to eq "¡agrrrg!"


def test_"Bouba tiene 100 de salud inicialmente":
  expect(Bouba.salud).to eq 100


def test_"Si Bouba recibe 5 puntos de daño disminuye su salud en 10 puntos":
  Bouba.recibir_danio!(5)
  expect(Bouba.salud).to eq 90


def test_"Si Bouba recibe 10 puntos de daño disminuye su salud en 20 puntos":
  Bouba.recibir_danio!(10)
  expect(Bouba.salud).to eq 70


def test_"Si Bouba recibe mucho daño su salud no puede ser menor a 0":
  Bouba.recibir_danio!(69)
  expect(Bouba.salud).to eq 0
