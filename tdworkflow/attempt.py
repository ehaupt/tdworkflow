import dataclasses
from typing import Dict

from .project import Project
from .workflow import Workflow


@dataclasses.dataclass
class Attempt:
    id: int
    sessionId: int = -1
    sessionUuid: str = ""
    sessionTime: str = ""
    workflow: Workflow = None
    project: Project = None
    index: int = -1
    retryAttemptName: str = ""
    done: bool = False
    success: bool = False
    cancelRequested: bool = False
    params: Dict = None
    createdAt: str = ""
    finishedAt: str = ""

    def __post_init__(self):
        self.id = int(self.id)
        if self.project and isinstance(self.project, dict):
            self.project = Project(**self.project)
        if self.workflow and isinstance(self.workflow, dict):
            self.workflow = Workflow(**self.workflow)
        self.done = bool(self.done)
        self.success = bool(self.success)
        self.cancelRequested = bool(self.cancelRequested)

    @property
    def session_id(self):
        return self.sessionId

    @property
    def session_uuid(self):
        return self.sessionUuid

    @property
    def sesesion_time(self):
        return self.sessionTime

    @property
    def retry_attempt_name(self):
        return self.retryAttemptName

    @property
    def cancel_requested(self):
        return self.cancelRequested

    @property
    def finished_at(self):
        return self.finishedAt

    def finished(self):
        return bool(self.finished_at)

    def update(self, **args):
        other_attempt = Attempt(**args)
        self.id = other_attempt.id
        self.sessionId = other_attempt.sessionId
        self.sessionUuid = other_attempt.sessionUuid
        self.workflow = other_attempt.workflow
        self.project = other_attempt.project
        self.index = other_attempt.index
        self.retryAttemptName = other_attempt.retryAttemptName
        self.done = other_attempt.done
        self.success = other_attempt.success
        self.cancelRequested = other_attempt.cancelRequested
        self.params = other_attempt.params
        self.createdAt = other_attempt.createdAt
        self.finishedAt = other_attempt.finishedAt
