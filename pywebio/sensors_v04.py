#!/usr/bin/env python3
# vim: set fileencoding=utf-8

from minio import Minio, ResponseError
import pandas as pd
from io import StringIO

bucket_name = "sensors"
minio_address = "localhost:9000"
minio_access_key = "tester"
minio_secret_key = "tester01"


def main():
    client = Minio(minio_address, minio_access_key, minio_secret_key, secure=False)

    found = client.bucket_exists(bucket_name)
    print("Bucket found:", found)

    objects = client.list_objects(bucket_name, recursive=False)

    for obj in objects:
        print(
            obj.bucket_name,
            obj.object_name,
            obj.last_modified,
            obj.etag,
            obj.size,
            obj.content_type,
        )
        try:
            response = client.get_object(bucket_name, obj.object_name)
            buff = StringIO(response.read().decode())
            data = pd.read_csv(buff)
            print(data)
        except ResponseError as err:
            print(err)
        finally:
            response.close()
            response.release_conn()


if __name__ == "__main__":
    main()
