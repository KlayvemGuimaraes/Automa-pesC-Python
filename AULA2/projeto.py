# Passo 1 : importar a base de dados

# Base de dados com python
# r = local do arquivo 
# Churn = taxa de cancelamento 
# not a number = NaN
# dropna = exclui valores vazios
# ALL / ANY
# ALL = Excluir tal que tem todos valores vazios
# ANY = Excluir tal que possui algum valor vazio
# Passo 2 : Visualizar a base de dados

  # - Entender as informações disponíveis 
  # - Descobrir os problemas da base de dados 
  # informação que não te ajuda, atrapalha.
  # Excluir coluna .drop()
  # axis -> 0 = linha; excluir linha
  # axis-> 1 = coluna; excluir coluna


# Passo 3 = tratamento de dados 
# - OBJECT = TEXTO, - FLOAT64 = DECIMAL, - INT64 = INTEIRO 


# Passo 3 : Tratamento de dados 
    # Resolver valores que estão sendo reconhecidos de forma errada
    # - Resolver valores vazios     

#.sum() = soma
#.mean() = média
#.value_counts() = contar valores
#.value_counts(normalize=True) = cmostrar em porcentagem '
#.map(para formatacao)