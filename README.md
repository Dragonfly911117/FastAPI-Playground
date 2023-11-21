# FakeCDN

## Run

```bash
uvicorn main:app --reload
```
## Upload file

```bash
curl -X POST -F "file=@./test.txt" http://localhost:8000/FakeCDN/upload
```
or <br> Run the [test.http](/test.http) request with fixed file path

## Get file

* http://localhost:8000/FakeCDN/all for listing all files
* http://127.1:8000/FakeCDN/{id} for getting the file with id(0-indexed)


# Misc things
The file uploaded is stored in the directory "/uploaded_files" and attached with a timestamp
