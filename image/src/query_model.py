import os
import time
from pydantic import BaseModel, Field
import boto3
import uuid
from typing import List, Optional
from botocore.exceptions import ClientError

TABLE_NAME = os.environ.get("TABLE_NAME")


class QueryModel(BaseModel):
    query_id: str = Field(default_factory=lambda: uuid.uuid4().hex)
    create_time: int = Field(default_factory=lambda: int(time.time()))
    query_text: str
    query_answer: Optional[str] = None
    sources: List[str] = Field(default_factory=list)
    is_complete: bool = False

    @classmethod
    def get_table(cls: "QueryModel") -> boto3.resource():
        dynamoDB = boto3.resource("dynamodb")
        return dynamoDB.table(TABLE_NAME)

    def put_items(self):
        items = self.as_ddb_item()
        try:
            response = QueryModel.get_table().put_item(Item=items)
            print(response)
        except ClientError as e:
            print("Client Error", e.response["Error"]["Message"])
            raise e

    def as_ddb_item(self):
        item = {k: v for k, v in self.dict().items() if v is not None}
        return item

    @classmethod
    def get_item(cls, query_id: str) -> "QueryModel":
        try:
            response = cls.get_table().get_item(Key={"query_id": query_id})
        except ClientError as e:
            print("ClientError", e.response["Error"]["Message"])
            return None

        if "Item" in response:
            item = response["Item"]
            return cls(**item)
        else:
            return None
