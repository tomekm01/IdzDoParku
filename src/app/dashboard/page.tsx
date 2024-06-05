'use client'
import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';

export default function DashboardPage() {
  const router = useRouter();
  const [username, setUsername] = useState('');

  useEffect(() => {
    const fetchUsername = async () => {
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
        setUsername(data.username);
      } catch (error) {
        console.error('Error fetching username:', error);
      }
    };

    fetchUsername();

    return () => {
      setUsername('');
    };
  }, []);

  const handleLogout = async () => {
    const sessionId = sessionStorage.getItem('session_id');
    if (!sessionId) return;

    try {
      await fetch('http://localhost:8000/api/logout/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ session_id: sessionId }),
      });
      sessionStorage.removeItem('session_id');
      router.push('.');
    } catch (error) {
      console.error('Logout error:', error);
    }
  };


  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-6 bg-gray-50">
      <div className="grid gap-8 lg:grid-cols-2">
        <div>
          <h1 className="text-3xl font-bold mb-4">Witaj {username || 'Username'}!</h1>
        </div>
        <div className="flex flex-col space-y-4 lg:justify-center items-center">
          <a
            href="/poi_list"
            className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-lg transition-colors"
          >
            Lista POI
          </a>
          <a
            href="/ranking"
            className="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-lg transition-colors"
          >
            Ranking
          </a>
          <a
            href="/achievements"
            className="bg-orange-500 hover:bg-orange-600 text-white font-bold py-2 px-4 rounded-lg transition-colors"
          >
            Achievements
          </a>
          <button
            onClick={handleLogout}
            className="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-lg transition-colors"
          >
            Logout
          </button>
        </div>
      </div>
      <footer className="mt-8">
        <p className="text-sm text-gray-500">
          © {new Date().getFullYear()} IdzDoParku. All rights reserved.
        </p>
      </footer>
    </div>
  );
}
