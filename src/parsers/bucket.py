from ..dataclasses.bucket import *


def parse_bucket(buckets: list[dict]) -> list[Bucket]:
    return [
        Bucket(name=bucket.get("Name"), creation_date=bucket.get("CreationDate"),)
        for bucket in buckets
    ]


def parse_contents(contents_raw: list[dict]) -> list[Content]:
    return [
        Content(name=content.get("Key"), last_modified=content.get("LastModified"))
        for content in contents_raw
    ]
