"""Clean Code in Python - Chapter 8: Unit Testing & Refactoring

> Frameworks and Libraries for Unit Testing

"""

from mrstatus import MergeRequestException
from mrstatus import MergeRequestExtendedStatus as MergeRequestStatus
from ut_frameworks_3 import AcceptanceThreshold


class MergeRequest:
    def __init__(self):
        self._context = {"upvotes": set(), "downvotes": set()}
        self._status = MergeRequestStatus.OPEN

    def close(self):
        self._status = MergeRequestStatus.CLOSED

    @property
    def status(self):
        if self._status == MergeRequestStatus.CLOSED:
            return self._status

        return AcceptanceThreshold(self._context).status()

    def _cannot_vote_if_closed(self):
        if self._status == MergeRequestStatus.CLOSED:
            raise MergeRequestException("can't vote on a closed merge request")

    def upvote(self, by_user):
        self._cannot_vote_if_closed()

        self._context["downvotes"].discard(by_user)
        self._context["upvotes"].add(by_user)

    def downvote(self, by_user):
        self._cannot_vote_if_closed()

        self._context["upvotes"].discard(by_user)
        self._context["downvotes"].add(by_user)
