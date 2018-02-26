class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]

    def collect_data(self,data):
        if data is None:
            return None
        self.datas.append(data)

    def output_html(self):
        fout=open('output.html','w')

        fout.write('<html>')
        fout.write('<meta charset="UTF-8">')
        fout.write('<body>')
        fout.write('<table>')

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>"+data['url']+"</td>" )
            fout.write("<td>"+data['title']+"</td>" )

            fout.write("</tr>")

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()

