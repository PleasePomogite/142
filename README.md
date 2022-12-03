 # Пипина Алина 142

- ## Питон с переводом.py - перевод систем счисления в Python
- ## Пипина.pdf - файл с маркдауном
- ## нейр.PNG - работа с нейронной сетью
- ## Таблица умножения.py - таблица умножения (на python)
- ## Default.xlsx - в екселе 3 таблицы
- ## Хемминг.ipynb - python с кодом Хеминга
- ## логикааа.xlsx - таблица с решением по алгебре логики
- ## Морзянка.py - азбука Морзе на python 
- ## АлгебраЛогикийоу.py - задание по алгебре логики с сайта
- ## Видева в python.py - слайдшоу на питоне 
- ## Вопросики.py - викторина (мб не работает)
$$\overline{A\wedge B}=\overline{A}\vee \overline{B}$$
![Build Status](https://static.findanime.net/uploads/pics/00/84/061_o.jpg)

![](https://github.com/PleasePomogite/142/blob/main/Image/lagrida_latex.png)
<body>
  <pre class="mermaid">
    flowchart LR
        A-->B
        B-->C
        C-->D
        click A callback "Tooltip"
        click B "https://www.github.com" "This is a link"
        click C call callback() "Tooltip"
        click D href "https://www.github.com" "This is a link"
  </pre>

  <script>
    const callback = function () {
      alert('A callback was triggered');
    };
    const config = {
      startOnLoad: true,
      flowchart: { useMaxWidth: true, htmlLabels: true, curve: 'cardinal' },
      securityLevel: 'loose',
    };
    mermaid.initialize(config);
  </script>
</body>
