# Ciclo 029 — EM13MAT404

- **Situação:** aprovada
- **Temas:** funcao_trigonometrica
- **Nível cognitivo:** entender
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Considere a função $f(x) = 3\cos(2x) - 1$, definida para $x \in \mathbb{R}$.

No ciclo trigonométrico (circunferência de raio 1 centrada na origem), o valor de $\cos(\theta)$ corresponde à abscissa do ponto $P$ que se desloca sobre a circunferência conforme o ângulo $\theta$ varia.

Usando essa relação entre o ciclo trigonométrico e a representação de $f$ no plano cartesiano, determine, justificando cada resposta com base no comportamento do ponto $P$ sobre a circunferência:

a) o domínio de $f$;

b) o período de $f$;

c) a imagem de $f$.

## Gabarito

Domínio: $\mathbb{R}$; Período: $\pi$; Imagem: $[-4, 2]$

## Resolução

**a) Domínio**

No ciclo trigonométrico, o ângulo $\theta$ pode assumir qualquer valor real — positivo, negativo, maior que $2\pi$ etc. — pois o ponto $P$ simplesmente continua girando pela circunferência indefinidamente. Como $2x$ pode ser qualquer número real quando $x$ percorre $\mathbb{R}$, o cosseno de $2x$ está sempre definido. Logo:
$$D(f) = \mathbb{R}$$

**b) Período**

No ciclo trigonométrico, o ponto $P$ retorna à mesma posição sempre que o ângulo aumenta $2\pi$ radianos (uma volta completa). Aqui o ângulo que gira é $2x$, então uma volta completa ocorre quando:
$$2x = 2\pi \;\Rightarrow\; x = \pi$$
Assim, $\cos(2x)$ repete seus valores a cada $x = \pi$. As operações de multiplicar por $3$ e subtrair $1$ apenas reescalam e deslocam verticalmente o gráfico no plano cartesiano — elas não alteram o ritmo com que o ponto $P$ completa voltas no ciclo. Portanto o período de $f$ é:
$$T = \pi$$

**c) Imagem**

Como o ciclo trigonométrico tem raio $1$, a abscissa do ponto $P$ (isto é, $\cos(2x)$) varia sempre entre $-1$ e $1$:
$$-1 \le \cos(2x) \le 1$$
Multiplicando por $3$ (o que estica a projeção no plano cartesiano, correspondendo a um círculo 'equivalente' de raio 3 na análise da amplitude):
$$-3 \le 3\cos(2x) \le 3$$
Subtraindo $1$ (deslocamento vertical do gráfico no plano cartesiano):
$$-4 \le 3\cos(2x) - 1 \le 2$$
Logo:
$$Im(f) = [-4, 2]$$

## Formalização verificável

- `funcao` — expressão `3*cos(2*x) - 1`, esperado `S.Reals`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `3*cos(2*x) - 1`, esperado `pi`, parâmetros `{'consulta': 'periodo'}`
- `funcao` — expressão `3*cos(2*x) - 1`, esperado `Interval(-4, 2)`, parâmetros `{'consulta': 'imagem', 'dominio': 'S.Reals'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (domínio de 3*cos(2*x) - 1: Reals). | (2) aprovado: Gabarito confirmado (período pi). | (3) aprovado: Gabarito confirmado (imagem de 3*cos(2*x) - 1: Interval(-4, 2)).
  - funcao/dominio=aprovado
  - funcao/periodo=aprovado
  - funcao/imagem=aprovado
- **Crítico:** aprovou
  - clareza: 4/5 — Enunciado bem estruturado, com dados completos (função, domínio de definição) e três pedidos claros (domínio, período, imagem), cada um exigindo justificativa via ciclo trigonométrico. Pequena imprecisão: não se explicita que a justificativa deve mencionar explicitamente a comparação ciclo-plano em cada item, o que pode gerar respostas que só usam fórmulas sem de fato articular as duas representações.
  - adequacao_nivel: 3/5 — O nível declarado é 'entender', compatível com a tarefa de identificar/justificar características a partir de uma relação já dada no enunciado. Porém a resolução exige aplicar transformações (multiplicação e translação) sobre domínio, período e imagem, o que se aproxima mais de 'aplicar' do que de mero 'entender'. Ainda assim, dentro do Ensino Médio, é uma exigência razoável e a estrutura de resposta (relacionar ciclo e transformações) é multiestrutural/relacional, compatível com o nível declarado, mas seria mais preciso enquadrar como 'aplicar'.
  - alinhamento_bncc: 4/5 — A questão cumpre bem as três exigências centrais: pede domínio, período e imagem (não cálculo de valores), e exige explicitamente que a resposta seja justificada com base no comportamento do ponto P no ciclo, articulando ciclo trigonométrico e plano cartesiano de forma integrada (não como itens isolados, já que os itens dependem da mesma leitura geométrica). O único ponto que impede nota máxima é que o item (a), domínio, é trivialmente satisfeito pela definição de x real, com baixa mobilização real da comparação ciclo-cartesiano (a justificativa do domínio é quase redundante), reduzindo a robustez da integração em todos os itens.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 3/5 — O contexto (função cosseno com amplitude e translação) é um exemplo clássico de livro didático, ainda que a exigência de justificar via ciclo trigonométrico traga alguma diferenciação. Não há contextualização significativa (sem situação real ou aplicação), e a estrutura passo a passo do enunciado (a, b, c) e da resolução esperada guia fortemente o caminho de resolução, aproximando-se do efeito Topaze ao already indicar que a resposta deve seguir 'o comportamento do ponto P'.
