from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from silhouette import generate_svg_from_image_bytes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process")
async def process_image(file: UploadFile = File(...)):
    contents = await file.read()
    svg = generate_svg_from_image_bytes(contents)
    return {"svg": svg}
