import React, { useState } from 'react';
import axios from 'axios';

const FileUpload = ({ onUpload }) => {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    try {
      if (!selectedFile) {
        alert('Please select a file.');
        return;
      }

      const formData = new FormData();
      formData.append('file', selectedFile);

      // Replace 'YOUR_BACKEND_ENDPOINT' with the actual backend endpoint where you want to upload the file
      const response = await axios.post('YOUR_BACKEND_ENDPOINT', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });

      // Pass the response or any necessary data back to the parent component
      onUpload(response.data);
      
      // Optionally, clear the selected file after successful upload
      setSelectedFile(null);
    } catch (error) {
      console.error('Error uploading file:', error);
      // Handle error accordingly, e.g., display an error message
    }
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
};

export default FileUpload;


