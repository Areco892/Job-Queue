from datetime import datetime

from app.models import Job, JobStatus


def test_job_creation():
    job = Job(type="send_email", payload={"to": "test@example.com"})
    assert job.type == "send_email"
    assert job.payload == {"to": "test@example.com"}
    assert job.status == JobStatus.PENDING
    assert job.result is None
    assert job.error is None
    assert isinstance(job.id, str)
    assert isinstance(job.created_at, datetime)


def test_job_status_enum():
    assert JobStatus.PENDING.value == "pending"
    assert JobStatus.IN_PROGRESS.value == "in_progress"
    assert JobStatus.COMPLETED.value == "completed"
    assert JobStatus.FAILED.value == "failed"


def test_job_unique_id():
    job1 = Job(type="send_email", payload={"to": "test@example.com"})
    assert isinstance(job1.id, str)
    job2 = Job(type="send_email", payload={"to": "test2@example.com"})
    assert isinstance(job2.id, str)
    assert job1.id != job2.id
