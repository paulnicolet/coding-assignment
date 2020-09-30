from enum import Enum


class Status(Enum):
    """Represents a class status.
    """
    VALID = 'valid'
    INVALID = 'invalid'
    GRANULARITY_STAGED = 'granularity_staged'
    COVERAGE_STAGED = 'coverage_staged'

    @classmethod
    def aggregate(cls, statuses):
        """Returns the status to keep from a set of statuses, using defined priorities.

        Args:
            statuses (Set[Status]): A set of statuses.

        Returns:
            Status: The final status taking precedence over the others.
        """
        if cls.INVALID in statuses:
            return cls.INVALID

        if cls.COVERAGE_STAGED in statuses:
            return cls.COVERAGE_STAGED

        if cls.GRANULARITY_STAGED in statuses:
            return cls.GRANULARITY_STAGED

        return cls.VALID
