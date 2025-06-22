import React from 'react';

const Header = () => {
  return (
    <header className="fixed top-0 left-0 w-full bg-white shadow-md z-10">
      <div className="max-w-7xl mx-auto px-4 py-3 flex justify-between items-center">
        <h1 className="text-xl font-bold">Album</h1>
        <button className="text-sm bg-gray-800 text-white px-3 py-1 rounded hover:bg-gray-700">
          Sign up
        </button>
      </div>
    </header>
  );
};

export default Header;
