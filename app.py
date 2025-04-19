from flask import Flask, request, send_file, send_from_directory
import qrcode
import io
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/generate_qr')
def generate_qr():
    data = request.args.get('data')
    if not data:
        return "Missing data", 400

    # Convert to bytes and check byte length
    byte_data = data.encode('utf-8')  # Use 'utf-8' encoding
    if len(byte_data) >= 2953:
        return "Data too long for QR code (limit: 2952 bytes)", 413  # HTTP 413: Payload Too Large

    try:
        img = qrcode.make(data)
    except:
        return "Could not generate QR Code.", 413

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return send_file(buffer, mimetype='image/png')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 6000))
    app.run(host='0.0.0.0', port=port)
