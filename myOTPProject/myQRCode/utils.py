

import qrcode
from io import BytesIO
import base64



def generate_qr(verification_url):
    
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(verification_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # ইমেজটিকে সরাসরি মিডিয়া ফাইলে সেভ না করে মেমরিতে (Base64) রাখা ভালো
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    qr_base64 = base64.b64encode(buffer.getvalue()).decode()
    return qr_base64


