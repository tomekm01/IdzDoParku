"use client";

import { useEffect, useState } from "react";
import { POI } from "../types/interfaces";

export default function POIListPage() {
  const [pois, setPois] = useState<POI[]>([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/pois/")
      .then((response) => response.json())
      .then((data) => setPois(data));
  }, []);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-6 bg-gray-50">
      <div className="grid gap-8 lg:grid-cols-2">
        <h1>POI List</h1>
      </div>
      <div>
        <ol>
          {pois.map((poi) => (
            <li
              key={poi.poi_id}
              className="bg-white shadow-md rounded-lg p-6 mb-4"
            >
              <h2 className="text-xl font-bold mb-2">{poi.name}</h2>
              <p className="text-gray-700">Park: {poi.park.park_name}</p>
              <p className="text-gray-700">Opis: {poi.description}</p>
              <p className="text-gray-700">
                Wartość punktowa: {poi.score_worth}
              </p>
              <a
                href={`/poi/${poi.poi_id}`}
                className="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-lg transition-colors mt-4 inline-block"
              >
                View Details
              </a>
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
