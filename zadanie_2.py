from weasyprint import HTML, CSS

string = '''<table>
    <thead>
        <tr>
            <th>Pracownik</th>
            <th>Czas pracy</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Mateusz</td>
            <td>10h 30min</td>
        </tr>
    </tbody>
</table>'''

stylesheet = '''
    body {
        background-color:#ece4d5;
        font-family: sans-serif;
    }

    thead tr{
        border-bottom: 3px black solid;
    }

    tbody tr {
        border-bottom: 1px black solid;
    }

    tbody tr td {
        padding-bottom: 5px
    }
'''

html = HTML(string=string)
css = CSS(string=stylesheet)
html.write_pdf('test1.pdf', stylesheet=[css])


