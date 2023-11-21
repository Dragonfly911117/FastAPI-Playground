import os
import shutil
from datetime import datetime
from typing import Annotated, Optional

from fastapi import FastAPI, File, UploadFile, APIRouter

prefix = "/FakeCDN"
router = APIRouter(prefix=prefix, tags=["FakeCDN"])

@router.post("/upload file/")
async def create_upload_file(file: UploadFile):
    flag = saveFile(file)
    return {"filename": file.filename, "content_type": file.content_type, "success": flag}

def saveFile(file: Optional[UploadFile]) -> bool:
    try:
        os.makedirs("uploaded_files", exist_ok=True)
        filename = file.filename.split(".")
        filename = f"{filename[0]}_{datetime.now().timestamp()}.{filename[1]}"
        with open(os.path.join("uploaded_files", filename), "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        return False
    return True
