from flask import Flask, render_template
import qrcode

app = Flask(__name__)

@app.route("/")
def home():
    # Lista de imagens com mensagens e cronologia
    images_data = [
        
        {
            "path": "static/images/romantic5.jpg",
            "message": "Há exatamente 1 ano, passamos nosso primeiro natal juntos, onde conheci sua família e mesmo um pouco assustado com toda a situação, estava ainda mais convencido de que havia feito a escolha certa...",
            "chronology": "Dezembro de 2023",
        },
        {
            "path": "static/images/romantic4.jpg",
            "message": "Nos conhecemos em um carnaval, no próximo carnaval já estávamos namorando, usando roupas iguais e nos apaixonando cada vez mais conforme descobríamos mais um sobre o outro...",
            "chronology": "Feveiro de 2024",
        },
        
        {
            "path": "static/images/romantic2.jpg",
            "message": "Mesmo que estejamos juntos a menos de 2 anos, parece que vivemos vários momentos incríveis e marcantes que vamos levar conosco e lembrar para sempre...",
            "chronology": "Novembro de 2024",
        },
        {
            "path": "static/images/romantic1.jpg",
            "message": "Mesmo em tempos difíceis você se faz meu porto seguro e me ajuda a encontrar meu ponto de equilíbrio e me empurra, para que eu siga em frente mesmo com todos os desafios...",
            "chronology": "Novembro 2024",
        },
        {
            "path": "static/images/romantic3.jpg",
            "message": "Mal posso esperar pelos momentos com você que estão por vir. Estamos entrando em uma nova aventura das nossas vidas e sei que juntos não temos com o que nos preocupar.",
            "chronology": "Novembro 2024",
        },
    ]
    return render_template("index.html", images_data=images_data)

@app.route("/qrcode")
def generate_qr():
    # URL do site
    site_url = "https://leokaique10.pythonanywhere.com/"
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
