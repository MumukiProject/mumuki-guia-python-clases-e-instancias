class Sobreviviente:
  def __init_(self):
    self.energia = 1000


  def energi(self):
    self.energia


  def atacar!(self, zombie, danio):
    zombie.recibir_danio!(danio)


  def ataque_masivo!(self, zombis):
    zombis.each { |zombi| atacar!(zombi, 15) }


