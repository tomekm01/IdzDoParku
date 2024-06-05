"use client";

import React, { useEffect, useState } from "react";
import { POI, Comment } from "../types/interfaces";

const POIListPage = () => {
  const [pois, setPois] = useState<POI[]>([]);
  const [code, setCode] = useState("");
  const [currentPOI, setCurrentPOI] = useState<number | null>(null);
  const [comments, setComments] = useState<Comment[]>([]);
  const [newComment, setNewComment] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [invalidCode, setInvalidCode] = useState<boolean>(false);

  useEffect(() => {
    fetch("http://localhost:8000/api/pois/")
      .then((response) => response.json())
      .then((data) => setPois(data))
      .catch((error) => {
        console.error("Error fetching POIs:", error);
        setError("Error fetching POIs");
      });
  }, []);

  const handleCodeChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setCode(event.target.value);
  };

  const handleSubmit = (poiId: number) => (event: React.FormEvent) => {
    event.preventDefault();
    console.log(`Submitting QR code ${code} for POI ${poiId}`);
    fetch(`http://localhost:8000/api/pois/${poiId}/check_qr_code/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ qr_code: code }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("QR code validation response:", data);
        if (data.valid) {
          setCurrentPOI(poiId);
          fetchComments(poiId);
          setInvalidCode(false);
        } else {
          setCurrentPOI(null);
          setComments([]);
          setInvalidCode(true);
        }
      })
      .catch((error) => {
        console.error("Error validating QR code:", error);
        setError("Error validating QR code");
      });
  };

  const fetchComments = (poiId: number) => {
    fetch(`http://localhost:8000/api/pois/${poiId}/comments/`)
      .then((response) => response.json())
      .then((data) => setComments(data))
      .catch((error) => {
        console.error("Error fetching comments:", error);
        setError("Error fetching comments");
      });
  };

  const handleNewCommentChange = (
    event: React.ChangeEvent<HTMLTextAreaElement>
  ) => {
    setNewComment(event.target.value);
  };

  const handleAddComment = (poiId: number) => (event: React.FormEvent) => {
    event.preventDefault();
    console.log(`Adding comment to POI ${poiId}`);

    fetch(`http://localhost:8000/api/pois/${poiId}/add_comment/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ content: newComment }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Comment added:", data);
        setComments((prevComments) => [...prevComments, data]);
        setNewComment("");
        setError(null);
      })
      .catch((error) => {
        console.error("Error adding comment:", error);
        setError("Error adding comment");
      });
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-6 bg-gray-50">
      <div className="grid gap-8 lg:grid-cols-2">
        <h1>POI List</h1>
      </div>
      {error && <div className="text-red-500">{error}</div>}
      <div>
        <ol>
          {pois.map((poi) => (
            <li key={poi.id} className="bg-white shadow-md rounded-lg p-6 mb-4">
              <h2 className="text-xl font-bold mb-2">{poi.name}</h2>
              <p className="text-gray-700">Park: {poi.park.park_name}</p>
              <p className="text-gray-700">Opis: {poi.description}</p>
              <p className="text-gray-700">
                Wartość punktowa: {poi.score_worth}
              </p>
              <form
                onSubmit={handleSubmit(poi.id)}
                className="w-full max-w-lg mt-4"
              >
                <div className="flex items-center border-b-2 border-green-500 py-2">
                  <input
                    type="text"
                    value={code}
                    onChange={handleCodeChange}
                    placeholder="Wpisz kod zaliczenia POI"
                    className="appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none"
                  />
                  <button
                    type="submit"
                    className="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-lg transition-colors"
                  >
                    Dodaj
                  </button>
                </div>
              </form>
              {invalidCode && <p className="text-red-500">Błędny kod</p>}
              {currentPOI === poi.id && (
                <div className="bg-white shadow-md rounded-lg p-6 mt-4 w-full max-w-lg">
                  <h2>Komentarze</h2>
                  {comments.length > 0 ? (
                    comments.map((comment) => (
                      <p key={comment.id} className="text-gray-700">
                        {comment.content}
                      </p>
                    ))
                  ) : (
                    <p>Brak komentarzy</p>
                  )}
                  <form onSubmit={handleAddComment(poi.id)} className="mt-4">
                    <textarea
                      value={newComment}
                      onChange={handleNewCommentChange}
                      placeholder="Dodaj komentarz"
                      className="appearance-none bg-transparent border border-gray-300 w-full text-gray-700 py-2 px-3 leading-tight focus:outline-none"
                    />
                    <button
                      type="submit"
                      className="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-lg mt-2 transition-colors"
                    >
                      Dodaj komentarz
                    </button>
                  </form>
                </div>
              )}
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
};

export default POIListPage;
