from job import Job, JobStatus

class JobRepository:
    def __init__(self):
        # connect to database
        pass

    def add_job(self, job: Job):
        # add job to database
        pass

    def claim_next_job(self):
        # return the next job in queue and mark it as in progress
        pass

    def update_status(self, job_id: int, status: JobStatus):
        # update the status of the job with the given id
        pass
