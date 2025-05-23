from flask import Flask, request, jsonify
import os

app = Flask(__name__)

binarios_a_hexagrama = {
    "111111": 1, "000000": 2, "100010": 3, "010001": 4, "111010": 5, "010111": 6,
    "010000": 7, "000010": 8, "111011": 9, "110111": 10, "111000": 11, "000111": 12,
    "101111": 13, "111101": 14, "001000": 15, "000100": 16, "100110": 17, "011001": 18,
    "110000": 19, "000011": 20, "100101": 21, "101001": 22, "000001": 23, "100000": 24,
    "100111": 25, "111001": 26, "100001": 27, "011110": 28, "010010": 29, "101101": 30,
    "001110": 31, "011100": 32, "001111": 33, "111100": 34, "000101": 35, "101000": 36,
    "101011": 37, "110101": 38, "001010": 39, "010100": 40, "110001": 41, "100011": 42,
    "111110": 43, "011111": 44, "000110": 45, "011000": 46, "010110": 47, "011010": 48,
    "101110": 49, "011101": 50, "100100": 51, "001001": 52, "001011": 53, "110100": 54,
    "101100": 55, "001101": 56, "011011": 57, "110110": 58, "010011": 59, "110010": 60,
    "110011": 61, "001100": 62, "101010": 63, "010101": 64
}

def convertir_a_binario(tirada, mutar=False):
    binario = []
    for num in tirada:
        if num == 6:
            b = 0 if not mutar else 1
        elif num == 7:
            b = 1
        elif num == 8:
            b = 0
        elif num == 9:
            b = 1 if not mutar else 0
        else:
            raise ValueError(f"Número inválido: {num}")
        binario.append(str(b))
    return "".join(binario)

@app.route("/iching", methods=["POST"])
def iching():
    data = request.json
    tirada = data.get("tirada")
    if not tirada or len(tirada) != 6:
        return jsonify({"error": "Debes enviar una lista de 6 números"}), 400

    binario_original = convertir_a_binario(tirada)
    binario_resultante = convertir_a_binario(tirada, mutar=True)

    return jsonify({
        "hexagrama_original": {
            "numero": binarios_a_hexagrama.get(binario_original, "¿?"),
            "binario": binario_original
        },
        "hexagrama_resultante": {
            "numero": binarios_a_hexagrama.get(binario_resultante, "¿?"),
            "binario": binario_resultante
        }
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)