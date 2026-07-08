# 🚗 Autonomous Insurance Claims Processing Agent

An AI-powered application that extracts important information from First Notice of Loss (FNOL) documents and recommends the appropriate claim processing route using Google's Gemini API.

## 📌 Features

- Upload FNOL documents (.pdf or .txt)
- Extract claim details using Gemini AI
- Display extracted fields in JSON format
- Automatically recommend claim routing
- Handles different claim scenarios:
  - ✅ Fast-track
  - 🔍 Investigation Flag
  - 👨‍💼 Specialist Queue
  - 📋 Manual Review

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- pdfplumber
- python-dotenv
- JSON

---

## 📂 Project Structure

```
insurance_claim_agent/
│
├── app.py
├── extractor.py
├── router.py
├── validator.py
├── requirements.txt
├── README.md
├── .env
├── fast_track.txt
├── fraud_case.txt
├── injury_case.txt
└── manual_review.txt
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Sakshi-web-cmd/insurance-claim-agent.git
```

Move into the project

```bash
cd insurance-claim-agent
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

## 🚀 Workflow

1. Upload an FNOL document.
2. Extract text from the document.
3. Gemini AI extracts structured claim information.
4. Business rules determine the routing decision.
5. Display extracted fields and routing result.

---

## 📊 Routing Rules

| Condition | Recommended Route |
|-----------|-------------------|
| Missing mandatory fields | Manual Review |
| Fraud keywords detected | Investigation Flag |
| Injury claim | Specialist Queue |
| Damage below ₹25,000 | Fast-track |
| Otherwise | Normal Queue |

---

## 🧪 Sample Test Files

- fast_track.txt
- fraud_case.txt
- injury_case.txt
- manual_review.txt

---

## 📷 Output

The application displays:

- Extracted Claim Fields
- Recommended Claim Route
- Reason for Recommendation

---

## 👩‍💻 Author

**Sakshi Hiremath**

GitHub:
https://github.com/Sakshi-web-cmd

---

## 📄 License

This project is created for educational and learning purposes.