from enum import Enum


class Status(Enum):
    VALID = 'valid'
    INVALID = 'invalid'
    GRANULARITY_STAGED = 'granularity_staged'
    COVERAGE_STAGED = 'coverage_staged'

    @classmethod
    def aggregate(cls, statuses):
        if cls.INVALID in statuses:
            return cls.INVALID

        if cls.COVERAGE_STAGED in statuses:
            return cls.COVERAGE_STAGED

        if cls.GRANULARITY_STAGED in statuses:
            return cls.GRANULARITY_STAGED

        return cls.VALID
