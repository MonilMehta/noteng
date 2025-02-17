import React, { useEffect, useState } from 'react';
import JobCard from './JobCard';

function Jobs() {
  const [jobs, setJobs] = useState([]);
  const token = localStorage.getItem('token');
  console.log(token);
  useEffect(() => {
    fetch('https://monilmeh.pythonanywhere.com/api/jobboard/', {
      headers: {
        'Authorization': `Bearer ${token}` 
      }
    })
      .then(response => response.json())
      .then(data => setJobs(data))
      .catch(error => console.error('Error fetching jobs:', error));
  }, [token]);

  const handleDelete = (jobId) => {
    fetch(`https://monilmeh.pythonanywhere.com/api/jobboard/${jobId}/`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${token}` 
      }
    })
      .then(response => {
        if (response.ok) {
          setJobs(jobs.filter(job => job.job_id !== jobId));
        } else {
          console.error('Error deleting job');
        }
      })
      .catch(error => console.error('Error deleting job:', error));
  };
  console.log(jobs);

  return (
    <div className='m-6 grid grid-cols-1 md:grid-cols-2 gap-4'>
      {jobs.length === 0 ? (
        <h1 className='flex justify-center items-center self-center font-semibold text-xl md:text-2xl lg:text-3xl'>Please wait jobs openings migth be loading...</h1>
      ) : (
        jobs.map((job) => (
          <JobCard key={job.job_id} job={job} onDelete={handleDelete} />
        ))
      )}
    </div>
  );
}
export default Jobs;
