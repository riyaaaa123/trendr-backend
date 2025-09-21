# Meesho Dice Hackathon Project – Backend

### Team Members :
- Bhumika Bachchan
-  Riya Jindal
-  Yukta Agrawal

## Project Overview

This project is the backend for **Meesho app** aimed at enhancing the shopping and social experience for users and influencers.

<img width="1096" height="766" alt="image" src="https://github.com/user-attachments/assets/03c73fd8-355f-4903-87e0-e9aa38909b3e" />


## Key goals

- Let users create and personalized wishlists for different occasions.
- Allow influencers to upload reels and tag products in them.
- Enable users to interact with products via swipe gestures (like/reject).
- Maintain a leaderboard for most liked Reel.

--- 

## Features

### 1. Influencer Reels with Product Tagging
 - Influencers on Meesho can upload reels showcasing products available on the platform.
 - Products are tagged within the reel, allowing users to explore and purchase items seamlessly.
 - Engagement metrics such as likes and shares, are tracked to provide influencers with actionable insights. 
### 2. Swipe-Based Product Interaction
 - Users can swipe left to dismiss a product or swipe right to add it to their wishlist, creating an engaging, gamified shopping journey within Meesho.
 -  The backend updates wishlists and user preferences in real-time, enabling dynamic product recommendations based on interactions.
### 3. Dashboard and reward system
 - Influencers have access to a dedicated dashboard that displays these metrics, helping them optimize content and engagement.
 - Additionally, a coin/reward system incentivizes influencers based on the reel performance, motivating higher-quality content creation.
### 4. Personalized and Shareable Wishlists
 - Allows the users to create multiple wishlists within Meesho for specific occasions- birthdays, festivals, or events.
 - Each wishlist can be shared with friends or family, enabling collaborative shopping experiences.
### 5. Leaderboard for Top Reels
 - A weekly leaderboard highlights top-performing reels based on engagement metrics, encouraging community participation and rewarding influencers.

---

## Backend Architecture

- **Framework**: Django + Django REST Framework
- **Authentication**: JWT (JSON Web Tokens)
- **Database**: SQLite
- **Key Models**:
  - `User`: User information and authentication
  - `Wishlist`: Occasion-based product collections
  - `Product`: Product details
  - `Videos`: Influencer reels with tagged products
  - `WishListShare`: to share personal wishlist with other users
- **API Endpoints:**
  - `/api/signup/` — create a new user
  - `/api/login/` — user login, returns JWT tokens
  - `/api/profile/` — fetch user profile
  - `/api/products/` — CRUD operations for products
  - `/api/videos/` — CRUD operations for reels
  - `/api/wishlists/` — create/view/update user wishlists

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/riyaaaa123/trendr-backend.git
cd trendr-backend
```

### 2. Create virtual environment
```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install all dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply database migrate 
```bash
python manage.py migrate
```

### 5. Create SuperUser(optional - for admin access)
```bash
python manage.py createsuperuser
```

### 6. Run Server 
```bash
python manage.py runserver
```

The backend will be available at http://localhost:8000/.
