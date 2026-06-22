import re

with open("rosas.html", "r", encoding="utf-8") as f:
    html = f.read()

letter_html = """
        <div class="letter-container" id="letterContainer">
            <div class="letter">
                <p>Enquanto seu nerdola favorito não chega para lhe entregar suas rosas pessoalmente, ele criou umas da forma que ele sabe fazer de melhor: sendo nerdola através de código.</p>
                <p>Espero que goste, gatinha de olhos e cabelos cor de mel.</p>
                <p class="signature">Com carinho,<br>Seu nerdola favorito.</p>
            </div>
        </div>
"""

letter_css = """
.letter-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: var(--dark-color);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
    animation: slideDownFade 1s 10s forwards;
}

.letter {
    background: #fff;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    max-width: 85%;
    text-align: center;
    font-family: 'Arial', sans-serif;
    color: #333;
    line-height: 1.6;
    font-size: 1.1rem;
    animation: letterShow 1s 1s forwards;
    opacity: 0;
    transform: translateY(-50px) scale(0.9);
}

.letter p {
    margin-bottom: 15px;
}

.letter .signature {
    font-style: italic;
    font-weight: bold;
    color: #ee5286;
    margin-top: 20px;
}

@keyframes slideDownFade {
    0% { transform: translateY(0); opacity: 1; }
    100% { transform: translateY(100vh); opacity: 0; visibility: hidden; }
}

@keyframes letterShow {
    0% { opacity: 0; transform: translateY(-50px) scale(0.9); }
    100% { opacity: 1; transform: translateY(0) scale(1); }
}
"""

js_addition = """
    setTimeout(() => {
        document.getElementById('flowersContainer').style.display = 'block';
    }, 11000); // 10s + 1s for letter to disappear
"""

# Insert CSS before </style>
html = html.replace('</style>', f'{letter_css}</style>')

# Insert JS before </script>
html = html.replace('</script>', f'{js_addition}</script>')

# Insert letter HTML right after <body class="container">
html = html.replace('<body class="container">', f'<body class="container">{letter_html}')

# Change flowers div to have id and display:none
html = html.replace('<div class="flowers">', '<div class="flowers" id="flowersContainer" style="display: none;">')

with open("rosas.html", "w", encoding="utf-8") as f:
    f.write(html)
