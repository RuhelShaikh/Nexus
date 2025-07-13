# Smart Monitoring System for Identifying Drug Trafficking on Social Media

## Project Statement

_CONNECT_ ------ _DETECT_ ------ _PROTECT_

## Solution

- _Illegal Activities on Messaging Platforms_:

  - Messaging platforms are exploited for illegal activities such as drug trafficking by leveraging anonymity and encryption.

- _Controlled Environment for Detection_:

  - A dummy social media platform is created as a controlled environment to detect and analyze trafficking activities.

- _AI and Data Analytics_:

  - Utilize AI and data analytics to detect suspicious posts, patterns, and networks of traffickers.

- _Tracking Identifiers_:

  - Track identifiers such as IP addresses, mobile numbers, and email IDs.

- _User-Friendly Interface_:

  - Provide real-time analytics, visual reports, and alerts for law enforcement through a user-friendly interface.

- _Streamlined Investigations_:
  - Streamline investigations by flagging suspicious activities and uncovering trafficking networks.

## Setup instructions

1. Clone the project
  - git clone https://github.com/your-org/your-repo.git
  - cd your-repo
2. Setup MongoDB
  - create a database in atlas, or local. 
3. Setup ENV file in root
  - MONGO_URI=your database URI
  - JWT_SECRET=your_secret_key
4. Download and install ollama
  - Run this command
    * ollama pull wizardlm2
5. Install dependencies
  - cd Social_Media_App/frontend
    * npm install

  - cd ../backend
    * npm install

  - cd ../../Dashboard/UI
    * npm install

  - For Python backend
    * pip install -r requirements.txt
6. To run the project
  - In ollama, run this command 
    * ollama serve  
  - cd Dashboard/UI
    * npm run dev
  - cd Social_Media_App/backend
    * npm start
  - cd Social_Media_App/frontend
    * npm run dev

## Features

1. IP Reputation Check
2. Device Fingerprint
3. Get IP
4. Geolocation
5. Encrypt Passwords (with storage in the database)
6. Detect VPN
7. User Flagging
8. Photo/Image Hosting
9. Compliance: GDPR and CCPA (DPDPDA)

### Flag Activation

- Turn On: If someone uses unwanted keywords.

## Risk Score Calculation

### Factors

- Transaction Volume
- Location Risk
- Behavior Pattern
- Network Analysis

### Risk Score Formula

Risk Factor = (Post Frequency Score + Keyword Score + Location Score + Message Score) / 20 \* 100

### Risk Score Components

- Post Frequency Methodology:

  - Min [5, post count]

- Keyword Score:

  - Min [10, Length of Flagged Word]

- Message Score:

  - Min [10, (Total Coded * 0.5) + Total Positive]

- Scaling of Score (Normalization):
  - (Total Score / Maximum Score) \* 100

### Methodology of Risk Factor Counter

- Distance Calculation:
  - If the distance between user location and hotspot is within a threshold (0.1), then Risk Score = 5; otherwise, Risk Score = 0.
  - Distance Formula: Haversine

## Dashboard

- Display only the top 3 scores on the dashboard.

### Detailed Factors

- Post Counts
- Flagged Words
- Total Positive
- Total Coded (Negative)

## VPN Analysis

1. IP Information
2. Proxy Check
3. IP2Location
4. DNSB1
5. Port Scan
6. Real IP

## Methodology

### Distance Calculation: Haversine Formula

a = sin²(Δφ / 2) + cos(φ₁) _ cos(φ₂) _ sin²(Δλ / 2)  
c = 2 _ atan2(√a, √(1−a))  
d = R _ c

- _Where_:
  - φ₁, φ₂ = latitudes of the two points
  - Δφ = difference in latitudes
  - Δλ = difference in longitudes
  - R = Earth's radius (mean radius = 6,371 km)

## Compliance

- Ensure compliance with GDPR and CCPA (DPDPDA) for data protection and privacy.

## User Interface

- _Real-Time Analytics_: Display real-time data and analytics.
- _Visual Reports_: Generate visual reports for easy understanding.
- _Alerts_: Provide instant alerts to law enforcement agencies.

## Technology Stack

- _AI and Machine Learning_: For detecting suspicious activities.
- _Data Analytics_: To analyze patterns and networks.
- _Database_: Secure storage of encrypted passwords and user data.
- _Frontend_: User-friendly dashboard for visual reports and alerts.
- _Backend_: Robust server-side logic for processing and tracking.

## Implementation Steps

1. Set Up Controlled Environment: Develop a dummy social media platform.
2. Integrate AI and Data Analytics: Implement algorithms for detecting suspicious activities.
3. Develop Tracking Mechanisms: Track IP addresses, mobile numbers, and email IDs.
4. Create User Interface: Design and develop the dashboard for real-time analytics and alerts.
5. Implement Security Features: Encrypt passwords, detect VPNs, and ensure compliance with GDPR and CCPA.
6. Testing and Deployment: Test the system thoroughly and deploy for use by law enforcement.

## Conclusion

The Smart Monitoring System aims to connect, detect, and protect by leveraging advanced AI and data analytics to identify and prevent drug trafficking activities on social media platforms. By providing law enforcement with real-time insights and actionable data, the system facilitates effective investigations and helps dismantle trafficking networks.
