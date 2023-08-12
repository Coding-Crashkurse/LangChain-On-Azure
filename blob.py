from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

connection_string = "DefaultEndpointsProtocol=https;AccountName=mystoragemyname123;AccountKey=HyrwrdWWQm7X8Z5BSzIt4StbjYPX/VFGJ2L+j12B2nkb5ZJbLZG0ElKUT2SP5hxYaGP7W2Oxmo5F+AStCubK3w==;EndpointSuffix=core.windows.net"  #
container_name = "mycontainer"
blob_name = "mystoragemyname123"
directory_path = "Data"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

for root, dirs, files in os.walk(directory_path):
    for file in files:
        file_path = os.path.join(root, file)
        blob_name = os.path.relpath(file_path, directory_path)

        blob_client = blob_service_client.get_blob_client(
            container=container_name, blob=blob_name
        )

        with open(file_path, "rb") as data:
            blob_client.upload_blob(data)

        print(f"Datei {file_path} erfolgreich zu {blob_name} hochgeladen!")
