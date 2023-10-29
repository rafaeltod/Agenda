import json

class Conta:
  def __init__(self, id, nome, email, senha):
    self.__id = id
    self.__nome = nome
    self.__email = email
    self.__senha = senha

  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_email(self): return self.__email
  def get_senha(self): return self.__senha

  def set_id(self, id): self.__id = id
  def set_nome(self, nome): self.__nome = nome
  def set_email(self, email): self.__email = email
  def set_senha(self, senha): self.__senha = senha

  def __eq__(self, x):
    if self.__id == x.__id and self.__nome == x.__nome and self.__email == x.__email and self.__senha == x.__senha:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__email} - {self.__senha}"


class NConta:
  __contas = []  # lista de contas inicia vazia

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    for conta in cls.__contas:
      if conta.get_email() == obj.get_email():
        return False
    id = 0  # encontrar o maior id já usado
    for aux in cls.__contas:
      if aux.get_id() > id: id = aux.get_id()
    obj.set_id(id + 1)
    cls.__contas.append(obj)  # insere um conta (obj) na lista
    cls.salvar()
    return True

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.__contas  # retorna a lista de contas

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for obj in cls.__contas:
      if obj.get_id() == id: return obj
    return None

  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    for conta in cls.__contas:
      if conta.get_email() == obj.get_email() and conta.get_id() != obj.get_id():
        return False
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      aux.set_nome(obj.get_nome())
      aux.set_email(obj.get_email())
      aux.set_senha(obj.get_senha())
      cls.salvar()
      return True

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      cls.__contas.remove(aux)
      cls.salvar()

  @classmethod
  def abrir(cls):
    cls.__contas = []
    try:
      with open("contas.json", mode="r") as arquivo:
        contas_json = json.load(arquivo)
        for obj in contas_json:
          aux = Conta(obj["_Conta__id"], obj["_Conta__nome"], obj["_Conta__email"], obj["_Conta__senha"])
          cls.__contas.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("contas.json", mode="w") as arquivo:
      json.dump(cls.__contas, arquivo, default=vars)
