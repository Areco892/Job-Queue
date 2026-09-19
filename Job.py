class JobStatus:
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

class Job:
    def __init__(self, type, payload):
        self.type = type
        self.payload = payload
        self.status = JobStatus.PENDING
        self.created_at = None
        self.updated_at = None