# 🎬 SmartFlix – AI-Powered Movie Recommendation Web App

SmartFlix is a full-stack AI-powered movie recommendation web app. It helps users find movies based on their mood or preferences using an intelligent recommendation engine, the TMDB API, and AWS cloud services.

## 🚀 Project Features

- 🔍 Search & recommend movies based on mood/genre
- 🎞️ Live metadata & posters from TMDB API
- 🤖 AI-based recommendation engine (cosine similarity)
- 📦 AWS S3 for config storage
- 💾 AWS DynamoDB for user preferences & favorites
- ☁️ AWS Elastic Beanstalk for Flask app hosting
- 🔐 Optional: Amazon Cognito for user authentication
- 
## 🧱 Architecture

                 ┌─────────────────────────────┐
                 │        User (Web UI)        │
                 └────────────┬────────────────┘
                              │
                      HTTP Requests
                              ▼
       ┌────────────────────────────────────────────┐
       │        Flask Backend (Python API)          │
       │        + Recommendation Engine             │
       └────┬───────────────────────┬───────────────┘
            │                       │
            ▼                       ▼
     TMDB API for Movie Data   AWS Services (below)



## 🧰 Tech Stack

| Layer             | Technology                                |
|------------------|--------------------------------------------|
| Frontend         | HTML, Bootstrap, Jinja2                    |
| Backend API      | Python, Flask                              |
| Recommendation   | Scikit-learn, Pandas                       |
| Movie Metadata   | TMDB API                                   |
| Cloud Hosting    | AWS Elastic Beanstalk                      |
| Config Storage   | AWS S3                                     |
| User Data Store  | AWS DynamoDB                               |
| Logging          | AWS CloudWatch                             |

## 📁 Project Structure

```bash
smartflix/
├── app/            # Flask core app (routes, logic)
├── config/         # Config files (e.g., mood to genre mappings)
├── .ebextensions/  # AWS EB config files
├── application.py  # App entry point
