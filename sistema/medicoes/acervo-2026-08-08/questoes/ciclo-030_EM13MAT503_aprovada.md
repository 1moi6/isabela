# Ciclo 030 — EM13MAT503

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** aplicar
- **Dificuldade:** dificil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Uma fábrica vende um certo produto a um preço unitário de $p$ reais. Estudos de mercado mostram que, para esse preço, a quantidade vendida mensalmente é dada por $q(p) = 300 - p$ unidades (com $0 < p < 300$). O custo mensal de produção, em reais, para fabricar $q$ unidades é $C(q) = 2000 + 50q$. O lucro mensal $L(p)$ é a diferença entre a receita obtida com as vendas, $R(p) = p \cdot q(p)$, e o custo de produção $C(q(p))$. Qual deve ser o preço $p$ (em reais) para que o lucro mensal seja máximo?

## Alternativas

- (a) R$ 150,00
  - *erro representado:* Maximizar apenas a receita R(p) = 300p - p², ignorando o custo de produção C(q(p)); vértice de R(p) ocorre em p=150.
- (b) R$ 175,00  ← correta
- (c) R$ 125,00
  - *erro representado:* Erro de sinal ao distribuir o custo na subtração L = R - C: escrever -50p em vez de +50p, obtendo L(p) = -p²+250p-17000 e vértice p=125.
- (d) R$ 350,00
  - *erro representado:* Esquecer de dividir por 2 na fórmula do vértice, calculando p = -b/a em vez de p = -b/(2a).

## Gabarito

p = 175 reais

## Resolução

**Passo 1 — Escrever a receita em função de $p$:**
$$R(p) = p \cdot q(p) = p(300-p) = 300p - p^2$$

**Passo 2 — Escrever o custo em função de $p$**, substituindo $q(p) = 300-p$ em $C(q)$:
$$C(p) = 2000 + 50(300-p) = 2000 + 15000 - 50p = 17000 - 50p$$

**Passo 3 — Montar a função lucro:**
$$L(p) = R(p) - C(p) = (300p - p^2) - (17000 - 50p)$$
$$L(p) = 300p - p^2 - 17000 + 50p = -p^2 + 350p - 17000$$

**Passo 4 — Identificar o ponto de máximo.** Como o coeficiente de $p^2$ é negativo ($a=-1$), a parábola tem concavidade para baixo, logo possui ponto de **máximo** no vértice:
$$p_v = -\frac{b}{2a} = -\frac{350}{2(-1)} = \frac{350}{2} = 175$$

**Passo 5 — Verificar que $p=175$ está no domínio válido** ($0<p<300$): sim, satisfaz a condição de demanda positiva.

**Passo 6 — (Conferência) Lucro máximo:**
$$L(175) = -175^2 + 350(175) - 17000 = -30625 + 61250 - 17000 = 13625$$

Portanto, o preço que maximiza o lucro mensal é $p = 175$ reais (com lucro máximo de $R\$13.625,00$).

## Formalização verificável

- `funcao` — expressão `-p**2 + 350*p - 17000`, esperado `[175, 13625]`, parâmetros `{'consulta': 'vertice'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** rejeitado — Divergência: extremo calculado 1000; gabarito 800.
  - funcao/maximo=rejeitado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: Divergência: extremo calculado 1000; gabarito 800. Resultado calculado independentemente: extremo calculado 1000. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 2

- **Verificador:** aprovado — Gabarito confirmado (vértice calculado (175, 13625)).
  - funcao/vertice=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem estruturado, define claramente p, q(p), C(q), R(p) e L(p), com domínio explícito. Não há ambiguidade sobre o que é pedido.
  - adequacao_nivel: 4/5 — O processo exigido (montar função lucro a partir de dados de receita e custo, depois aplicar fórmula do vértice) é consistente com 'aplicar' e exige integração de múltiplos passos (relacional na SOLO), acima de mera substituição. Poderia exigir uma etapa extra de interpretação/investigação para se aproximar mais do espírito de 'investigar' da habilidade, mas está adequado ao nível médio.
  - alinhamento_bncc: 5/5 — Atende plenamente a EM13MAT503: pede ponto de máximo de função quadrática, em contexto de Matemática Financeira (lucro, receita, custo), articulando os conceitos em um único problema coerente, não apenas cálculo algébrico isolado.
  - distratores: 5/5 — Todos os distratores representam erros sistemáticos plausíveis: ignorar o custo (150), erro de sinal na subtração (125), erro na fórmula do vértice (350). Nenhum é absurdo ou trivialmente eliminável.
  - originalidade: 3/5 — O contexto de lucro/receita/custo com função de demanda linear é um clássico recorrente em livros didáticos e listas de exercícios; embora bem construído, não traz elemento diferenciado de contextualização significativa nem evita o padrão-modelo tradicional desse tipo de problema.
