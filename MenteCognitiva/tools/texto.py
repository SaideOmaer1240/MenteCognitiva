import pypandoc

# Texto em LaTeX que você deseja converter
latex_text = r"""\documentclass{article}
\usepackage{amsmath}
\begin{document}

Resolvendo a equação quadrática: 

\[
ax^2 + bx + c = 0
\]

\textbf{Passo 1: Identificação dos coeficientes}

Identificamos os coeficientes \(a\), \(b\), e \(c\) da equação.

\textbf{Passo 2: Fórmula Quadrática}

A fórmula quadrática é:

\[
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\]

\textbf{Passo 3: Cálculo do Discriminante}

Calculamos o discriminante (\(\Delta\)):

\[
\Delta = b^2 - 4ac
\]

\textbf{Passo 4: Cálculo das Raízes}

Dependendo do valor de \(\Delta\):

1. Se \(\Delta > 0\): A equação tem duas raízes reais e distintas:
   \[
   x_1 = \frac{-b + \sqrt{\Delta}}{2a}, \quad x_2 = \frac{-b - \sqrt{\Delta}}{2a}
   \]

2. Se \(\Delta = 0\): A equação tem uma raiz real (dupla):
   \[
   x = \frac{-b}{2a}
   \]

3. Se \(\Delta < 0\): A equação tem duas raízes complexas:
   \[
   x_1 = \frac{-b + i\sqrt{-\Delta}}{2a}, \quad x_2 = \frac{-b - i\sqrt{-\Delta}}{2a}
   \]
    

Vamos resolver a equação quadrática seguindo o passo a passo fornecido. Vamos usar como exemplo a equação:

\[
2x^2 + 3x - 5 = 0
\]

\textbf{Passo 1: Identificação dos Coeficientes}

Identificamos os coeficientes \(a\), \(b\) e \(c\) da equação:

\begin{itemize}
    \item \(a = 2\)
    \item \(b = 3\)
    \item \(c = -5\)
\end{itemize}

\textbf{Passo 2: Fórmula Quadrática}

A fórmula quadrática é:

\[
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\]

\textbf{Passo 3: Cálculo do Discriminante}

Calculamos o discriminante \((\Delta)\):

\[
\Delta = b^2 - 4ac
\]

Calculando passo a passo:

\[
\Delta = 3^2 - 4 \cdot 2 \cdot (-5)
\]

\[
\Delta = 9 + 40
\]

\[
\Delta = 49
\]

\textbf{Passo 4: Cálculo das Raízes}

Como \(\Delta > 0\), a equação tem duas raízes reais e distintas.

\[
x_1 = \frac{-b + \sqrt{\Delta}}{2a}
\]

\[
x_2 = \frac{-b - \sqrt{\Delta}}{2a}
\]

Calculando \(x_1\):

\[
x_1 = \frac{-3 + \sqrt{49}}{2 \cdot 2}
\]

\[
x_1 = \frac{-3 + 7}{4}
\]

\[
x_1 = \frac{4}{4}
\]

\[
x_1 = 1
\]

Calculando \(x_2\):

\[
x_2 = \frac{-3 - \sqrt{49}}{2 \cdot 2}
\]

\[
x_2 = \frac{-3 - 7}{4}
\]

\[
x_2 = \frac{-10}{4}
\]

\[
x_2 = -2.5
\]

\textbf{Resumo das Raízes}

As raízes da equação \(2x^2 + 3x - 5 = 0\) são:

\begin{itemize}
    \item \(x_1 = 1\)
    \item \(x_2 = -2.5\)
\end{itemize} 

  
\end{document}
"""
# Converter texto LaTeX para HTML com suporte a MathJax
html_output = pypandoc.convert_text(latex_text, 'html', format='latex')

# Adiciona MathJax para renderizar equações matemáticas
mathjax_script = """
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.0/es5/tex-mml-chtml.js">
</script>
"""

def latex2html(text):
    html_output = pypandoc.convert_text(text, 'html', format='latex')
    return html_output


# Inclui o script do MathJax no HTML
html_output = f"{mathjax_script}\n{html_output}"

# Escreve a saída em um arquivo HTML
with open("Arquivo_html.html", "w", encoding='utf-8') as file:
    file.write(html_output)


