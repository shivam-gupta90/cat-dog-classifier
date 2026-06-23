from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from PIL import Image

import torch

from torchvision import transforms

from model import CNN

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


model = CNN()

model.load_state_dict(
    torch.load(
        "cat_dog_model.pth",
        map_location="cpu"
    )
)

model.eval()


transform = transforms.Compose([
    transforms.Resize((128,128)),
    transforms.ToTensor()
])


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    image = Image.open(file.file)

    image = image.convert("RGB")

    image = transform(image)

    image = image.unsqueeze(0)

    with torch.no_grad():

        output = model(image)

        prob = torch.sigmoid(output).item()

    prediction = (
        "Dog"
        if prob > 0.5
        else "Cat"
    )

    confidence = round(
        max(prob,1-prob)*100,
        2
    )

    return {
        "prediction": prediction,
        "confidence": confidence
    }