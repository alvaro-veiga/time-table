import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams, Link, useNavigate } from 'react-router-dom';

const SalaDetail = () => {
    const { id } = useParams();
    const [sala, setSala] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        fetchSala();
    }, []);

    const fetchSala = async () => {
        try {
            const response = await axios.get(`/api/salas/${id}/`);
            setSala(response.data);
        } catch (error) {
            console.error('Erro ao buscar sala:', error);
        }
    };

    const handleDelete = async () => {
        try {
            await axios.delete(`/api/salas/${id}/`);
            navigate('/salas');
        } catch (error) {
            console.error('Erro ao deletar sala:', error);
        }
    };

    if (!sala) return <div>Carregando...</div>;

    return (
        <div>
            <h2>Detalhes da Sala</h2>
            <p><strong>Nome:</strong> {sala.nome}</p>
            <p><strong>Capacidade:</strong> {sala.capacidade}</p>
            <p><strong>Recursos:</strong> {sala.recursos}</p>
            <button onClick={handleDelete}>Deletar Sala</button>
            <Link to="/salas">Voltar para Salas</Link>
        </div>
    );
};

export default SalaDetail;