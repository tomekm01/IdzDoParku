// src/types/interfaces.ts

// Interfejs dla tabeli "Parks"
export interface Park {
  park_id: number; // lub string, jeśli używasz UUID
  park_name: string;
  location: string;
  description: string;
}

// Interfejs dla tabeli "Achievements"
export interface Achievement {
  achievement_id: number; // lub string, jeśli używasz UUID
  name: string;
  description: string;
  requirements: string;
}

// Interfejs dla tabeli "Users"
export interface User {
  user_id: number; // lub string, jeśli używasz UUID
  username: string;
  password_hash: string;
  email: string;
  registration_date: Date;
  score: number;
}

// Interfejs dla tabeli "POIs"
export interface POI {
  poi_id: number;
  park: {
    park_name: string;
  };
  name: string;
  description: string;
  latitude: number;
  longitude: number;
  qr_code: string;
  additional_info_link: string;
  score_worth: number;
}

// Interfejs dla tabeli "User_Achievements"
export interface UserAchievement {
  user_achievement_id: number; // lub string, jeśli używasz UUID
  user_id: number; // lub string, jeśli używasz UUID
  achievement_id: number; // lub string, jeśli używasz UUID
}

// Interfejs dla tabeli "Login_Sessions"
export interface LoginSession {
  session_id: number; // lub string, jeśli używasz UUID
  user_id: number; // lub string, jeśli używasz UUID
  start_date: Date;
  end_date: Date;
}

// Interfejs dla tabeli "QR_Scans"
export interface QRScan {
  scan_id: number; // lub string, jeśli używasz UUID
  poi_id: number; // lub string, jeśli używasz UUID
  user_id: number; // lub string, jeśli używasz UUID
  scan_date: Date;
}

// Interfejs dla tabeli "Comments"
export interface Comment {
  comment_id: number; // lub string, jeśli używasz UUID
  poi_id: number; // lub string, jeśli używasz UUID
  user_id: number; // lub string, jeśli używasz UUID
  content: string;
  comment_date: Date;
}
