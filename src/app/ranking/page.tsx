"use client";

import { useEffect, useState } from "react";
import { User } from "../types/interfaces";


export default function RankingPage() {

  const [users, setUsers] = useState<User[]>([]);
  const [currentUser, setCurrentUser] = useState([0, "", 0]);

  useEffect(() => {
    const fetchUserRanking = async () => {
      const sessionId = sessionStorage.getItem('session_id');
      if (!sessionId) return;

      try {
        const response = await fetch('http://localhost:8000/api/get_user_ranking/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ session_id: sessionId }),
        });
        if (!response.ok) throw new Error('Failed to fetch user ranking');
        const data = await response.json();
        setUsers(data.serialized_ranking);
      } catch (error) {
        console.error('Error fetching ranking:', error);
      }
    };

    fetchUserRanking();
  }, []);

  useEffect(() => {
    const fetchCurrentUser = async () => {
      const sessionId = sessionStorage.getItem('session_id');
      if (!sessionId) return;

      try {
        const response = await fetch('http://localhost:8000/api/get_user_info/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ session_id: sessionId }),
        });
        if (!response.ok) throw new Error('Failed to fetch user information');
        const data = await response.json();
        setCurrentUser([data.user_id, data.username, data.score]);
      } catch (error) {
        console.error('Error fetching user ID:', error);
      }
    };

    fetchCurrentUser();
  }, []);


  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-6 bg-gray-50">
      {currentUser && (
        <div className="mb-6 p-4 bg-blue-100 rounded-lg shadow-md">
          <h2 className="text-xl font-bold mb-2">{currentUser[1]} - {currentUser[2]}</h2>
        </div>
      )}
      <div>
        <ol>
          {users.map((user, position) => (
            <li
              key={user.id}
              className={`shadow-md rounded-lg p-6 mb-4 ${user.id === currentUser[0] ? 'bg-green-300' : 'bg-white'}`}
            >
              <h2 className="text-xl font-bold mb-2">{position + 1}. {user.username} {user.score}</h2>
            </li>
          ))}
        </ol>
      </div>
      <footer className="mt-8">
        <p className="text-sm text-gray-500">
          © {new Date().getFullYear()} IdzDoParku. All rights reserved.
        </p>
      </footer>
    </div>
  );
}
