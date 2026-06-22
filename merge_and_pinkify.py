import re

def process():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
        
    with open("src/style/style.css", "r", encoding="utf-8") as f:
        css = f.read()

    with open("src/js/script.js", "r", encoding="utf-8") as f:
        js = f.read()

    # Modify base pink flower colors
    css = css.replace('background-color: #f672b0;', 'background-color: #ffb6c1;')
    css = css.replace('background-image: linear-gradient(to top, #ee5286, #ee5286);', 'background-image: linear-gradient(to top, #ff7eb3, #ff758c);')
    css = css.replace('background-color: #6bf0ff;', 'background-color: #ff9a9e;')

    css_additions = """
/* Variations of Pink Gradients for each flower */
.flower--1 .flower__leaf { background-image: linear-gradient(to top, #ff9a9e 0%, #fecfef 100%); }
.flower--2 .flower__leaf { background-image: linear-gradient(to top, #ff758c 0%, #ff7eb3 100%); }
.flower--3 .flower__leaf { background-image: linear-gradient(to top, #fa709a 0%, #fee140 100%); }
.flower--4 .flower__leaf { background-image: linear-gradient(to top, #ff0844 0%, #ffb199 100%); }
.flower--5 .flower__leaf { background-image: linear-gradient(to top, #f43b47 0%, #fbc2eb 100%); }
.flower--6 .flower__leaf { background-image: linear-gradient(to top, #f77062 0%, #fe5196 100%); }

/* Positioning and sizing for new flowers */
.flower--4 { left: 20%; bottom: 8vmin; transform-origin: bottom center; transform: scale(0.7) rotate(-20deg); animation: moving-flower-1 4s linear infinite; }
.flower--5 { left: 80%; bottom: 12vmin; transform-origin: bottom center; transform: scale(0.8) rotate(25deg); animation: moving-flower-2 4s linear infinite; }
.flower--6 { left: 35%; bottom: 5vmin; transform-origin: bottom center; transform: scale(0.6) rotate(-5deg); animation: moving-flower-3 4s linear infinite; }

.flower--4 .flower__line { height: 40vmin; animation-delay: 0.5s; }
.flower--5 .flower__line { height: 50vmin; animation-delay: 0.7s; }
.flower--6 .flower__line { height: 35vmin; animation-delay: 0.9s; }
"""
    css += css_additions

    # Replace links with inline style and script
    html = re.sub(r'<link rel="stylesheet" href="\./src/style/style\.css">', f'<style>{css}</style>', html)
    html = re.sub(r'<script src="\./src/js/script\.js"></script>', f'<script>{js}</script>', html)

    flower_template = """
            <div class="flower flower--{num}">
                <div class="flower__leafs flower__leafs--{num}">
                    <div class="flower__leaf flower__leaf--1"></div>
                    <div class="flower__leaf flower__leaf--2"></div>
                    <div class="flower__leaf flower__leaf--3"></div>
                    <div class="flower__leaf flower__leaf--4"></div>
                    <div class="flower__white-circle"></div>

                    <div class="flower__light flower__light--1"></div>
                    <div class="flower__light flower__light--2"></div>
                    <div class="flower__light flower__light--3"></div>
                    <div class="flower__light flower__light--4"></div>
                    <div class="flower__light flower__light--5"></div>
                    <div class="flower__light flower__light--6"></div>
                    <div class="flower__light flower__light--7"></div>
                    <div class="flower__light flower__light--8"></div>
                </div>
                <div class="flower__line">
                    <div class="flower__line__leaf flower__line__leaf--1"></div>
                    <div class="flower__line__leaf flower__line__leaf--2"></div>
                    <div class="flower__line__leaf flower__line__leaf--3"></div>
                    <div class="flower__line__leaf flower__line__leaf--4"></div>
                </div>
            </div>
"""
    more_flowers = flower_template.format(num=4) + flower_template.format(num=5) + flower_template.format(num=6)

    html = html.replace('<div class="grow-ans" style="--d: 1.2s">', more_flowers + '\n            <div class="grow-ans" style="--d: 1.2s">')

    with open("rosas.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    process()
