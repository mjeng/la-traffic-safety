from google.cloud import storage
import pickle

BUCKET_NAME = "grid-data"

storage_client = storage.Client()

def upload_blob(source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(BUCKET_NAME)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

def download_blob(source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(BUCKET_NAME)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print('Blob {} downloaded to {}.'.format(
        source_blob_name,
        destination_file_name))

def cloud_pickle_load(file_name):
    download_blob(file_name, file_name)
    pick = pickle.load( open(file_name, "rb" ) )
    return pick

def cloud_pickle_dump(file, file_name):
    pickle.dump(file, open(file_name, "wb" ) )
    upload_blob(file_name, file_name)
