from flask import Blueprint, request, jsonify
from app.utils.utils import csvToList

search_route = Blueprint('search', __name__)

listAllOperator = csvToList()

@search_route.route('/', methods=['GET'])
def search_operator():

    filterByCNPJ = request.args.get('filterbycnpj', '')
    filterByName = request.args.get('filterbyname', '').replace(" ", "").lower()

    if filterByCNPJ:
        listResult = [
            operator for operator in listAllOperator if filterByCNPJ in operator["CNPJ"]
        ]

        if not listResult:
            return jsonify({"message": "O CNPJ não foi encontrado."})

        return jsonify(listResult)

    if filterByName:
        listResult = [
            operator for operator in listAllOperator
            if (filterByName in operator["Razao_Social"].replace(" ", "").lower()) or
               (filterByName in operator["Nome_Fantasia"].replace(" ", "").lower())
        ]

        if not listResult:
            return jsonify({"message": "Empresa não encontrada."})

        return jsonify(listResult)

    if filterByName:
        listResult = [
            operator for operator in listAllOperator
            if filterByName.replace(" ", "").lower() in operator["Razao_Social"].replace(" ", "").lower() or operator[
                "Nome_Fantasia"].replace(" ", "").lower()
        ]

        if not listResult:
            return jsonify({"message": "Empresa não encontrada."})

        return jsonify(listResult)

    return jsonify(listAllOperator)
