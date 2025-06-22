// src/components/MiddleBody.jsx
function MiddleBody() {
  const cards = new Array(9).fill(0); // 9개의 빈 카드

  return (
    <main style={{ paddingTop: '100px', paddingBottom: '2rem' }}>
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(3, 1fr)',
        gap: '1.5rem',
        padding: '0 2rem'
      }}>
        {cards.map((_, index) => (
          <div key={index} style={{
            border: '1px solid #ccc',
            borderRadius: '10px',
            padding: '1rem',
            textAlign: 'center'
          }}>
            <img
              src="/vite.svg"
              alt="이미지"
              style={{ width: '100%', height: '150px', objectFit: 'cover' }}
            />
            <p style={{ margin: '1rem 0 0 0' }}>이건 카드입니다!</p>
          </div>
        ))}
      </div>
    </main>
  );
}

export default MiddleBody;
