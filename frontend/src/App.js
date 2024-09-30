import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import SalaList from './components/Salas/SalaList';
import SalaForm from './components/Salas/SalaForm';
import SalaDetail from './components/Salas/SalaDetail';

function App() {
  return (
    <Router>
      <div>
        <nav>
          <Link to="/salas">Salas</Link>
          {/* Adicione links para Professores, Disciplinas, etc. */}
        </nav>
        <Routes>
          <Route path="/salas" element={<SalaList />} />
          <Route path="/salas/nova" element={<SalaForm />} />
          <Route path="/salas/:id" element={<SalaDetail />} />
          {/* Adicione rotas para Professores, Disciplinas, etc. */}
          <Route path="/" element={<h1>Bem-vindo à Tabela de Horários</h1>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;