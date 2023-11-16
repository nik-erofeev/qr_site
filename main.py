import qrcode
from fastapi import FastAPI
from starlette.responses import StreamingResponse
from io import BytesIO  
import uvicorn

app = FastAPI()


@app.get('/generate-qr-code')
def generate_qrcode(string: str) -> StreamingResponse:
    qr = qrcode.QRCode(box_size=10,
                       border=10)

    qr.add_data(string)

    image = qr.make_image()

    data = BytesIO()
    image.save(data)

    data.seek(0)
    return StreamingResponse(data, media_type='img/png', headers={"Content-Disposition": "attachment; filename=generate-qr-code.png"})


uvicorn.run(app, port=9500)
