# Ciclo 049 — EM13MAT305

- **Situação:** aprovada
- **Temas:** funcao_logaritmica
- **Nível cognitivo:** analisar
- **Dificuldade:** dificil | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Cientistas utilizam escalas logarítmicas para descrever a magnitude de fenômenos naturais cuja intensidade varia em muitas ordens de grandeza, como ocorre com a energia liberada em abalos sísmicos. Um modelo simplificado dessa relação define a magnitude $M$ de um terremoto, em função da energia $E$ (em joules) por ele liberada, pela expressão

$$M(E) = \frac{2}{3}\left(\log_{10}(E) - 4\right), \quad E > 0.$$

a) Um terremoto liberou energia $E_1 = 10^{13}$ J. Calcule sua magnitude $M_1$.

b) Um segundo terremoto ocorreu na mesma região, com magnitude exatamente uma unidade maior que a do primeiro, ou seja, $M_2 = M_1 + 1$. Determine, em função de $E_1$, a energia $E_2$ liberada por esse segundo terremoto, calcule a razão $E_2/E_1$ e mostre que essa razão não depende do valor de $E_1$ — isto é, que qualquer terremoto cuja magnitude seja uma unidade maior que a de outro libera sempre o mesmo número de vezes mais energia, independentemente do nível de energia inicial.

## Gabarito

M1 = 6; E2/E1 = 10^(3/2) = 10√10 ≈ 31,62, valor constante e independente de E1 (todo acréscimo de 1 unidade na magnitude multiplica a energia por esse mesmo fator).

## Resolução

**Passo 1 — Calcular $M_1$**

Com $E_1 = 10^{13}$ J, temos $\log_{10}(E_1) = 13$. Substituindo na fórmula:

$$M_1 = \frac{2}{3}\left(13 - 4\right) = \frac{2}{3}\cdot 9 = 6.$$

**Passo 2 — Inverter a função para expressar $E$ em termos de $M$**

Da definição:
$$M = \frac{2}{3}\left(\log_{10}E - 4\right) \;\Rightarrow\; \frac{3}{2}M = \log_{10}E - 4 \;\Rightarrow\; \log_{10}E = \frac{3}{2}M + 4.$$

Logo,
$$E = 10^{\,4 + \frac{3}{2}M} = 10^{4}\cdot 10^{\frac{3}{2}M}.$$

(Conferência: para $M_1=6$, $E_1 = 10^4\cdot10^{9} = 10^{13}$ J, coincidindo com o dado do item a.)

**Passo 3 — Determinar $E_2$ e a razão $E_2/E_1$**

Como $M_2 = M_1+1 = 7$:
$$E_2 = 10^{4}\cdot 10^{\frac{3}{2}\cdot 7} = 10^{4+10{,}5} = 10^{14{,}5}.$$

A razão entre as energias é:
$$\frac{E_2}{E_1} = \frac{10^{4}\cdot10^{\frac{3}{2}M_2}}{10^{4}\cdot10^{\frac{3}{2}M_1}} = 10^{\frac{3}{2}(M_2-M_1)} = 10^{\frac{3}{2}(1)} = 10^{3/2} = 10\sqrt{10} \approx 31{,}62.$$

**Passo 4 — Mostrar que a razão independe de $E_1$**

Para qualquer terremoto de magnitude $M$ (energia $E$) e outro de magnitude $M+1$ (energia $E'$), repetindo o cálculo anterior:
$$\frac{E'}{E} = 10^{\frac{3}{2}\left[(M+1)-M\right]} = 10^{3/2},$$
que é uma constante que **não depende de $M$ nem de $E$**. Ou seja, aumentar a magnitude em exatamente 1 unidade sempre multiplica a energia liberada pelo mesmo fator $10\sqrt{10}\approx 31{,}62$, seja o terremoto inicial fraco ou muito forte — a variação da grandeza física (energia) é sempre multiplicativa e constante quando a variação da grandeza logarítmica (magnitude) é aditiva e constante.

## Formalização verificável

- `funcao` — expressão `Rational(2,3)*(log(x,10) - 4)`, esperado `6`, parâmetros `{'consulta': 'valor', 'ponto': '10**13'}`
- `equacao` — expressão `Eq(Rational(2,3)*log(k,10), 1)`, esperado `[10**(Rational(3,2))]`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Gabarito confirmado (f(10000000000000) = 6). | (2) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - funcao/valor=aprovado
  - equacao=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem estruturado, define claramente a função, os dados e o que é pedido em cada item, sem ambiguidades. A notação e as condições (E>0) estão explícitas.
  - adequacao_nivel: 4/5 — O item (a) é de nível 'aplicar' (substituição direta), mas o item (b) exige generalizar uma relação (mostrar que a razão E2/E1 independe de E1), o que corresponde a 'analisar' (SOLO relacional/estendido-abstrato), pois demanda articular a estrutura logarítmica com a invariância do resultado. A presença do item (a) mais simples não compromete o núcleo analítico da questão, mas reduz levemente a pureza do nível declarado.
  - alinhamento_bncc: 5/5 — Atende plenamente à EM13MAT305: o contexto sísmico é realista, a função logarítmica é central, e a questão exige compreender a variação (magnitude aditiva ↔ energia multiplicativa), indo além da simples aplicação da definição de logaritmo, pois pede prova de invariância da razão.
  - distratores: 5/5 — não se aplica (questão discursiva).
  - originalidade: 4/5 — O contexto de magnitude sísmica é usual em livros didáticos, mas a exigência de demonstrar a invariância da razão E2/E1 para qualquer E1 é uma abordagem mais analítica e menos mecânica que o padrão 'calcule a magnitude dado E'. Não há pistas que antecipem a resposta (sem efeito Topaze), e a tarefa de generalização confere originalidade pedagógica ao problema.
