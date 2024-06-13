import React, { useState, useEffect } from 'react';
import FavoriteBorderOutlinedIcon from '@mui/icons-material/FavoriteBorderOutlined';
import axios from 'axios';

function Posts() {
    const [cardData, setCardData] = useState([]);

    useEffect(() => {
      const fetchData = async () => {
        try {
          const response = await axios.get('https://monilmeh.pythonanywhere.com//api/posts', {
            headers: {
              'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4MjY5MzkxLCJpYXQiOjE3MTgyNDc3OTEsImp0aSI6ImI1NDU5NTYyOThhMDQwNGY4ZTkzN2JkYWM0MjRiNjYyIiwidXNlcl9pZCI6IjYwMDA0MjIwMjA3In0.3Tap7Xk9toixMMOwbnkgegqcg4vBZ-3WJvLlyoST97g'
            }
          });
          console.log('API Response:', response.data); // Log the API response
          const data = response.data.map((item) => ({
            heading1: item.title,
            body: item.description,
            icon: <FavoriteBorderOutlinedIcon className="text-blue-500" style={{ width: '20px', height: '20px' }} />,
            timelimit: item.likes,
            category: item.subtype, 
            url: item.post_url,
            deadlines: item.deadline,
            image: item.image,
          }));
          console.log('Mapped Data:', data); 
          setCardData(data);
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      };
      fetchData();
    }, []);
  return (
    <div className='flex flex-col w-full'>
    
    
    <div className='grid grid-cols-1 gap-5 m-10 md:grid-cols-2 md:gap-10'>
      {cardData.map((data, i) => {
        return (
          <div className='flex justify-evenly mr-1 ml-1 md:mr-2 md:ml-2 lg:mr-4 lg:ml-2' key={i}>
            <div className='border p-3 rounded-lg bg-gray-200 w-full'>
              <p className='font-bold text-[18px] md:text-[15px]'>{data.heading1}</p>
              <div className='flex flex-col items-center'>
                <img src={data.image} alt={data.heading1} className='w-full h-80 object-cover mb-3' />
                <p className='mt-2 text-sm border-b-[1px] pb-3 text-[16px]'>{data.body}</p>
              </div>
              <p className='font-bold text-[18px] md:text-[15px] border-custom-blue'>{data.url}</p>
              <div className='flex justify-between'>
                <div className='flex items-center'>
                  {data.icon}
                  <p className='text-custom-blue font-bold md:font-normal'>{data.timelimit}</p>
                </div>
                <p className='text-custom-blue font-bold md:font-normal'>{data.category}</p>
                <p className='text-custom-blue font-bold md:font-normal'>{data.deadlines}</p>
              </div>
            </div>
          </div>
        );
      })}
    </div>
  </div>
  )
}

export default Posts