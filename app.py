from flask import Flask, render_template, request, jsonify
from Service import GeneratorDM, XMLwork, MySQLService


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('FirstPage.html')


@app.route('/datamatrix', methods=['GET', 'POST'])
def datamatrix():
    if request.method == 'POST':
        datamatrix_text = request.form.get('DMText')
        datamatrix_list = datamatrix_text.split('\n')
        file_names = GeneratorDM.generateDM(datamatrix_list)
        gtins = GeneratorDM.getGtins(datamatrix_list)
        return jsonify(file_names=file_names, gtins=gtins)
    return render_template('datamatrix.html', datamatrix_text='')


@app.route('/gtinJournal')
def gtinJournal():
    matrix = MySQLService.getFreeDM()
    gtinDescr = MySQLService.get_gtin_description
    return render_template('gtinJournal.html', matrix=matrix, get_gtin_description=gtinDescr)


if __name__ == '__main__':
    app.run()
