from pathlib import Path
tabelle = '<!DOCTYPE html>\n<hmtl lang="de">\n   <head>\n        <title>Zufallsfarben</title>\n        <meta charset="utf8">\n        <link href="zf.css" rel="stylesheet">\n        <script src="../JavaScript/jquery-3.5.1.min.js"></script>\n' 
tabelle +=	'    </head>\n    <body>\n        <table>\n'
for reihe in range(1, 117):
    tabelle += "            <tr>"
    for feld in range(1, 201):
        tabelle += f"<td id='r{reihe}f{feld}'></td>"
    tabelle += "</tr>\n"
tabelle += "        </table>\n"
tabelle += '	</body>\n    <script src="rauten_zufallsfarben.js"></script>\n</html>'

with open(Path("d:/Programmieren/JavaScript/").joinpath("grosseRauten.html"), "wt") as dokument:
    dokument.write(tabelle)