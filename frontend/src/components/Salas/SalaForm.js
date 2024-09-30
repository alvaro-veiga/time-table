import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const SalaForm = () => {
    const [nome, setNome] = useState('');
    const [capacidade, setCapacidade] = useState('');
    const [recursos, setRecursos] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post('/api/salas/', { nome, capacidade, recursos });
            navigate('/salas');
        } catch (error) {
            console.error('Erro ao criar sala:', error);
        }
    };

    return (
        <div>
            <h2>Adicionar Nova Sala</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Nome:</label>
                    <input type="text" value={nome} onChange={(e) => setNome(e.target.value)} required />
                </div>
                <div>
                    <label>Capacidade:</label>
                    <input type="number" value={capacidade} onChange={(e) => setCapacidade(e.target.value)} required />
                </div>
                <div>
                    <label>Recursos:</label>
                    <textarea value={recursos} onChange={(e) => setRecursos(e.target.value)}></textarea>
                </div>
                <button type="submit">Salvar</button>
            </form>
        </div>
    );
};

export default SalaForm;
