import React from 'react';
import Header from './components/Header.jsx';
import PhotoCard from './components/PhotoCard.jsx';
import MiddleBody from './components/MiddleBody.jsx';


function App() {
  const cards = Array.from({ length: 9 }, (_, i) => ({
    id: i,
    title: `사진 ${i + 1}`,
    imgURL: '/assets/sunset.jpeg',
    content: "This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer."
  }));

  return (
    <>
    <Header />
    <MiddleBody />

    {/* 카드들 그리드로 배치 */}
    <div style={{
      width: '100%',
      display: 'grid',
      gridTemplateColumns: 'repeat(3, 1fr)',
      gap: '40px',
      padding: '60px 30px',
      marginBottom: '40px',
      backgroundColor: '#f8f9fa',
      boxSizing: 'border-box',
    }}>
      {cards.map(card => (
        <PhotoCard key={card.id} title={card.title} imgURL={card.imgURL} content={card.content} />
      ))}
    </div>

    </>
  )
}

export default App