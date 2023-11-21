from fastapi import APIRouter, File
from fastapi.responses import FileResponse
import os

router = APIRouter(prefix="/FakeCDN", tags=["FakeCDN"])

def list_files(dir_path):
    res = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            res.append(os.path.join(root, file))
    return res

# Replace 'your_directory_path' with the actual directory path
list_files('your_directory_path')
@router.get("/all")
def index():
    return list_files("uploaded_files")


@router.get("/get/{id}")
async def getImgById(id: int):
    file_path = list_files("uploaded_files")[id]
    return FileResponse(file_path)
