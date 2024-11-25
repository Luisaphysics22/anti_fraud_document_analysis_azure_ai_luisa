from azure.storage.blob import BlobServiceClient


CONNECTION_STRING = "YOUR_CONNECTION_STRING"
CONTAINER_NAME = "YOUR_CONTAINER_NAME"

def upload_test(file_path, blob_name):
    try:
        # Conexão com o serviço Blob
        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)

        # Faz upload de um arquivo local
        with open(file_path, "rb") as data:
            blob_client = container_client.get_blob_client(blob_name)
            blob_client.upload_blob(data, overwrite=True)
            print(f"Arquivo {blob_name} enviado com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")

# Teste
if __name__ == "__main__":
    # Insira o caminho do arquivo que deseja testar
    upload_test(r"C:\Users\luisa\OneDrive\Documentos\DIO\BOOTCAMP MICROSOFT AZURE AI-102\DOCS\nubank.jpg", "nubank.png")
