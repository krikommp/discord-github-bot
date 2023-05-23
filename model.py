from pydantic import BaseModel
from typing import List

class Repository(BaseModel):
    pass

class Sender(BaseModel):
    pass

class Pusher(BaseModel):
    pass

class Persion(BaseModel):
    name: str
    email: str
    username: str
    
class CommitsItem(BaseModel):
    id: str
    tree_id: str
    distinct: bool
    message: str
    timestamp: str
    url: str
    author: Persion
    committer: Persion
    added: List[str]
    removed: List[str]
    modified: List[str]

class HeadCommit(BaseModel):
    id: str
    tree_id: str
    distinct: bool
    message: str
    timestamp: str
    url: str
    author: Persion
    committer: Persion
    added: List[str]
    removed: List[str]
    modified: List[str]

class Root(BaseModel):
    ref: str
    before: str
    after: str
    repository: Repository
    pusher: Pusher
    sender: Sender
    created: bool
    deleted: bool
    forced: bool
    compare: str
    commits: List[CommitsItem]
    head_commit: HeadCommit
        