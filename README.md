# Meesho Dice Hackathon Project – Backend

## Project Overview

This project is the backend for a **Meesho app** aimed at enhancing the shopping and social experience for users and influencers.

## Key goals

- Let users create and personalized wishlists for different occasions.
- Allow influencers to upload reels and tag products in them.
- Enable users to interact with products via swipe gestures (like/reject).
- Maintain a leaderboard for most liked Reel.

## Features

### 1. Personalized and Shareable Wishlists

- Users can create multiple wishlists for specific occasions (birthdays, festivals, etc.).
- Wishlists can be shared with other users.
- Backend supports CRUD operations for wishlists and ensures proper product-user association.

### 2. Influencer Reels with Product Tagging

- Influencers can upload reels showcasing products.
- Products can be tagged and viewed within reels for easy access.
- Tracks likes for engagement metrics.

### 3. Swipe-Based Product Interaction

- Users can swipe left to reject a product or swipe right to add it to a wishlist(dating-app like feel).
- Backend updates the user's preferences and wishlists accordingly.

### 4. Leaderboard for Top Reels

- Calculates weekly top reels based on engagement metrics (likes).
- Provides real-time leaderboard updates.

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

---

## Getting Started

### 1. Clone the repository

bash
git clone https://github.com/riyaaaa123/trendr-backend.git
cd trendr-backend

### 2. Create virtual environment

python -m venv venv
source venv/bin/activate
