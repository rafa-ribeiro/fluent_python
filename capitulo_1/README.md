### Capítulo 1 - Modelo de dados do Python

1. Métodos especiais como, por exemplo, __getitem__, __str__, podem ser chamados de métodos dunder (dunder methods).


2. Ao fazer um collection[key], o interpretador executa na verdade um: collection.__getitem__(key)


3. Implementar o método especial __getitem__ faz com que eu possa aplicar slicing:

Pega as 3 primeiras cartas do baralho

```python 
    deck[:3]		
```

Pega a partir do indice 12 e avança de 13 em 13 até o final do baralho

```python
    deck[12::13]
```


4. Implementar o mesmo __getitem__ faz com que a classe seja iterável. Inclusive iterando reversamente com o comando reversed(deck).


5. A nossa classe FrenchDeck apesar de não implementar o método contains, funciona com o método in por ser uma classe iterável, dessa forma ao usarmos o in, o interpretador fará uma varredura sequencial nos cards da nossa classe.


6. Métodos especiais são criados para serem chamados pelo interpretador e NÃO por você. Fazemos len(collection) ao invés de collection.__len__()


7. Para os tipos de dados embutidos, os built-in é mais rápido chamar os métodos que referenciam os métodos especiais do que chamá-los diretamente.

-- Exemplo: Chamar o len é mais rápido que chamar o __len__() para tipos de dados como str ou list. Isso porque eles podem estar implementados de forma com que o tamanho já esteja contabilizado e associado na memória e não tendo a necessidade de efetuar qualquer iteração.


8. __repr__ -> Representação em string -> built-in function = repr(obj)

-- A string retorna de __repr__ não deve ser ambígua e, se possível, deve corresponder ao código-fonte necessário para se recriar o objeto que está sendo representado.

-- str é mais adequada para exibição aos usuários finais, enquanto que __repr__ deve seguir a premissa acima e mais adequada para o developer.

-- Se for somente implementar repr ou str, prefire implementar o __repr__ porque, quando um __str__ personalizado não estiver disponível, o Python chamará __repr__ como alternativa.


9. Por padrão, as instâncias das classes definida pelo usuário são consideradas verdadeiras, a menos que __bool__ ou __len__ esteja implementada.

Ex: Ao fazer bool(x), o interpretador executára:
-- Se __bool__ implementado ==> x.__bool__()
-- Se __bool__ não implementado ==> x.__len__(). Então se len == 0 retorna False senão retorna True


10. A expressão OR sozinha não retorna um booleano, mas sim um dos valores de cada lado da expressão, por isso ao sobreescrevermos o __bool__, precisamos garantir o retorno
booleano com bool(self.x or self.y)


11. Operadores aritméticos reversos =>
-- É possível fazer vector * 3 implementando __mul__
-- Mas para conseguir fazer 3 * vector é necessário implementar o mesmo método reverso -> __rmul__


12. Operadores de atribuição combinada
-- a = a + 1 torna-se a += 1


13. Leitura complementar
-- Data Model de The Python Language Reference.
-- Livro Python in a Nutshell, 2° edição, Alex Martelli
-- Python Essential Reference, 4° edição e Python Cookbook, Ambos de David Beazley
-- The Art of the Metaobject Protocol (AMOP)


14. A comunidade Ruby chama seu equivalente aos métodos especiais de Métodos Mágicos.
