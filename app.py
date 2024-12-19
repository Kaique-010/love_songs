from flask import Flask, render_template
import qrcode

app = Flask(__name__)

@app.route("/")
def home():
    # Lista de imagens com mensagens e cronologia
    images_data = [
        {
            "path": "static/images/romantic1.jpg",
            "message": "Nosso primeiro Natal juntos, repleto de amor e carinho.",
            "chronology": "Dezembro de 2020",
        },
        {
            "path": "static/images/romantic2.jpg",
            "message": "O sorriso mais lindo que ilumina meu mundo.",
            "chronology": "Verão de 2021",
        },
        {
            "path": "static/images/romantic3.jpg",
            "message": "Aquele momento mágico sob as estrelas.",
            "chronology": "Outono de 2022",
        },
        {
            "path": "static/images/romantic4.jpg",
            "message": "Aquele momento mágico sob as estrelas.",
            "chronology": "Inverno de 23",
        },
        {
            "path": "static/images/romantic5.jpg",
            "message": "Aquele momento mágico sob as estrelas.",
            "chronology": "Inverno de 23",
        },
    ]
    return render_template("index.html", images_data=images_data)

@app.route("/qrcode")
def generate_qr():
    # URL do site
    site_url = "http://127.0.0.1:5000/"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(site_url)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save("static/qr_code.png")
    return "QR Code gerado! Verifique o arquivo em: static/qr_code.png"

if __name__ == "__main__":
    app.run(debug=True)
