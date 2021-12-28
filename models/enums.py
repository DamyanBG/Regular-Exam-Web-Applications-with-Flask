import enum


class RoleType(enum.Enum):
    customer = "customer"
    worker = "worker"
    admin = "admin"


class State(enum.Enum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"
