'use client'
import { useRouter } from 'next/navigation';
import { useState } from "react";

export default function LoginPage() {
  const router = useRouter();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleUsernameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setPassword(event.target.value);
  };

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    try {
      const response = await fetch("http://localhost:8000/api/login/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username,
          password,
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      console.log("Login successful:", data);
      router.push("/dashboard");
    } catch (error) {
      console.error("Login error:", error);
    }
  };


  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-6 bg-white">
    <form onSubmit={handleSubmit} className="bg-white rounded-lg shadow-lg p-8">
      <div className="mb-4">
        <label htmlFor="username" className="block text-gray-700 font-bold mb-2">Nazwa użytkownika:</label>
        <input
          type="text"
          id="username"
          value={username}
          onChange={handleUsernameChange}
          className="w-full px-3 py-2 leading-tight focus:outline-none focus:shadow-outline border border-gray-300 rounded-md"
        />
      </div>
      <div className="mb-4">
        <label htmlFor="password" className="block text-gray-700 font-bold mb-2">Hasło:</label>
        <input
          type="password"
          id="password"
          value={password}
          onChange={handlePasswordChange}
          className="w-full px-3 py-2 leading-tight focus:outline-none focus:shadow-outline border border-gray-300 rounded-md"
        />
      </div>
      <div className="md:flex md:items-center md:justify-center">
        <button type="submit" className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-lg transition-colors">Zaloguj się</button>
      </div>
    </form>
  </div>
  );
}
