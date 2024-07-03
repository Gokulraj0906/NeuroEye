import React, { useState } from 'react';
import axios from 'axios';

const Home = () => {
  const [imageFile, setImageFile] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [data, setData] = useState(null);

  // Function to handle image selection
  const handleImageChange = (e) => {
    const file = e.target.files[0];
    setImageFile(file);

    // Create a preview of the selected image
    const reader = new FileReader();
    reader.onloadend = () => {
      setImagePreview(reader.result);
    };
    if (file) {
      reader.readAsDataURL(file);
    }
  };

  // Function to handle image upload
  const uploadImage = async () => {
    if (!imageFile) {
      console.error('Please select an image');
      return;
    }

    // Create a FormData object
    const formData = new FormData();
    formData.append('file', imageFile);

    try {
      // Send a POST request with Axios
      const response = await axios.post('http://127.0.0.1:5000', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });

      // Handle the response
      console.log('Image uploaded successfully:', response.data);
      setData(response.data.prediction);
    } catch (error) {
      // Handle errors
      console.error('Error uploading image:', error);
    }
  };

  // Inline styles
  const styles = {
    container: {
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      padding: '20px'
    },
    imagePreview: {
      width: '300px',
      height: '300px',
      objectFit: 'cover',
      marginTop: '20px',
      borderRadius: '10px'
    },
    button: {
      marginTop: '20px',
      padding: '10px 20px',
      fontSize: '16px',
      cursor: 'pointer'
    },
    result: {
      marginTop: '20px',
      fontSize: '24px',
      fontWeight: 'bold'
    }
  };

  return (
    <div style={styles.container}>
      <h2>Image Upload</h2>
      <input type="file" onChange={handleImageChange} />
      <button style={styles.button} onClick={uploadImage}>Upload Image</button>
      {imagePreview && <img src={imagePreview} alt="Image Preview" style={styles.imagePreview} />}
      {data && <div style={styles.result}>{data}</div>}
    </div>
  );
};

export default Home;
