# viedoApp
install all packages of requirements.py in your environment before running 
    pip install -r "requirements.txt" 
    
    
Available Api endpoints = [
  {
  path: '',
  description: get request for getting list of uploaded videos and post request for uploading, 
  allowed_method: GET, POST,
  expected_request_body:{ title:charType, video: files with .mp4 or .mkv extension }
  },
  
  {
  path: 'add/',
  description: get request for getting list of uploaded videos,
  allowed_method: POST,
  expected_request_body:{ title:charType, video: files with .mp4 or .mkv extension }
  },
  path: 'charges/',
  description: get request for getting list of uploaded videos,
  allowed_method: POST,
  expected_request_body:{ 'video_size_in_MB': 'size in mb',
        'length_in_sec': 'type of video format',
        'type':'video format' }
  },
  
]



        
