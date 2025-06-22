import React from 'react';
import Header from '../components/Header';
import AlbumCard from '../components/AlbumCard';
import Footer from '../components/Footer';
import sampleImage from '../assets/sample.jpg';

const AlbumPage = () => {
  const albums = Array(9).fill({
    image: sampleImage,
    title: 'Album Title',
    description: 'This is a wider card with supporting text below.',
  });

  return (
    <>
      <Header />
      <main className="pt-20 max-w-7xl mx-auto px-4">
        <section className="text-center my-12">
          <h2 className="text-3xl font-bold mb-2">Album Example</h2>
          <p className="text-gray-600">Something short and leading about the collection.</p>
        </section>

        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
          {albums.map((album, idx) => (
            <AlbumCard
              key={idx}
              image={album.image}
              title={album.title}
              description={album.description}
            />
          ))}
        </div>
      </main>
      <Footer />
    </>
  );
};

export default AlbumPage;
