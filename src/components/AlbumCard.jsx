import React from 'react';

const AlbumCard = ({ image, title, description }) => {
  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden">
      <img src={image} alt={title} className="w-full h-48 object-cover" />
      <div className="p-4">
        <h3 className="text-lg font-semibold">{title}</h3>
        <p className="text-sm text-gray-600">{description}</p>
        <div className="mt-4 flex justify-between">
          <button className="text-sm text-white bg-blue-500 px-3 py-1 rounded hover:bg-blue-600">View</button>
          <button className="text-sm text-white bg-gray-500 px-3 py-1 rounded hover:bg-gray-600">Edit</button>
        </div>
      </div>
    </div>
  );
};

export default AlbumCard;
