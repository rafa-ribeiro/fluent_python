### Capítulo 2 - Uma coleção de sequências 


15. São sequências container -> list, tuple e collections.deque -> podem armazenar itens de tipos diferentes.
-- Sequências container armazenam em sí as REFERÊNCIAS aos objetos, por isso podem apontar para tipos distintos


16. str, bytes, bytearray, memoryview e array.array -> São sequências simples -> armazenam itens de um único tipo.
--- Sequências simples armazenam fisicamente o valor de cada item em seu próprio espaço de memória.


17. Sequências mutáveis -> list, bytearray, array.array, collections.deque e memoryview


18. Sequências imutáveis -> tuple, str e bytes


19. ABS - Abstract base classes


20. List comprehensions são, geralmente, mais rápidos que a forma sintática usual.


21. List Comprehensions = listcomps


22. Expressões geradoras = genexps


23. O script 02-array-seq/listcomp_speedy.py no repositório do livro Python Fluente no github mostra um teste simples de
velocidade comparando listcomp com as functions filter/map.


24. As listcomps fazem apenas uma coisa: elas criam listas.


25. genexps criam sequências que não sejam listas.


26. genexps -> podemos utilizar listcomps para inicializar tuplas, arrays e outros tipos de sequência, porém uma genexp
economiza memória, pois ela gera itens um por um usando o protocolo de iteradores, em vez de criar uma lista completa
somente para alimentar outro construtor.


27. listcomps são delimitadas por colchetes: 

<code>
    [x for x in 'abc']
</code>


28. genexps são delimitadas por parênteses -> tuple(ord(symbol) for symbol in symbols)
-- Se a expressão geradora for o único argumento em uma chamada de função, não será necessário duplicar o parênteses
para indicar um tupla.


29. Tuplas -> O laço for ao iterar por uma tupla sabe como obter seus itens de forma separada, isso é chamado de
Unpacking ou Desempacotamento.


30. Tuplas podem ser usadas para, de uma forma elegante, trocar os valores de duas variáveis, por exemplo: a, b = b, a


31. A função collections.namedtuple é uma fábrica (factory) que gera subclasses de tuple melhoradas com nomes de campos
e um nome de classe.


32. As instâncias de uma classe criada com namedtuple ocupam exatamente a mesma quantidade de memória que tuplas porque
os nomes dos campos são armazenados na classe.


33. Namedtuple usam menos memória que um objeto normal, pois não armazenam atributos em um __dict__() por instância.


34. Atributos úteis de namedtuple:
-- _fields: devolve uma tupla com os nomes dos campos da classe.
-- _make(iterable): permite instanciar uma tupla nomeada a partir de um iterável
-- _asdict(): retorna um collections.OrderedDict criado a partir da instância da tupla nomeada.


35. Slicing = Fatiamento
-- S[a:b] -> Do conjunto S pego os elementos de a (inclusive) até b (exclusive)
-- São utilizados em todos os tipos de sequência Python = list, tuple, str, etc.


36. Os objetos slice podem ser utilizados para leitura de arquivos posicionais por possibilitar que seja possível alocar
as fatias em outras várias. Exemplo:
-- SKU = slice(0, 6)
| for item in item_lines:
|   print(item[SKU])


37. Se x for um array de 4 dimensões, temos que x[i, ...] é uma forma abreviada para x[i, :, :, :]


38. As fatias não são úteis apenas para extrair informações de sequências; elas também podem ser usadas para alterar
sequências mutáveis in-place - ou seja, sem precisar recriá-las.


39. "+" e "*" para concatenação de sequências sempre criam objetos novos, nunca alteram seus operandos.


40. "+=" e "*=" são operadores de atribuição combinada


41. O método especial que faz o parâmetro de atribuição combinada '+=' funcionar é o método __iadd__ de
"in-place addition" ou soma in-place. Caso não tenha sido implementado, o Python usará o __add__ como alternativa.


42. Por sua vez, "*=" funcionar através do método especial __imul__


43. Lições:
- Colocar itens mutáveis em tuplas, não é uma boa ideia.
- Uma atribuição combinada não é uma operação atômica, uma vez que ela lança uma exceção e executa parte de seu trabalho
- Inspecionar bytecodes em Python não é muito difícil e pode ajudar a entender determinados comportamentos.


44. O método list.sort orderna uma lista in-place, isto é, SEM CRIAR UMA CÓPIA. Como altera o objeto alvo, o método
retorna None.


45. Convenção do Python -> as funções que alteram o próprio objeto, retornam None para deixar claro que nenhum novo
objeto foi criado, mas sim a própria instância foi alterada.


46. A desvatangem desssa convenção é que os métodos in-place não podem ser chamados em cascata.


47. Diferente de list.sort, a built-in function sorted cria um novo objeto.


48. O Algoritmo de ordenação usado em Python é o Timsort


49. Busca binária está disponível em Python no módulo bisect da biblioteca padrão.


50. bisect.insort -> Insere um elemento de forma ordenada mantendo a sequência ordenada.


51. Lista não é a resposta para tudo


52. Um array é mais eficiente para se armazenar valores de ponto flutuante, pois um array não armazena objetos float
completo, mas apenas os bytes compactos que representam seus valores de máquina.


53. deque -> double-ended queue ou fila dupla, eficiente para casos em que é preciso adicionar e remover itens das
extremidades de uma sequência, FIFO ou LIFO.


54. Um array é mais eficiente que uma lista para se armazenar valores numéricos


55. Ao criar um array é preciso fornecer um código de tipo (typecode).


56. 'b' é o typecode para signed char.


57. Se um array('b') for criado, cada item será armazenado em um único byte e será interpretado como um interiro de
-128 a 127. Para sequências longas de números, essa estratégia economiza bastante memória. Além de não se possível
adicionar nenhum outro valor que não seja do tipo do array.


58. pickle também é uma maneira rápida e mais flexível de salvar dados numéricos, quase tão rápida quanto o
array.tofile, no entanto pickle trata quase todos os tipos tipos embutidos, incluindo números complex, coleções
aninhadas e até mesmo instâncias de classes definidas pelo usuário automaticamente (se não forem muito complexas).


59. A classe memoryview embutida é um tipo de sequência de memória compartilhada que permite lidar com fatias de arrays
sem copiar os bytes. Permite copiar memória entre estruturas de dados sem fazer uma cópia inicial (exemplos:
informações como imagens PIL, banco de dados SQLlite, arrays NumPy, etc). Boa para conjuntos grandes de dados


60. memoryview.cast permite alterar o modo como vários bytes são lidos ou escritos como unidades sem mover os dados
por aí.


61. memoryview.cast devolve outro objeto memoryview, sempre compartilhando a mesma memória.


62. NumPy implementa tipos para arrays e matrizes multidimensionais e homogêneos que armazenam não só números como
também registros definidos pelo usuário, além de oferencer operações eficientes aplicadas a todos os elementos
de uma só vez.


63. SciPy é baseada em NumPy e oferece muitos algoritmos de computação científica, de álgebra linear a cálculo numérico
e estatísticas.


64. from time import perf_counter as pc -> Timer de medição de desempenho de alta resolução (desde Python 3.3)


65. collections.deque é uma fila dupla thread-safe, criada para proporcionar inserção e remoção rápidas de ambas as 
extremidades


66. collections.deque é uma boa opção quando se quer utilizar, por exemplo, uma lista dos "últimos itens vistos", pois
o deque pode ser de tamanho limitado e, quando cheio, ao inserir novos itens, os itens da extremidade oposta serão 
descartados.


67. collections.deque não são indicados para os casos em que se precisar adicionar/remover elementos no/do meio de uma
sequência, as operações são mais custosas.


68. O algoritmo de ordenação usado em sorted e em list.sort é o Timsort, um algoritmo adaptativo que alterna entre
as estratégias de insertion sort e merge sort, de acordo com o grau de ordenação dos dados.
