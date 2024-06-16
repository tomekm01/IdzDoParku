"use client";

import { useEffect, useState } from "react";
import { Achievement } from "../types/interfaces";

export default function AchievementsPage() {
  
  const [achievements, setAchievements] = useState<Achievement[]>([]);
  const [userAchievements, setUserAchievements] = useState<Achievement[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(true);

  useEffect(() => {
    fetch("http://localhost:8000/api/achievements/")
      .then((response) => response.json())
      .then((data) => {
        console.log("Fetched Achievements:", data);
        setAchievements(data)});
  }, []);

  useEffect(() => {
    const fetchUserAchievements = async () => {
      const sessionId = sessionStorage.getItem('session_id');
      if (!sessionId) return;

      try {
        const response = await fetch('http://localhost:8000/api/get_user_achievements/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ session_id: sessionId }),
        });
        if (!response.ok) throw new Error('Failed to fetch user achievements');
        const data = await response.json();
        //console.log("User Achievements:", data.serialized_achievements);
        setUserAchievements(data.serialized_achievements);
        setIsLoading(false);
      } catch (error) {
        console.error('Error fetching achievements:', error);
      }
    };

    fetchUserAchievements();
  }, []);


  const isUserAchievement = (achievementId: number) => {
    console.log("Checking Achievement ID:", achievementId);
    console.log("User Achievements:", userAchievements);
    return Array.isArray(userAchievements) && userAchievements.some(ach => ach.id === achievementId);
  };

  if (isLoading) {
    return( 
    <div className="flex flex-col items-center justify-center min-h-screen py-6 bg-gray-50">
    <div className="grid gap-8 lg:grid-cols-2">
      <h1>Loading...</h1>
    </div>
  
    <footer className="mt-8">
      <p className="text-sm text-gray-500">
        © {new Date().getFullYear()} IdzDoParku. All rights reserved.
      </p>
    </footer>
    </div>
    );
  }

  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-6 bg-gray-50">
      <div className="grid gap-8 lg:grid-cols-2">
        <h1>Achievements</h1>
      </div>
      <div>
        <ol>
          {achievements.map((achievement) => (
            <li
              key={achievement.id}
              className={`shadow-md rounded-lg p-6 mb-4 ${isUserAchievement(achievement.id) ? 'bg-green-300' : 'bg-white'}`}
            >
              <h2 className="text-xl font-bold mb-2">{achievement.name}</h2>
              <p className="text-gray-700">Opis: {achievement.description}</p>
              <p className="text-gray-700">Wymagania: {achievement.requirements}</p>
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
