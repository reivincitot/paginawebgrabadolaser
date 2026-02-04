import React from 'react'

function App() {
  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1>🎉 ¡Laser Store está funcionando!</h1>
      <p>Frontend React corriendo correctamente.</p>
      <div style={{ marginTop: '20px', padding: '10px', background: '#f0f0f0' }}>
        <h3>Servicios disponibles:</h3>
        <ul>
          <li>Product API: http://localhost:8002</li>
          <li>Orders API: http://localhost:8003</li>
          <li>Clients API: http://localhost:8004</li>
        </ul>
      </div>
    </div>
  )
}

export default App
