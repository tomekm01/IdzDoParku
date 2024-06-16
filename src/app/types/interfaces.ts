export interface Park {
  id: number;
  park_name: string;
  location: string;
  description: string;
}

export interface Achievement {
  id: number;
  name: string;
  description: string;
  requirements: string;
}

export interface User {
  id: number;
  username: string;
  password_hash: string;
  email: string;
  registration_date: Date;
  score: number;
}

export interface POI {
  id: number;
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

export interface UserAchievement {
  id: number;
  user_id: number;
  achievement_id: number;
}

export interface LoginSession {
  id: number;
  user_id: number;
  start_date: Date;
  end_date: Date;
}

export interface QRScan {
  id: number;
  poi_id: number;
  user_id: number;
  scan_date: Date;
}

export interface Comment {
  id: number;
  poi_id: number;
  user_id: number;
  content: string;
  comment_date: Date;
}
