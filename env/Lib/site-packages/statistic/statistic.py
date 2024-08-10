from collections import Counter



def get_numeros(numeros: list) -> list:
  lista = []
  for numero in numeros:
    if type(numero) is list:
      for sub in get_numeros(numero):
        lista.append(sub)
    else:
      lista.append(numero)
  return lista



class _StatisticCalculate:


  def media(self, numeros: list) -> float:
    numeros = get_numeros(numeros)
    return float(sum(numeros) / len(numeros))


  def media_ponderada(self, numeros: list, pesos: list ) -> float:
    numeros = get_numeros(numeros)
    pesos = get_numeros(pesos)
    if len(numeros) != len(pesos):
      raise ValueError('As duas listas devem ter as mesmas dimensões')
 
    for index in range(len(numeros)):
      numeros[index] *= pesos[index]

    media = sum(numeros) / sum(pesos)
    return float(media)


  def mediana(self, numeros: list) -> float:
    numeros = get_numeros(numeros)
    numeros.sort()
    if len(numeros) % 2 == 0:
      return (numeros[int(len(numeros) / 2)] + numeros[int(len(numeros) / 2) - 1]) / 2
    return numeros[int(len(numeros) / 2)]


  def moda(self, numeros: list) -> list:
    lista = []
    numeros = get_numeros(numeros)
    counter = Counter(numeros).most_common()
    for numero in counter:
      if numero[1] == counter[0][1]:
        lista.append(numero[0])
      else:
        break

    if counter[0][1] == counter[-1][1]:
      return []
    return lista


  def variancia(self, numeros: list) -> float:
    numeros = get_numeros(numeros)
    media = self.media(numeros)
    for index in range(len(numeros)):
      numeros[index] -= media
      numeros[index] *= numeros[index]
    soma = sum(numeros)
    return soma / (len(numeros) - 1)


  def desvio_padrao(self, numeros: list) -> float:
    numeros = get_numeros(numeros)
    return self.variancia(numeros) ** 0.5

  
  def amplitude(self, numeros: list) -> float:
    numeros = get_numeros(numeros)
    return max(numeros) - min(numeros)

  
  def desvio_medio(self, numeros: list) -> float:
    numeros = get_numeros(numeros)
    media = self.media(numeros)
    for index in range(len(numeros)):
      numeros[index] = abs(numeros[index] - media)
    return sum(numeros) / len(numeros)


  def erro_padrao(self, numeros: list) -> float:
    numeros = get_numeros(numeros)
    desvio = self.desvio_padrao(numeros)
    return desvio / (len(numeros) ** 0.5)


  def coeficiente_variacao(self, numeros: list) -> float:
    desvio = self.desvio_padrao(numeros)
    media = self.media(numeros)
    variacao = (desvio / media) * 100
    return variacao


  def soma_quadrados_desvios_acima_media(self, numeros: list)  -> float:
    numeros = get_numeros(numeros)
    media = self.media(numeros)
    for numero in numeros:
      numero = (numero - media) ** 2
    
    return sum(numeros)



  def coeficiente_correlacao(self, lista_x: list, lista_y: list) -> float:
    lista_x = get_numeros(lista_x)
    lista_y = get_numeros(lista_y)
    media_x = self.media(lista_x)
    media_y = self.media(lista_y)

    nova_lista = []
    for index in range(len(lista_x)):
      nova_lista.append((lista_x[index] - media_x) * (lista_y[index] - media_y))

    denominador = (self.soma_quadrados_desvios_acima_media(lista_x) * self.soma_quadrados_desvios_acima_media(lista_y)) ** 0.5    
    return sum(nova_lista) / denominador


  def covariancia(self, lista_x: list, lista_y: list) -> float:
    lista_x = get_numeros(lista_x)
    lista_y = get_numeros(lista_y)
    media_x = self.media(lista_x)
    media_y = self.media(lista_y)

    nova_lista = []
    for index in range(len(lista_x)):
      nova_lista.append((lista_x[index] - media_x) * (lista_y[index] - media_y))

    return sum(nova_lista) / (len(nova_lista) - 1)



class Statistic:


  __statistic = _StatisticCalculate()
  def media(self, numeros: list) -> float:
    """
    esta função recebe como parametro uma lista de numeros,
    ou matriz de numeros e retorna a media dos números da
    cadeia de números informada
    """
    return self.__statistic.media(numeros)


  def media_ponderada(self, numeros: list, pesos: list) -> float:
    """
    esta função recebe como parametro uma lista de numeros,
    ou matriz de numeros, e uma lista com seus respectivos 
    pesos, no mesmo tamanho e/ou dimensões que a lista de 
    numeros e retorna a media ponderada da cadeia de números informada
    """
    return self.__statistic.media_ponderada(numeros, pesos)


  def mediana(self, numeros: list) -> float:
    """
    esta função recebe como paremetro uma lista de números,
    ou uma matriz de números e retorna a mediana dos numeros
    informados
    """
    return self.__statistic.mediana(numeros)


  def moda(self, numeros: list) -> list:
    """
    esta função recebe como paremetro uma lista de números,
    ou uma matriz de números e retorna uma lista com a moda
    dos números
    """
    return self.__statistic.moda(numeros)


  def variancia(self, numeros: list) -> float:
    """
    esta função recebe como paremetro uma lista de números,
    ou uma matriz de números e retorna a variância desta amostra
    """
    return self.__statistic.variancia(numeros)


  def desvio_padrao(self, numeros: list) -> float:
    """
    esta função recebe como paremetro uma lista de números,
    ou uma matriz de números e retorna o desvio padrão desta amostra
    """
    return self.__statistic.desvio_padrao(numeros)


  def amplitude(self, numeros: list) -> float:
    """
    esta função recebe como paremetro uma lista de números,
    ou uma matriz de números e retorna sua amplitude
    """
    return self.__statistic.amplitude(numeros)


  def desvio_medio(self, numeros: list) -> float:
    """
    esta função recebe como paremetro uma lista de números,
    ou uma matriz de números e retorna seu desvio médio
    """
    return self.__statistic.desvio_medio(numeros)

  def erro_padrao(self, numeros: list) -> float:
    """
    esta função recebe como paremetro uma lista de números,
    ou uma matriz de números e retorna seu erro padrão
    """
    return self.__statistic.erro_padrao(numeros)


  def coeficiente_variacao(self, numeros: list) -> float:
    """
    esta função recebe como paremetro uma lista de números,
    ou uma matriz de números e retorna a porcentagem do 
    coeficiente de variação
    """
    return self.__statistic.coeficiente_variacao(numeros)
  

  def soma_quadrados_desvios_acima_media(self, numeros: list)  -> float:
    """
    esta função recebe como paremetro uma lista de números,
    ou uma matriz de números e retorna a soma dos quadrados
    dos desvidos dados acima da media da amostra
    """
    return self.__statistic.soma_quadrados_desvios_acima_media(numeros)


  def coeficiente_correlacao(self, lista_x: list, lista_y: list) -> float:
    """
    esta função recebe como parametro dois conjunto de dados, um em cada lista,
    e retorna o coeficiente de correlação.
    """
    return self.__statistic.coeficiente_correlacao(lista_x, lista_y)

  
  def covariancia(self, lista_x: list, lista_y: list) -> float:
    """
    esta função recebe como parametro dois conjunto de dados, 
    um em cada lista, e retorna a covariância.
    """
    return self.__statistic.covariancia(lista_x, lista_y)