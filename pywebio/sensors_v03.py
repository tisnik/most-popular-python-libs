#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from minio import Minio, ResponseError

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
            data = response.read().decode()
            print(data)
        except ResponseError as err:
            print(err)
        finally:
            response.close()
            response.release_conn()


if __name__ == "__main__":
    main()
