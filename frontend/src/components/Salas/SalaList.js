import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const SalaList = () => {
    const [salas, setSalas] = useState([]);

    useEffect(() => {
        fetchSalas();
    }, []);

    const fetchSalas = async () => {
        try {
            const response = await axios.get('/api/salas/');
            setSalas(response.data);
        } catch (error) {
            console.error('Erro ao buscar salas:', error);
        }
    };

    return (
        <div>
            <h2>Salas</h2>
            <Link to="/salas/nova">Adicionar Nova Sala</Link>
            <ul>
                {salas.map(sala => (
                    <li key={sala.id}>
                        {sala.nome} - Capacidade: {sala.capacidade}
                        <Link to={`/salas/${sala.id}`}>Detalhes</Link>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default SalaList;
